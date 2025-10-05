import os
import re
import json
import yaml
import subprocess

from pathlib import Path
from datetime import datetime
from typing import List, Dict, Optional


try:
    from rich.console import Console
    from rich.markdown import Markdown
    from rich.table import Table
    from rich.panel import Panel
    from rich.syntax import Syntax
    from rich import box
    RICH_AVAILABLE = True
except ImportError:
    RICH_AVAILABLE = False
    print("Rich library not found. Install it with 'pipenv install rich' for better output formatting.")
    subprocess.run(["pipenv", "install", "rich"])
    from rich.console import Console
    from rich.markdown import Markdown
    from rich.table import Table
    from rich.panel import Panel
    from rich.syntax import Syntax
    from rich import box

if RICH_AVAILABLE == False:
    exit(1)

console = Console()


class NoteIndex:
    def __init__(self, directory: str):
        self.directory = Path(directory)
        self.index = []
    
    def parse_frontmatter(self, content: str) -> (Dict, str):
        match = re.match(r'^---\n(.*?)\n---\n(.*)', content, re.DOTALL)
        if match:
            return yaml.safe_load(match.group(1)), match.group(2)
        return {}, content
    
    def extract_wiki_links(self, content: str) -> List[str]:
        return re.findall(r'\[\[([^\]]+)\]\]', content)

    def get_first_heading(self, content: str) -> Optional[str]:
        match = re.search(r'^(##+)\s+(.*)', content, re.MULTILINE)
        if match:
            return match.group(2).strip()
        return None
    
    def index_notes(self):
        console.print(f"[bold green]Indexing notes in directory:[/bold green] {self.directory}")

        unique_ids = set()
        for md_file in self.directory.rglob('*.md'):
            try:
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()

                frontmatter, body = self.parse_frontmatter(content)
                links = self.extract_wiki_links(body)
                title = frontmatter.get('title', md_file.stem)

                stat = md_file.stat()

                note_id = str(md_file.relative_to(self.directory))
                if note_id in unique_ids:
                    continue
                unique_ids.add(note_id)

                note = {
                    'id': note_id,
                    'path': str(md_file),
                    'filename': md_file.name,
                    'title': title,
                    'tags': frontmatter.get('tags', []),
                    'category': frontmatter.get('category', 'Uncategorized'),
                    'status': frontmatter.get('status', 'draft'),
                    'created_at': datetime.fromtimestamp(stat.st_ctime).isoformat(),
                    'updated_at': datetime.fromtimestamp(stat.st_mtime).isoformat(),
                    'related': links,
                    'content': body,
                    'size': stat.st_size,
                    'modified': datetime.fromtimestamp(stat.st_mtime).strftime('%Y-%m-%d %H:%M:%S'),
                }

                self.index.append(note)
            except Exception as e:
                console.print(f"[bold red]Error processing file {md_file}:[/bold red] {e}")
        return self.index
    
    def save_index(self, output_file: str = ".lazy_notes_index.json"):
        index_path = self.directory / output_file
        with open(index_path, 'w', encoding='utf-8') as f:
            json.dump(self.index, f, ensure_ascii=False, indent=4)
        console.print(f"[bold green]Index saved to:[/bold green] {index_path}")

    def load_index(self, index_file: str = ".lazy_notes_index.json") -> List[Dict]:
        index_path = self.directory / index_file
        if not index_path.exists():
            console.print(f"[bold red]Index file not found:[/bold red] {index_path}")
            return []

        with open(index_path, 'r', encoding='utf-8') as f:
            self.index = json.load(f)
        console.print(f"[bold green]Index loaded from:[/bold green] {index_path}")


