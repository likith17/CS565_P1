import unittest
from mission2 import Solution  # Importing the Solution class

class TestMission2(unittest.TestCase):
    def test_mission2(self):
        sol = Solution()
        grid = [[0,1],[1,0]]
        self.assertEqual(sol.mission2(grid), 2)  # Expected output: 2
    def test_2mission2(self):
        sol = Solution()
        grid2 = [
                [0, 0, 0, 0],
                [1, 1, 0, 0],
                [0, 0, 0, 1],
                [0, 1, 0, 0]
                ]
        #print(sol.mission2(grid2))
        self.assertEqual(sol.mission2(grid2), 5) 
        
if __name__ == "__main__":
    unittest.main()
