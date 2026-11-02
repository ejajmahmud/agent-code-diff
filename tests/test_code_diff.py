"""Unit tests for agent_code_diff."""
import unittest
from agent_code_diff.differ import compute_unified_diff

class TestCodeDiff(unittest.TestCase):
    def test_diff_generation(self):
        d = compute_unified_diff("line1\n", "line2\n")
        self.assertIn("-line1", d)
        self.assertIn("+line2", d)

if __name__ == "__main__":
    unittest.main()
