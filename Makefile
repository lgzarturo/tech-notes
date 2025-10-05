# Makefile for indexing notes

.PHONY: index search serve graph

index:
	@python3 bin/index_notes.py

search: 
	@rg --type md -i "$(q)" | fzf --preview 'bat --style=numbers --color=always --line-range :500 {}' --height 40% --layout=reverse --border
	@echo "Search complete."

serve:
	@mkdocs serve

tag:
	@rg --type md "^tags:.*$(t)" -l | fzf --preview 'bat --style=numbers --color=always --line-range :500 {}' --height 40% --layout=reverse --border

stats:
	@echo "Total notes: $$(rg --type md --files | wc -l)"
	@echo "Total tags: $$(rg --type md -o 'tags: .*' | sort -u | wc -l)"
	@echo "Total connections: $$(rg --type md -o '\[\[.*?\]\]' | sort -u | wc -l)"

graph:
	@python3 bin/generate_graph.py > graph.dot
	@dot -Tpng graph.dot -o graph.png
	@echo "Graph generated as graph.png"