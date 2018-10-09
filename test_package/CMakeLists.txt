cmake_minimum_required(VERSION 3.4)
project(test_package)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

#test via find_package method
message(STATUS "testing via find_package method")
message(STATUS "finding SnoreGrowl")
find_package(SnoreGrowl REQUIRED)
message(STATUS "finding SnoreGrowl++")
find_package(SnoreGrowl++ REQUIRED)
add_executable(test_find_package main.cpp)
target_link_libraries(test_find_package Snore::SnoreGrowl++ Snore::SnoreGrowl)

message(STATUS "testing via manual linkage")
add_executable(test_manual_conan main.cpp)
target_link_libraries(test_manual_conan CONAN_PKG::snoregrowl++)
