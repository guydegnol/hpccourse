## High Performance Computing

This project is an introduction course on HPC


##### Cuda extensions

- Load Extension
```python:
import IPython
hpcourse.load_extra_magics(IPython.get_ipython())
# or 
hpcourse.ipsa_login("login", IPython.get_ipython())
```

- Cuda basic extension: it compiles C/C++ code and exec it
```c:
%%ipsa_nvcudac_and_exec
#include <iostream>
int main() {
    for (int i = 0; i <= 10; ++i) {
        std::cout << i << std::endl;
    }
}
```

- Cuda most sophisticated method
> `%%ipsa_nvcudac --name example.cu --compile false`
>> NOTE: The cell must contain either code or comments to be run successfully. 
>> It accepts 2 arguments. `-n` | `--name`  - which is the name of either CUDA source or Header
>> The name parameter must have extension `.cu` or `.h`
>> Second argument `-c` | `--compile`; default value is `false`. The argument is a flag to specify
>> if the cell will be compiled and run right away or not. It might be usefull if you're playing in
>> the `main` function

- To compile and run all CUDA files you need to run
```python
%%cuda_run
# This line just to bypass an exeption and can contain any text
```

### Program

- Program:
 - 1/5 (2h): Nov-09/13:30
    - Introduction HPC (45m)
    - Introduction to git (30m)
    - Check students configs (45m)
 - 2/5 (4h): Nov-10/08:30
    - Course: notebook/pandas/numpy/matplotlib (55m)
    - Exercice: notebook/pandas/numpy/matplotlib (55m)
    - Improve: code efficiency (55m)
    - Course: basic C/C++  (55m)
 - 3/5 (4h): Nov-17/08:30
    - Exercice: basic C/C++ (55m)
    - Exercice: code efficiency (55m)
    - Course: multithreading (CPU/GPU) CUDA (55m)
    - Exercice: multithreading (CPU/GPU) (55m)
 - 4/5 (4h): Dec-01/08:30
    - Course: examples of resolutions (55m)
    - Exercice: multithreading (CPU/GPU) (55m)
    - Course: Same problem with noisy data (15m)
    - Exercice: multithreading (CPU/GPU) (55m)
    - Open questions: (55m)
 - 5/5 (4h): Dec-07/13:30
    - Course: examples of resolutions (15m)
    - Exercice: multithreading (CPU/GPU) (1h30)
    - Course: examples of resolutions (15m)
    - Exercice: multithreading (CPU/GPU) (1h30)
    - Open questions: (55m)

# Cours Omar
https://www.overleaf.com/project/5efda0c4d82afb0001032586


# Mandelbrot
python
https://github.com/harrism/numba_examples
c/c++
https://github.com/cristian-szabo-university/mandelbrot-cuda/tree/master/Mandelbrot

