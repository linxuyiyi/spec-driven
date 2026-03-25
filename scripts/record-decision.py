#!/usr/bin/env python
"""Record a decision to the knowledge base."""

import argparse
import sys
from datetime import datetime
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description='Record an architecture decision')
    parser.add_argument('title', help='Decision title')
    parser.add_argument('--background', '-b', required=True, help='Background description')
    parser.add_argument('--decision', '-d', required=True, help='Final decision')
    parser.add_argument('--reason', '-r', required=True, help='Reason for decision')
    parser.add_argument('--options', '-o', nargs='+', help='Considered options')
    parser.add_argument('--author', '-a', default='Agent', help='Decision author')
    parser.add_argument('--output', '-O', default='knowledge/decisions/', help='Output directory')
    
    args = parser.parse_args()
    
    # Generate filename
    date = datetime.now().strftime('%Y-%m-%d')
    slug = args.title.lower().replace(' ', '-').replace('/', '-')
    filename = f"{slug}.md"
    
    # Count existing decisions for numbering
    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)
    existing = list(output_dir.glob('*.md'))
    number = len(existing) + 1
    
    # Generate content
    content = f"""# {number:03d} - {args.title}

## 背景

{args.background}

## 可选方案

"""
    
    if args.options:
        for i, option in enumerate(args.options, 1):
            content += f"### 方案 {i}: {option}\n\n**优点**:\n\n**缺点**:\n\n"
    else:
        content += "### 方案 A\n\n**优点**:\n\n**缺点**:\n\n"
    
    content += f"""
## 最终决策

{args.decision}

## 决策理由

{args.reason}

## 影响

### 积极影响



### 潜在风险



## 时间线

- **决策日期**: {date}
- **决策人**: {args.author}

## 标签

#architecture #decision
"""
    
    # Write file
    filepath = output_dir / filename
    filepath.write_text(content)
    
    print(f"Decision recorded: {filepath}")
    return 0


if __name__ == '__main__':
    sys.exit(main())
