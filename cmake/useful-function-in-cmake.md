### Functions

Functions are not case sensitive, but it is suggested that we use the capaitalized version.

The parameters are separated by space or semi-colon.

```cmake
ADD_EXECUTABLE(hello a.cc;b.cc)
ADD_EXECUTABLE(hello a.cc b.cc)
```

#### Managing projects and input

+ PROJECT(project\_name)
+ ADD\_SUBDIRECTORY(source-dir \[binary-dir\] \[execlud-from-all\])

+ INCLUDE\_DIRECTORIES(dir)

```cmake
INCLUDE_DIRECTORIES([AFTER|BEFORE] [SYSTEM] dir1 dir2 ...)
```

+ LINK\_DIRECTORIES(dir1 dir2)
+ TARGET\_LINK\_LIBRARIES(target lib1 lib2)

It seems that `LINK_DIRECTORIES` shoud appear before `ADD_EXECUTABLE`.

+ AUX\_SOURCE\_DIRECTORY(dir VARIABLE)

Search for all source files under `dir` and store it into varialbe `VARIABLE`.

```cmake
AUX_SOURCE_DIRECTORY(. SRC_LIST)
ADD_EXECUTABLE(main ${SRC_LIST})
```

#### Managing projects output

+ ADD\_EXECUTABLE(name srcs)
+ ADD\_LIBRARY(name srcs)

##### ADD_LIBRARY

```cmake
ADD_LIBRARY(libname [SHARED|STATIC|MODULE]
        [EXCLUDE_FROM_ALL]
        source1 source2 ... sourceN)
```

`EXCLUDE_FROM_ALL` means the library will not be built unless it is dependent on.

### Set or get target properties

+ GET\_TARGET\_PROPERTY(VAR target property)
+ SET\_TARGET\_PROPERTIES(target PROPERTIES property-name property-value)

Some useful properties:

+ OUTPUT\_NAME: name to replace target name
+ SUFFIX: change the suffix of library
+ VERSION: so version
+ SOVERSION: API version

#### Install

```cmake
INSTALL(TARGETS myrun mylib mystaticlib
        RUNTIME DESTINATION bin
        LIBRARY DESTINATION lib
        ARCHIVE DESTINATION libstatic
       )
```

If any path is prefixed by `/`, then it is an absolute path, `CMAKE_INSTALL_PATH` will not take
effect. Otherwise, the path is `CMAKE_INSTALL_PATH/bin`, `CMAKE_INSTALL_PATH/lib`,
`CMAKE_INSTALL_PATH/libstatic`.

There are other types that can be installed.

+ FILES
+ PROGRAMS
+ DIRECTORY

```cmake
INSTALL(FILES file1 file2 DESTINATION doc)
INSTALL(PROGRAMS file1 file2 DESTINATION doc)
# difference: dir1 will be installed, dir2/* will be installed.
INSTALL(DIRECTORY dir1 dir2/ DESTINATION doc)
```

### Search for header or library

+ FIND\_PATH(var NAMES name1 name2 PATHS path1 path2)
+ FIND\_FILE
+ FIND\_LIBRARY
+ FIND\_PROGRAM
+ FIND\_PACKAGE

### Control compiler

+ ADD\_DEFINITIONS(option1 option2)

```cmake
ADD_DEFINITIONS(-DUSE_CUDA=1 -DMKL_OFF=1)
```

### Test related

+ ENABLE\_TESTING()
+ ADD\_TEST(testname Exename arg1 arg2)


### Flow control

#### IF/ELSEIF/ELSE/ENDIF

What means true in **cmake** ?

When the variable is not one of following:

+ empty
+ OFF
+ NO
+ 0
+ FALSE
+ NOTFOUND
+ <var>\_NOTFOUND

+ Logical
  + NOT var
  + a AND b
  + a OR b
+ Numerical comparison
  + string/variable LESS number
  + string/variable GREATER number
  + string/variable EQUAL number
+ String comparison and regular expression
  + string/variable LESS string
  + string/variable GREATER string
  + string/variable EQUAL string
  + string/variable MATCHES regex-expr
+ Millnaeous
  + file1 IS\_NEWER\_THAN file2
    + file1 is newer than file2; one of files does not exist. True
  + COMMAND cmd
  + EXISTS dir/file
  + IS\_DIERECTORY

#### FOREACH/ENDFOREANCH

There are three kinds of `FOREACH`.

```cmake
FOREACH(loop_var v1 v2)
ENDFOREANCH(loop_var)

FOREACH(loop_var RANGE num)
ENDFOREANCH(loop_var)

FOREACH(loop_var RANGE start end [step])
ENDFOREANCH(loop_var)
```

#### WHILE/ENDWHILE

```cmake
WHILE(condition)
ENDWHILE(condition)
```



