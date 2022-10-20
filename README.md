## High Performance Computing

This project is an introduction course on HPC

### V2 is available

V2 brings support of multiple source and header files.

##### Usage

- Load Extension
> `%load_ext nvcc_plugin`

- Mark a cell to be treated as cuda cell
> `%%cuda --name example.cu --compile false`
>> NOTE: The cell must contain either code or comments to be run successfully. 
>> It accepts 2 arguments. `-n` | `--name`  - which is the name of either CUDA source or Header
>> The name parameter must have extension `.cu` or `.h`
>> Second argument `-c` | `--compile`; default value is `false`. The argument is a flag to specify
>> if the cell will be compiled and run right away or not. It might be usefull if you're playing in
>> the `main` function

- To compile and run all CUDA files you need to run
```
%%cuda_run
# This line just to bypass an exeption and can contain any text


```


##### Admin
https://www.geeksforgeeks.org/how-to-run-cuda-c-c-on-jupyter-notebook-in-google-colaboratory/

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

#### 2 hours git
https://www.donnfelker.com/git/

#### 2 hours git
https://www.donnfelker.com/git/

