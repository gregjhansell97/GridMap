#include "grid_map.hpp"

using std::cout;
using std::endl;
using std::pair;
using std::set;
using std::vector;

void GridMap::add(unsigned x, unsigned y, int value){
  GridNode* n = new GridNode(x, y, value);
  this->add(n);
}


//TODO: finish this bruh
vector<int> GridMap::get_values(unsigned x, unsigned y, unsigned radius){
  if(this->sub_grids.size() > 0){
    set<pair<unsigned, unsigned> > coordinates;
    bool sub;
    bool add_y;
    bool add_x;
    for(unsigned i = 0; i < 8; i++){
      if(sub){
        unsigned x_index = x%this->width
      }else{

      }
      unsigned x_index = x +
      coordinates.
    }
    unsigned x_index = node->x%this->width;
    unsigned y_index = node->y%this->height;
  }else{

  }
  vector<int> values;



  cout << "getting values" << endl;
  return values;
}

void GridMap::add(GridNode* node) {
  if(this->sub_grids.size() > 0){
    unsigned x_index = node->x%this->width;
    unsigned y_index = node->y%this->height;
    node->x /= this->width;
    node->y /= this->height;
    sub_grids[x_index*this->height + y_index].add(node);
  }else{
    this->nodes.push_back(node);
    if(this->nodes.size() > threshold){
      this->create_sub_grids();
    }
  }
}

void GridMap::create_sub_grids(){
  if(this->depth == 0) return; //cannot go deeper
  unsigned size = this->width*this->height;
  this->sub_grids.resize(
    size,
    GridMap(
      this->threshold + 1,
      this->depth - 1,
      this->width,
      this->height));
  for(GridNode* node : nodes){
    this->add(node);
  }
}