class NoteSearcher:
    def __init__(self, index: List[Dict]):
        self.index = index

    def search(self, query: str, field: Optional[str] = None) -> List[Dict]:
        query = query.lower()
        results = []
        for note in self.index:
            match_score = 0
            match = False

            if field:
                if field == 'tags':
                    if isinstance(note.get('tags', []), list):
                        match = any(query in tag.lower() for tag in note.get('tags', []))
                        match_score = sum(1 for tag in note.get('tags', []) if query in tag.lower())
                elif field in note:
                    match = query in str(note.get(field, '')).lower()
                    match_score = str(note.get(field, '')).lower().count(query)
            else:
                match = (
                    query in note.get('title', '').lower() or
                    query in note.get('content', '').lower() or
                    any(query in tag.lower() for tag in note.get('tags', [])) or
                    query in note.get('category', '').lower()
                )
                match_score = (
                    note.get('title', '').lower().count(query) +
                    note.get('content', '').lower().count(query) +
                    sum(tag.lower().count(query) for tag in note.get('tags', [])) +
                    note.get('category', '').lower().count(query)
                )
            if match:
                results.append(note)
        return results

    def filter_by_tag(self, tag: str) -> List[Dict]:
        tag = tag.lower()
        return [note for note in self.index if tag in [t.lower() for t in note.get('tags', [])]]

    def filter_by_category(self, category: str) -> List[Dict]:
        category = category.lower()
        return [note for note in self.index if category == note.get('category', '').lower()]

    def filter_by_status(self, status: str) -> List[Dict]:
        status = status.lower()
        return [note for note in self.index if status == note.get('status', '').lower()]


class NoteViewer:
    @staticmethod
    def show_dataview(notes: List[Dict], limit: int = 50):
        if not notes:
            console.print("[bold yellow]No notes to display.[/bold yellow]")
            return
        table = Table(title=f"Found {len(notes)} notes", box=box.ROUNDED, show_lines=True, header_style="bold magenta")
        table.add_column("Title", style="bold cyan", no_wrap=False, width=40)
        table.add_column("Tags", style="magenta", width=30)
        table.add_column("Category", style="green", width=20)
        table.add_column("Status", style="yellow", width=12)
        table.add_column("Modified", style="white", width=20)
        table.add_column("Path", style="dim", width=40)

        for note in notes[:limit]:
            tags = ', '.join(note.get('tags', []) if isinstance(note.get('tags', []), list) else [])
            table.add_row(
                note.get('title', 'Untitled'),
                tags,
                note.get('category', 'Uncategorized'),
                note.get('status', 'draft'),
                note.get('modified', '-'),
                note.get('id', '-')
            )
        console.print(table)

        if len(notes) > limit:
            console.print(f"[bold yellow]Showing first {limit} notes out of {len(notes)}. Refine your search to see more.[/bold yellow]")
    
    @staticmethod
    def show_note_detail(note: Dict):
        if not note:
            console.print("[bold red]No note to display.[/bold red]")
            return
        
        title = note.get('title', 'Untitled')
        tags = ', '.join(note.get('tags', []) if isinstance(note.get('tags', []), list) else [])
        category = note.get('category', 'Uncategorized')
        status = note.get('status', 'draft')
        modified = note.get('modified', '-')
        path = note.get('id', '-')
        content = note.get('content', '')

        header = f"[bold cyan]{title}[/bold cyan]\n"
        header += f"[magenta]Tags:[/magenta] {tags} | "
        header += f"[green]Category:[/green] {category} | "
        header += f"[yellow]Status:[/yellow] {status} | "
        header += f"[white]Modified:[/white] {modified}\n"
        header += f"[dim]{path}[/dim]\n"

        console.print(Panel(header, title="Note info", style="bold blue"))
        console.print()

        md = Markdown(content)
        console.print(md)
        console.print()
        console.print(f"[dim]Path: {path}[/dim]")

    @staticmethod
    def show_stats(index: List[Dict]):
        total_notes = len(index)
        all_tags = {}
        categories = set()
        statuses = set()
        total_links = 0

        for note in index:
            all_tags.update({tag: all_tags.get(tag, 0) + 1 for tag in note.get('tags', []) if isinstance(note.get('tags', []), list)})
            if note.get('category'):
                categories.add(note.get('category'))
            if note.get('status'):
                statuses.add(note.get('status'))
            total_links += len(note.get('related', []))

        stats = f"""
        [bold green]Total notes:[/bold green] {total_notes}
        [bold magenta]Total tags:[/bold magenta] {len(all_tags)}
        [bold blue]Total categories:[/bold blue] {len(categories)}
        [bold yellow]Total statuses:[/bold yellow] {len(statuses)}
        [bold white]Total links:[/bold white] {total_links}
        """
        console.print(Panel(stats, title="Notes Statistics", style="bold green"))

        tag_counts = {}
        for note in index:
            for tag in note.get('tags', []):
                if isinstance(tag, str):
                    tag_counts[tag] = tag_counts.get(tag, 0) + 1
        
        if tag_counts:
            console.print("\n[bold magenta]Top Tags:[/bold magenta]")
            sorted_tags = sorted(tag_counts.items(), key=lambda x: x[1], reverse=True)[:10]
            for tag, count in sorted_tags:
                console.print(f"- {tag}: {count} notes")

