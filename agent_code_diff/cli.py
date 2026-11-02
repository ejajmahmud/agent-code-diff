"""Command line interface for agent-code-diff."""
from .differ import compute_unified_diff

def main():
    s1 = "def hello():\n    print('hi')\n"
    s2 = "def hello():\n    print('hello world')\n"
    print(compute_unified_diff(s1, s2))

if __name__ == "__main__":
    main()
