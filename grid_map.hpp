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
    threshold(unsigned):
    depth(unsigned):
    width(unsigned):
    height(unsigned):
  */
  GridMap(
    unsigned threshold,
    unsigned depth,
    unsigned width,
    unsigned height) :
    threshold(threshold), depth(depth), width(width), height(height){}

  /*
  adds a value to the GridMap

  Args:
    x(unsigned):
    y(unsigned):
    value(int)
  */
  void add(
    unsigned x,
    unsigned y,
    int value);

  /*
  returns values that fall in the radius of x and y

  Args:
    x(unsigned):
    y(unsigned):
    radius(unsigned): the distance away
  */
  std::vector<int> get_values(
    unsigned x,
    unsigned y,
    unsigned radius);

private:
  //member variables
  unsigned threshold = 5; //how many nodes can be held
  unsigned depth = 10; //how deep can this GridMap be?
  unsigned width = 10; //how much is x hashed (for deeper GridMaps)
  unsigned height = 10; //how much is y hashed (for deeper GridMaps)
  std::vector<GridNode*> nodes; //temporary till better ds created
  std::vector<GridMap> sub_grids;
  //functions
  void create_sub_grids();
  void add(GridNode* node);
  vector<GridMap> get_sub_grids();
};

#endif
