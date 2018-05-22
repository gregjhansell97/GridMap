import unittest
from grid_map import GridMap

class TestGridMapMethods(unittest.TestCase):
    """
    SPECIFICATION TESTING, STATE VARIABLES SHOULD NOT BE TOUCHED IN TESTING
    """
    def test_baisc_add(self):
        """
        Cannot assert check add, but if there is an error, it will be thrown.
        """
        gm = GridMap(threshold=2, bit_depth=8)
        gm.add(14, 7, "hello world")
        gm.add(0, 0, "DEADBEEF")
        gm.add(255, 255, "meh")
        for x in range(300):
            for y in range(300):
                gm.add(x, y, "")
        gm.add(0, 255, None)
        gm.add(15, 31, 3.14598)




if __name__ == "__main__":
    unittest.main()
