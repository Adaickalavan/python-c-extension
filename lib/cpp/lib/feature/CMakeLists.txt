find_package(OpenMP REQUIRED)

# synthesize_bright_exposure
add_library (feature SHARED
    ./feature.c
    ./feature.h) 
target_link_libraries(feature PRIVATE OpenMP::OpenMP_CXX)    