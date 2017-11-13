### Introduction

In `Linux` like system, there is a library called `pthread`, it provides couples of functions to `init, create, join` a thread.

In C++ 11, it supports multi-thread program natively.

### Header files

```cpp
#include <thread>
#include <mutex>
```

### Demos

#### Function without argumens

A simple program to start a thread, everything will be stored in a file `main.cc`.

```cpp
#include <iostream>
#include <thread>

void Bingo() {
    std::cout << "Bingo" << std::endl;
}

int main(int argc, char* argv[]) {
    std::thread t(Bingo);
    t.join();
    return EXIT_SUCCESS;
}
```

```makefile
g++ -std=c++11 main.cc
```

#### Function with arguments

```cpp
#include <iostream>
#include <thread>

void Bingo(int id) {
    std::cout << "Bingo: " << id <<std::endl;
}

int main(int argc, char* argv[]) {
    std::thread t(Bingo, 3);
    t.join();
    return EXIT_SUCCESS;
}
```

#### Function of an instance

```cpp
#include <iostream>
#include <thread>

class Bingo {
public:
    void SayBingo() {
        std::cout << "Bingo" << std::endl;
    }
};

int main(int argc, char* argv[]) {
    Bingo b;
    std::thread t(&Bingo::SayBingo, &b);
    t.join();
    return EXIT_SUCCESS;
}
```

#### Creation of multiple threads

```cpp
#include <iostream>
#include <thread>

void Bingo() {
    std::cout << "Bingo" << std::endl;
}

int main(int argc, char* argv[]) {
    const int THREAD_NUM = 4;
    std::thread t[THREAD_NUM];
    for (int i = 0; i < THREAD_NUM; ++i) {
        t[i] = std::thread(Bingo);
    }
    for (int i = 0; i < THREAD_NUM; ++i) {
        t[i].join();
    }
    return EXIT_SUCCESS;
}
```

