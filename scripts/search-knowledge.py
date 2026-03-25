#!/usr/bin/env python
"""Search the knowledge base."""

import argparse
import sys
from pathlib import Path


def search_knowledge(query: str, paths: list, case_sensitive: bool = False) -> list:
    """Search for query in knowledge base files."""
    results = []
    flags = 0 if case_sensitive else 2  # re.IGNORECASE
    
    for base_path in paths:
        base = Path(base_path)
        if not base.exists():
            continue
            
        for file in base.glob('**/*.md'):
            content = file.read_text()
            if query.lower() in content.lower() if not case_sensitive else query in content:
                # Find matching lines
                for i, line in enumerate(content.split('\n'), 1):
                    if query.lower() in line.lower() if not case_sensitive else query in line:
                        results.append({
                            'file': str(file),
                            'line': i,
                            'content': line.strip()[:100]
                        })
    
    return results


def main():
    parser = argparse.ArgumentParser(description='Search the knowledge base')
    parser.add_argument('query', help='Search query')
    parser.add_argument('--paths', '-p', nargs='+', 
                        default=['knowledge/decisions/', 'knowledge/errors/', 'knowledge/best-practices/'],
                        help='Paths to search')
    parser.add_argument('--case-sensitive', '-c', action='store_true', help='Case sensitive search')
    parser.add_argument('--limit', '-l', type=int, default=20, help='Max results')
    
    args = parser.parse_args()
    
    results = search_knowledge(args.query, args.paths, args.case_sensitive)
    
    if not results:
        print(f"No results found for '{args.query}'")
        return 0
    
    print(f"Found {len(results)} results for '{args.query}':\n")
    
    for i, r in enumerate(results[:args.limit], 1):
        print(f"{i}. {r['file']}:{r['line']}")
        print(f"   {r['content']}")
        print()
    
    if len(results) > args.limit:
        print(f"... and {len(results) - args.limit} more results")
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
