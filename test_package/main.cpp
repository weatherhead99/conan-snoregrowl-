#include <iostream>
#include <snoregrowl/growl.hpp>

int main(int argc, char** argv)
{
  Growl grl(GROWL_TCP, "dummy_password", "dummy_application");

  std::cout << "initialized Growl object..." << std::endl;
  
  

};
