#ifndef GRIDMAP_HPP
#define GRIDMAP_HPP

#include "grid_node.hpp"
#include <iostream>
#include <vector>
#include <set>
#include <map>

class GridMap{
public:
  GridMap(){}

  /*
  Constructor

  Args:

  */
  GridMap(
    unsigned threshold,
    unsigned char bit_depth,
    unsigned min_x,
    unsigned min_y):
    threshold(threshold),
    bit_depth(bit_depth),
    min_x(min_x),
    min_y(min_y){}

  void get_nodes(
    std::vector<GridNode*> nodes,
    unsigned x_min,
    unsigned y_min,
    unsigned x_max,
    unsigned y_max);

  bool overlaps(
    unsigned x_min,
    unsigned x_max,
    unsigned y_min,
    unsigned y_max);

  void add(
    unsigned x,
    unsigned y,
    int value);

private:
  //member variables
  unsigned threshold = 5; //how many nodes can be held
  unsigned bit_depth = 8; //how deep can this GridMap be?
  unsigned min_x = 0;
  unsigned min_y = 0;
  std::vector<GridNode*> nodes; //temporary till better ds created
  std::vector<GridMap*> sub_grids; //size four?

  //private functions
  unsigned char get_index(unsigned v){ return (v >> this->bit_depth-1)&1; }
  void add_node(GridNode* n);

};

#endif
