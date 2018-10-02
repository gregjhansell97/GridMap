#include "grid_map.hpp"

using std::cout;
using std::endl;
using std::pair;
using std::set;
using std::vector;

void GridMap::get_nodes(
    vector<GridNode*> nodes,
    unsigned x_min,
    unsigned y_min,
    unsigned x_max,
    unsigned y_max){
  return;
}

bool GridMap::overlaps(
    unsigned x_min,
    unsigned x_max,
    unsigned y_min,
    unsigned y_max){
  return false;
}

void GridMap::add(unsigned x, unsigned y, int value){
  this->add_node(new GridNode(x, y, value));
}

void GridMap::add_node(GridNode* n){
  return;
}
