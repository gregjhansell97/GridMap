#ifndef GRIDNODE_HPP
#define GRIDNODE_HPP

class GridNode{
public:
  GridNode(
    unsigned x,
    unsigned y,
    int data):
    x(x), y(y), data(data){}
  unsigned x;
  unsigned y;
  int data;
};

#endif
