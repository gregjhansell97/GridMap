from grid_map import GridMap
import timeit







if __name__ == "__main__":
    gm = GridMap(5, bit_depth=10)

    for x in range(1000):
        for y in range(1000):
            gm.add(x, y, "loc:" + str((x, y)))
    gm = gm.sub_grids[1][0]
    print(gm)
    gm = gm.sub_grids[0][0]
    print(gm)
    gm = gm.sub_grids[0][0]
    print(gm)
    gm = gm.sub_grids[0][0]
    print(gm)
    gm = gm.sub_grids[0][0]
    print(gm)
    gm = gm.sub_grids[0][0]
