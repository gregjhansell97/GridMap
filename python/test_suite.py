import unittest
from grid_map import GridMap

class TestGridMapMethods(unittest.TestCase):
    """
    SPECIFICATION TESTING, STATE VARIABLES SHOULD NOT BE TOUCHED IN TESTING
    """
    def test_add(self):
        """
        Cannot assert check add, but if there is an error, it will be thrown.
        """
        gm = GridMap(threshold=2, bit_depth=8)
        gm.add(14, 7, "hello world")
        gm.add(0, 0, "DEADBEEF")
        gm.add(255, 255, "meh")
        for x in range(256):
            for y in range(256):
                gm.add(x, y, "")
        gm.add(0, 255, None)
        gm.add(15, 31, 3.14598)

    def test_get_nodes(self):
        gm = GridMap(threshold=3, bit_depth=8)
        for x in range(256):
            for y in range(256):
                gm.add(x, y, str((x, y)))

        nodes = gm.get_nodes(0, 0, 255, 255)
        self.assertEqual(len(nodes), 256*256)

        nodes = gm.get_nodes(16, 32, 31, 47)
        self.assertEqual(len(nodes), (16)*(16))
        for x in range(16, 32, 1):
            for y in range(32, 48, 1):
                match = False
                for i in range(len(nodes)):
                    n = nodes[i]
                    if n.x == x and n.y == y:
                        match = True
                        nodes.pop(i)
                        break
                self.assertTrue(match)







if __name__ == "__main__":
    unittest.main()
