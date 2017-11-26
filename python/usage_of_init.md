## Usage of `__init__.py`

Python files are organized by modules. When Python sees a `__init__.py` in a directory, it knows
that it is a module.

Normally, it is empty. But it has other usages.

### `__all__` variable

In Python, we can import everything from a module. If `__all__` is defined in `__init__.py`, then
everything in the variable will be imported when `from module import *`.

### Better organization of import

If our modules directories is as follows:

```shell
- module1
  - __init__.py
  - module2
    - __init__.py
    - file.py
  - module3
    - __init__.py
```

If there is a class `File` defined in `file.py` of `module2`, we have to import like this:

```python
from module1.module2.file import File
```

But if we put `File` in `__init__.py` of `module2`, everything will seem more comfortable.

```
# contents in __init__.py of module2

from file import File

```

Then, we can import `File` this way:

```python
from module1.module2 import File
```

