import unittest
from mission4 import Solution  # Importing the Solution class

class TestMission4(unittest.TestCase):
    
    def test_mission4(self):
        sol = Solution()

        # Test case 1: Already solved
        grid1 = [[1, 2, 3],
                 [4, 5, 0]]
        self.assertEqual(sol.mission4(grid1), 0)  # Expected output: 0

        # Test case 2: One move away
        grid2 = [[1, 2, 3],
                 [4, 0, 5]]
        self.assertEqual(sol.mission4(grid2), 1)  # Expected output: 1

        # Test case 3: Two moves away
        grid3 = [[1, 2, 3],
                 [0, 4, 5]]
        self.assertEqual(sol.mission4(grid3), 2)  # Expected output: 2

        # Test case 4: Three moves away
        grid4 = [[1, 0, 3],
                 [4, 2, 5]]
        self.assertEqual(sol.mission4(grid4), 2)  # Expected output: 2
        
        # test case 5: unsolvable
        grid5 = [[1,0,5],
                 [4,0,3]]
        self.assertEqual(sol.mission4(grid5), "Alert!!!")
if __name__ == "__main__":
    unittest.main()
