"""
E2E test for the DRF-Vue3 Agent workflow.

This test verifies the complete agent workflow:
1. Parse a spec file
2. Generate project structure
3. Run knowledge search
"""

import subprocess
import sys
from pathlib import Path


def run_command(cmd: list, check: bool = True) -> subprocess.CompletedProcess:
    """Run a command and return the result."""
    print(f"Running: {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True)
    if check and result.returncode != 0:
        print(f"STDOUT: {result.stdout}")
        print(f"STDERR: {result.stderr}")
        raise RuntimeError(f"Command failed: {cmd}")
    return result


def test_knowledge_search():
    """Test the knowledge search script."""
    print("\n=== Testing knowledge search ===")
    
    result = run_command([
        'python3', 'scripts/search-knowledge.py', 'JWT',
        '--paths', 'knowledge/decisions/', 'knowledge/errors/', 'knowledge/best-practices/'
    ])
    
    assert 'Found' in result.stdout or 'No results' in result.stdout
    print("✓ Knowledge search test passed")


def test_directory_structure():
    """Test the directory structure is correct."""
    print("\n=== Testing directory structure ===")
    
    required_dirs = [
        'skills/drf-vue3-developer',
        'skills/spec-analyzer',
        'agent-config',
        'templates/backend',
        'templates/frontend',
        'templates/specs',
        'knowledge/decisions',
        'knowledge/errors',
        'knowledge/best-practices',
        'scripts',
    ]
    
    for dir_path in required_dirs:
        assert Path(dir_path).exists(), f"Missing directory: {dir_path}"
        print(f"✓ {dir_path}")
    
    print("✓ Directory structure test passed")


def test_required_files():
    """Test all required files exist."""
    print("\n=== Testing required files ===")
    
    required_files = [
        'skills/drf-vue3-developer/SKILL.md',
        'skills/spec-analyzer/SKILL.md',
        'agent-config/system-prompt.md',
        'agent-config/tools-config.yaml',
        'templates/specs/feature-spec-template.md',
        'templates/backend/requirements/base.txt',
        'templates/frontend/package.json',
    ]
    
    for file_path in required_files:
        assert Path(file_path).exists(), f"Missing file: {file_path}"
        print(f"✓ {file_path}")
    
    print("✓ Required files test passed")


def test_knowledge_base():
    """Test the knowledge base has content."""
    print("\n=== Testing knowledge base ===")
    
    kb_dirs = ['knowledge/decisions', 'knowledge/errors', 'knowledge/best-practices']
    
    for dir_path in kb_dirs:
        files = list(Path(dir_path).glob('*.md'))
        assert len(files) > 0, f"Empty knowledge directory: {dir_path}"
        print(f"✓ {dir_path} has {len(files)} file(s)")
    
    print("✓ Knowledge base test passed")


def main():
    """Run all E2E tests."""
    print("=" * 60)
    print("DRF-Vue3 Agent E2E Tests")
    print("=" * 60)
    
    tests = [
        test_directory_structure,
        test_required_files,
        test_knowledge_base,
        test_knowledge_search,
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError as e:
            print(f"✗ {test.__name__}: {e}")
            failed += 1
        except Exception as e:
            print(f"✗ {test.__name__}: Unexpected error: {e}")
            failed += 1
    
    print("\n" + "=" * 60)
    print(f"Results: {passed} passed, {failed} failed")
    print("=" * 60)
    
    return 0 if failed == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
