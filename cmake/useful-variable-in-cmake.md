### Varaibles

Variables can be set using `SET` command, passed in using `cmake -DVNAME=name`.

### Project level variables

+ PROJECT\_BINARY\_DIR:
+ PROJECT\_SOURCE\_DIR:
+ CMAKE\_SOURCE\_DIR
+ CMAKE\_BINARY\_DIR
+ CMAKE\_CURRENT\_SOURCE\_DIR: currently handling directories
+ CMAKE\_CURRENT\_BINARY\_DIR

There are two compling modes in `cmake`, and the later is suggested.

+ in source compiling:
  + Build directly in the source folder. This will generate a lot files that you do not want to
  care. It will pollute the source folder.
+ out source compiling
  + Mostly we first make a new directory named `build`. Then under this directory, we execute
  the command `cmake ..`

So return to the two variables above, when we are in `in-source-compiling`, `PROJECT_BINARY_DIR`
is equal to `PROJECT_SOURCE_DIR`. In the other case, `PROJECT_BINARY_DIR` is `build`.

+ ${PROJECT\_NAME}\_BINARY\_DIR
+ ${PROJECT\_NAME}\_SOURCE\_DIR

`${PROJECT_NAME}` is defined in function `PROJECT`. It is better that we do not use these
two variables, because we need to change every place if we modify the name of the project.

### Variables about install

+ CMAKE\_INSTALL\_PREFIX

```cmake
cmake -DCMAKE_INSTALL_PREFIX=/usr/xxx
```

The default values is `/usr/local`.


### Variables about output

+ EXECUTABLE\_OUTPUT\_PATH：
  + Specify the output path of executables
+ LIBRARY\_OUTPUT\_PATH
  + You guess it.

These two variables normally should be set at the place where we `ADD_EXECUTABLE` or `ADD_LIBRARY`

### Shell variables

+ CMAKE\_LIBRARY\_PATH
+ CMAKE\_INCLUDE\_PATH

```cmake
$ENV{shell-variable-name}
```

### Compiler options

+ CMAKE\_C\_FLAGS
+ CMAKE\_CXX\_FLAGS

