#!/usr/bin/env python
"""Record an error pattern to the knowledge base."""

import argparse
import sys
from datetime import datetime
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description='Record an error pattern')
    parser.add_argument('title', help='Error title')
    parser.add_argument('--error', '-e', required=True, help='Error message/traceback')
    parser.add_argument('--scenario', '-s', required=True, help='Trigger scenario')
    parser.add_argument('--cause', '-c', required=True, help='Root cause')
    parser.add_argument('--solution', '-S', required=True, help='Solution')
    parser.add_argument('--prevention', '-p', help='Prevention measures')
    parser.add_argument('--file', '-f', help='Related file path')
    parser.add_argument('--author', '-a', default='Agent', help='Author')
    parser.add_argument('--output', '-O', default='knowledge/errors/', help='Output directory')
    
    args = parser.parse_args()
    
    # Generate filename
    date = datetime.now().strftime('%Y-%m-%d')
    slug = args.title.lower().replace(' ', '-').replace('/', '-')
    filename = f"{slug}.md"
    
    # Generate content
    content = f"""# {args.title}

## 错误现象

```
{args.error}
```

## 触发场景

{args.scenario}

## 根因分析

{args.cause}

## 解决方案

{args.solution}

## 预防措施

{args.prevention or '待补充'}

## 相关代码

{f"- 文件路径：`{args.file}`" if args.file else '待补充'}

## 时间线

- **首次出现**: {date}
- **修复时间**: {date}
- **修复人**: {args.author}

## 标签

#error #debugging
"""
    
    # Write file
    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)
    filepath = output_dir / filename
    filepath.write_text(content)
    
    print(f"Error recorded: {filepath}")
    return 0


if __name__ == '__main__':
    sys.exit(main())
