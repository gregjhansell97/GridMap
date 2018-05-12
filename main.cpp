#include <iostream>
#include <vector>
#include "grid_map.hpp"
#include "grid_node.hpp"

using std::cout;
using std::endl;
using std::vector;

int main(){
  cout << "hello world" << endl;

  GridMap m(3, 2, 10, 10);
  m.add(157, 242, -18);
  vector<int> values = m.get_values(158, 250, 200);
  cout << values.size() << endl;
}
