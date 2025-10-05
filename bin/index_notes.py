import os
import re
import yaml

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


if __name__ == "__main__":
    index = index_notes('notes')
    import json
    with open('notes_index.json', 'w', encoding='utf-8') as f:
        json.dump(index, f, ensure_ascii=False, indent=4)
    print(f"Notas indexadas {len(index['all_notes'])} notas encontradas.")
    print(f"Tags encontrados: {len(index['by_tag'])} tags.")
    print(f"Conexiones encontradas: {len(index['connections'])} conexiones.")