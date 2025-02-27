import unittest
from mission3 import Solution  # Importing the Solution class

class TestMission3(unittest.TestCase):
    def test_mission3(self):
        sol = Solution()
        grid = [[2,2,2],
                [3,8,2],
                [4,3,4]]
        self.assertEqual(sol.mission3(grid), 1)  # Expected output: 1

if __name__ == "__main__":
    unittest.main()
