import os
import re
import yaml

import json

from pathlib import Path


def parse_frontmatter(content):
    match = re.match(r'^---\n(.*?)\n---\n(.*)', content, re.DOTALL)
    if match:
        return yaml.safe_load(match.group(1)), match.group(2)
    return {}, content


def extract_wiki_links(content):
    return re.findall(r'\[\[([^\]]+)\]\]', content)


def index_notes(directory):
    index = {
        'by_tag': {},
        'by_category': {},
        'connections': {},
        'all_notes': []
    }

    for md_file in Path(directory).rglob('*.md'):
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()

        frontmatter, body = parse_frontmatter(content)
        links = extract_wiki_links(body)
        title = frontmatter.get('title', md_file.stem)
        tags = frontmatter.get('tags', [])
        category = frontmatter.get('category', 'Uncategorized')
        
        note_info = {
            'title': title,
            'path': str(md_file.relative_to(directory)),
            'tags': tags,
            'category': category,
            'links': links
        }
        index['all_notes'].append(note_info)

        for tag in tags:
            if tag not in index['by_tag']:
                index['by_tag'][tag] = []
            index['by_tag'].setdefault(tag, []).append(note_info)

        index['by_category'].setdefault(category, []).append(note_info)

        index['connections'][md_file.stem] = links
    return index

def build_markdown_index(index):
    area_order = [
        'Areas', 'Backend', 'Daily', 'Database', 'DevOps', 'Frontend', 'Productivity', 'Projects', 'Resources', 'Tools', 'Topics'
    ]
    
    category_map = {
        'areas': 'Areas',
        'backend': 'Backend',
        'daily': 'Daily',
        'database': 'Database',
        'devops': 'DevOps',
        'frontend': 'Frontend',
        'productivity': 'Productivity',
        'projects': 'Projects',
        'resources': 'Resources',
        'tools': 'Tools',
        'topics': 'Topics',
    }
    
    by_category = index.get('by_category', {})
    lines = ['# Índice de notas']
    for area in area_order:
        cat_key = area.lower()
        if cat_key in by_category:
            lines.append(f'\n## {area}\n')
            
            for note in by_category[cat_key]:
                subcat = note.get('category', '')
                note_path = note['path'].replace('\\', '/')
                lines.append(f'- [{note["title"]}]({note_path})')
    return '\n'.join(lines) + '\n'


if __name__ == "__main__":
    index = index_notes('notes')
    with open('notes_index.json', 'w', encoding='utf-8') as f:
        json.dump(index, f, ensure_ascii=False, indent=4)
    print(f"Notas indexadas {len(index['all_notes'])} notas encontradas.")
    print(f"Tags encontrados: {len(index['by_tag'])} tags.")
    print(f"Conexiones encontradas: {len(index['connections'])} conexiones.")

    md_index = build_markdown_index(index)
    readme_path = Path('notes/README.md')
    
    if readme_path.exists():
        with open(readme_path, 'r', encoding='utf-8') as f:
            readme_content = f.read()
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(md_index)
        print('README.md actualizado con el nuevo índice.')
    else:
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(md_index)
        print('README.md creado con el índice de notas.')