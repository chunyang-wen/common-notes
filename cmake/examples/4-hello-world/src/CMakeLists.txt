LINK_DIRECTORIES(/Users/chengfu/opensource/chunyang/cmake-practice/3-hello-world/build/libhello)

SET(SRC main.cc)
ADD_EXECUTABLE(main ${SRC})

INCLUDE_DIRECTORIES(/Users/chengfu/opensource/chunyang/cmake-practice/3-hello-world/build/include/)
TARGET_LINK_LIBRARIES(main libhello.a)
