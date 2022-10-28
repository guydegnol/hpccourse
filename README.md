## High Performance Computing

This package is a support library for a course on High Performance Programming on GPU.


```

## Program

```
# 1/5 (2h): Nov-09/13:30
01 General introduction (slides)
02 Presentation of notebooks' environment (notebook)
03 Computing Metrics (notebook)

# 2/5 (4h): Nov-10/08:30
04 Hardware architecture (slides)
05 Introduction to C/C++ (notebook)
06 GPU programming (CUDA) (slides)

# 3/5 (4h): Nov-17/08:30
07 Introduction to git (notebook)
08 GPU programming (CUDA) (notebook)
09 Languages performances: from assembly to python (notebook)

# 4/5 (4h): Dec-01/08:30
10 Parallel architecture (slides)
11 Multiprocessing (notebook)
12 Multithreading (notebook)

# 5/5 (4h): Dec-07/13:30
13 Pi calculation
14 Mandelbrot
15 Matrix multiplication
16 Cryptocurrencies

Ideas
   Convergence time
   Build a search algo
   https://fractalytics.io/moore-penrose-matrix-optimization-cuda-c
   https://github.com/ishanthilina/CUDA-Calculation-Experiements/tree/master/q1
   Dask cuda

Won't probably do
  Message Passing Programming
```

# Cours Omar
https://www.overleaf.com/project/5efda0c4d82afb0001032586


##### Cuda extensions

- Load Extension
```python:
import IPython
hpccourse.load_extra_magics(IPython.get_ipython())
# or 
hpccourse.ipsa_login("login", IPython.get_ipython())
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


ilyas.arbouhi@ipsa.fr, ghislain.astier@ipsa.fr,pierre-olivier.briat@ipsa.fr,hugo.dubois@ipsa.fr,charles.duquesnoy@ipsa.fr,ali.el-khalil@ipsa.fr,romain.gardon@ipsa.fr,
abdelrahman.gohar@ipsa.fr,deo-gratias.houenou@ipsa.fr,luca.krebs@ipsa.fr,jean-charles.lacoffe@ipsa.fr,pauline.lelievre@ipsa.fr,loic1.martinez@ipsa.fr,adrien.mennessier@ipsa.fr,
justine.molina@ipsa.fr,alessandra.paddeu@ipsa.fr,nicolas.pepin@ipsa.fr,hugo.pires@ipsa.fr,celia.seka@ipsa.fr,celine.suffys@ipsa.fr,lucas.trias@ipsa.fr,quentin.vaunac@ipsa.fr
