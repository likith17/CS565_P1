import unittest
from mission1 import Solution  # Importing the Solution class

class TestMission1(unittest.TestCase):
    def test_mission1(self):
        sol = Solution()
        grid = [["1","1","1","1","0"],
                ["1","1","0","1","0"],
                ["1","1","0","0","0"],
                ["0","0","0","0","0"]]
        self.assertEqual(sol.mission1(grid), 1)  # Expected output: 1

if __name__ == "__main__":
    unittest.main()