def main():
    parser = argparse.ArgumentParser(
        description="Lazy Notes - A simple note indexing and searching tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python lazy_notes.py index --dir notes --output notes_index.json
    """
    )

    parser.add_argument('command', choices=['index', 'search', 'show', 'stats', 'tags', 'categories'], help="Command to execute")
    parser.add_argument('query', nargs='?', help="Search query or note ID", default='')
    parser.add_argument('-d', '--dir', default='notes', help="Directory containing markdown notes")
    parser.add_argument('-t', '--tag', help="Filter by tag")
    parser.add_argument('-c', '--category', help="Filter by category")
    parser.add_argument('-s', '--status', help="Filter by status")
    parser.add_argument('-l', '--limit', type=int, default=50, help="Limit number of results displayed")
    parser.add_argument('--reindex', action='store_true', help="Reindex notes before searching or showing")

    args = parser.parse_args()

    indexer = NoteIndex(args.dir)

    if args.command == 'index' or args.reindex or not indexer.load_index():
        indexer.index_notes()
        indexer.save_index()
    else:
        indexer.load_index()

    searcher = NoteSearcher(indexer.index)
    viewer = NoteViewer()

    if args.command == 'index':
        console.print(f"[bold green]Indexing completed. {len(indexer.index)} notes indexed.[/bold green]")
    elif args.command == 'search':
        if args.tag:
            results = searcher.filter_by_tag(args.tag)
        elif args.category:
            results = searcher.filter_by_category(args.category)
        elif args.status:
            results = searcher.filter_by_status(args.status)
        else:
            results = indexer.index if not args.query else searcher.search(args.query)
        viewer.show_dataview(results, limit=args.limit)
    elif args.command == 'show':
        if not args.query:
            console.print("[bold red]Please provide a note ID to show.[/bold red]")
            return
        note = None
        for n in indexer.index:
            if args.query in (n.get('id', ''), n.get('filename', ''), n.get('title', '')):
                note = n
                break
        if note:
            viewer.show_note_detail(note)
        else:
            console.print(f"[bold red]Note not found:[/bold red] {args.query}")
    elif args.command == 'stats':
        viewer.show_stats(indexer.index)
    elif args.command == 'tags':
        all_tags = set()
        for note in indexer.index:
            all_tags.update(tag for tag in note.get('tags', []) if isinstance(note.get('tags', []), list))
        console.print(f"[bold magenta]Tags ({len(all_tags)}):[/bold magenta] {', '.join(sorted(all_tags))}")
        for tag in sorted(all_tags):
            count = sum(1 for note in indexer.index if tag in (note.get('tags', []) if isinstance(note.get('tags', []), list) else []))
            console.print(f"- {tag}: {count} notes")
    elif args.command == 'categories':
        categories = {}
        for note in indexer.index:
            if note.get('category'):
                categories[note.get('category')] = categories.get(note.get('category'), 0) + 1
        console.print(f"[bold blue]Categories ({len(categories)}):[/bold blue]")
        for cat, count in sorted(categories.items(), key=lambda x: x[1], reverse=True):
            console.print(f"- {cat}: {count} notes")

if __name__ == "__main__":
    import argparse
    main()