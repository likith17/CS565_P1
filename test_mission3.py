import unittest
from mission3 import Solution  # Importing the Solution class

class TestMission3(unittest.TestCase):
    def test_mission3(self):
        sol = Solution()
<<<<<<< HEAD
        grid = [[2,2,2],
                [3,8,2],
                [4,3,4]]
        self.assertEqual(sol.mission3(grid), 1)  # Expected output: 1
=======
        grid = [[1,2,2],
                [3,8,2],
                [5,3,5]]
        self.assertEqual(sol.mission3(grid), 2)  # Expected output: 2
>>>>>>> ffee56bbaa765a5ed51f4d86f6932595c6ca3b46

if __name__ == "__main__":
    unittest.main()
