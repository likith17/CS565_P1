import unittest
from mission4 import Solution  # Importing the Solution class

class TestMission4(unittest.TestCase):
    def test_mission4(self):
        sol = Solution()
        grid = [[1,2,3],
                [4,0,5]]
        self.assertEqual(sol.mission4(grid), 1)  # Expected output: 1

if __name__ == "__main__":
    unittest.main()
