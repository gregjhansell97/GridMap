class GridNode:
    """
    A node used in GridMap, should be light on implementation, just stores
    values. In the C++ implementation may be chained in linked lists for speed
    and memory purposes

    Attributes:
        x(int): x location of node
        y(int): y location of node
        data(Object): the data contained within the node
    """
    def __init__(self, x, y, data):
        self.x = x
        self.y = y
        self.data = data

    """
    Used for debugging purposes

    Returns:
        string
    """
    def __str__(self):
        return str((self.x, self.y)) + ": " + str(self.data)

class GridMap:
    """
    Contains GridNodes and orders them in a grid-like datastructure, so that
    the runtime to retrieve specific nodes within a given boundary is fast

    Attributes:
        threshold(int): how many nodes can be held before it should break off
            into GridMaps
        bit_depth(int): How many bytes deep the values are
        nodes([GridNode]): what nodes belong to the GridMap
        sub_grids([GridMap (2x2)]): GridMap may have 4 sub-GridMaps if there are
            enough nodes to hit the threshold
        min_x(int): lower x boundary for the map
        min_y(int): lower y boundry for the map
        max_x(int): based on min_x and bit_depth to create upper x boundary
        max_y(int): based on min_y and bit_depth to create upper y boundary
    """
    def __init__(self, threshold=1024, bit_depth=8, min_x=0, min_y=0):
        self.threshold = threshold
        self.bit_depth = bit_depth
        self.nodes = []
        self.sub_grids = []
        self.min_x = min_x
        self.min_y = min_y
        self.max_x = self.min_x + (1<<bit_depth) - 1
        self.max_y = self.min_y + (1<<bit_depth) - 1

    """
    Used for debugging purposes

    Returns:
        string
    """
    def __str__(self):
        s = "-"*50 + "\n"
        s += "Boundary: "
        s += str((self.min_x, self.min_y))
        s += " to " + str((self.max_x, self.max_y)) + '\n'
        s += "Nodes: " + str(self.nodes)
        s += "-"*50
        return s

    """
    Adds a value at a given location. Location must be in bounds
    Arguments:
        x(int): x location of value
        y(int): y location of value
        value(Object): whatever it is that you're storing

    """
    def add(self, x, y, value):
        self.add_node(GridNode(x, y, value))

    """
    Adds a GridNode. May go deeper into object structure. GridNode must be in
    bounds. Use add, not add_node to add more values
    Arguments:
        node(GridNode): the node being added
    """
    def add_node(self, node):
        """
        starts gm at current grid_map, and tries to go deeper until it can no
        longer reach any more grid maps. Then it adds the node to that grid_map
        """
        gm = self #GridMap object
        while(len(gm.sub_grids) > 0): #goes until it hits bottom
            gm.nodes.append(node)#add nodes to every grid it goes to
            x_index = gm.get_index(node.x)
            y_index = gm.get_index(node.y)
            gm = gm.sub_grids[x_index][y_index]
        gm.nodes.append(node) #finally reached deepest part of tree
        #check if grid_map reached threshold
        if len(gm.nodes) > gm.threshold and gm.bit_depth > 0:
            #creates a 2x2 matrix of GridMaps to accomodate the nodes
            thresh = gm.threshold+1 #so you don't collapse to bottom
            depth = gm.bit_depth-1 #one closer to the bottom
            m_x = gm.min_x
            m_y = gm.min_y
            half_x = 1<<depth
            half_y = 1<<depth

            #The sub grids created should split the current grid four ways even
            gm.sub_grids = [[GridMap(threshold=thresh, bit_depth=depth, min_x=m_x, min_y=m_y),
                            GridMap(threshold=thresh, bit_depth=depth, min_x=m_x, min_y=m_y + half_y)],
                            [GridMap(threshold=thresh, bit_depth=depth, min_x=m_x + half_x, min_y=m_y),
                            GridMap(threshold=thresh, bit_depth=depth, min_x=m_x + half_x, min_y=m_y + half_y)]]
            #adds the nodes from gm to it's new subgrids
            for node in gm.nodes:
                x_index = gm.get_index(node.x)
                y_index = gm.get_index(node.y)
                sub_gm = gm.sub_grids[x_index][y_index]
                sub_gm.nodes.append(node)

    """
    Given a rectangular boundary, returns the nodes that fall in that boundary
    The boundary given must be in-bounds

    Arguments:
        x_min(int): lower x boundary
        y_min(int): lower y boundary
        x_max(int): upper x boundary
        y_max(int): upper y boundary

    Returns:
        [GridNode]
    """
    def get_nodes(self, x_min, y_min, x_max, y_max):
        nodes = []
        grids = [self] #make this a queue and add heuristics?
        #using breadth first search algorithm
        while len(grids) > 0:
            gm = grids.pop()
            if len(gm.sub_grids) == 0:
                #no sub_grids, just go through and find ones in boundary
                for n in nodes:
                    #location is in boundaries
                    if x_min <= n.x <= x_max and y_min <= n.y <= y_max:
                        nodes.append(n)
            elif x_min <= gm.min_x
                and x_max >= gm.max_x
                and y_min <= gm.min_y
                and y_max >= gm.max_y:
                #boundaries larger than grid so just grab nodes
                nodes.extend(gm.nodes)
            elif gm.overlaps(x_min, y_min, x_max, y_max):
                """
                Must have sub grids otherwise would be triggered earlier
                Adds subgrids
                TODO: would there be a way to determine what blocks
                of gm overlap in the same runtime?
                """
                grids.extend([
                    gm.sub_grids[0][0],
                    gm.sub_grids[1][0],
                    gm.sub_grids[0][1],
                    gm.sub_grids[1][1]])

    """
    Used to calculate index of given value (either 1 or 0)

    Arguments:
        v: the value that's being indexed

    Returns:
        index, either 0 or 1
    """
    def get_index(self, v):
        return (v >> self.bit_depth-1)&1

    """
    Checks if rectangular block overlaps with boundary of GridMap, only works
    for integer boundaries

    Arguments:
        x_min(int): lower x boundary
        y_min(int): lower y boundary
        x_max(int): upper x boundary
        y_max(int): upper y boundary

    Returns:
        boolean: true if they do overlap, false otherwise
    """
    def overlaps(self, x_min, y_min, x_max, y_max):
        x_range = range(self.min_x,self.max_x + 1)
        y_range = range(self.min_y, self.max_y + 1)
        if (x_min in x_range and y_min in y_range)
            or (x_max in x_range and y_min in y_range)
            or (x_min in x_range and y_max in y_range)
            or (x_max in x_range and y_max in y_range):
            #one is inside the other:
            return True

        #switch view points because other block may be inside the other
        x_range = range(x_min, x_max + 1)
        y_range = range(y_min, y_max + 1)

        if (self.min_x in x_range and self.min_y in y_range)
            or (self.max_x in x_range and self.min_y in y_range)
            or (self.min_x in x_range and self.max_y in y_range)
            or (self.max_x in x_range and self.max_y in y_range):
            #one is inside the other:
            return True
        return False
