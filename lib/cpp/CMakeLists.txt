# CMake version cmake@v3.10.x
cmake_minimum_required(VERSION 3.10 FATAL_ERROR)

# Project name and a few useful settings. Other commands can pick up the results
project(pycextension
    VERSION 0.1.0)

# Must use GNUInstallDirs to install libraries into correct locations on all platforms.
include(GNUInstallDirs)

# Include CMAKE
include(${CMAKE_ROOT}/Modules/FindPkgConfig.cmake)

# Build settings
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/out/)

# Add subdirectories - libraries
add_subdirectory(./lib/feature/)
