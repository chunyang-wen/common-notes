GCC/G++ compiles content from `/dev/stdin`

```makefile
echo "int main() {}" | g++ -x c++ -Wall -o a.out -
echo "int main() {}" | g++ -x c -Wall -o a.out -
```
