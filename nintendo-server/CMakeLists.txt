cmake_minimum_required(VERSION 3.10)
project(ds_tcp_server)

set(CMAKE_CXX_STANDARD 17)

include_directories(/opt/devkitpro/libnds/lib)
include_directories(/opt/devkitpro/libnds/include)
include_directories(/opt/devkitpro/libnds/include/nds)
include_directories(/opt/devkitpro/libnds/include/nds/arm9)
include_directories(/opt/devkitpro/devkitARM)
link_directories(/opt/devkitpro/libnds/lib)
link_directories(/opt/devkitpro/libnds/include)
link_directories(/opt/devkitpro/libnds/include/nds)
link_directories(/opt/devkitpro/libnds/include/nds/arm9)


add_executable(ds_tcp_server source/main.cpp)