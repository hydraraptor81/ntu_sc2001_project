Clone the repo
```
git clone https://github.com/hydraraptor81/ntu_sc2001_project.git
```

## Project 1: Integration of Merge Sort & Insertion Sort

### For Windows 

I modified the code to handle file operations properly on Windows. You can use the gcc from https://winlibs.com/, I recommend to use winget to install it. Any other C compiler works, but I will use gcc for the purposes of this guide. I used MCF+UCRT, but the other permutations using POSIX/MSVCRT will work as well.

Replace helloworld.c with the correct source file
```
gcc -Ofast -march=native -mtune=native -flto=auto -funroll-loops" -o helloworld.c -o helloworld.exe
.\helloworld.exe
```
### For MacOS/Linux

Make sure you have git, gcc and bash.

cd into src, build and run the code
```
cd ntu_sc2001_project/project1/src
./build.sh

cd ../bin
./run.sh
```
if the code is working this is the expected output
```
Enter max value in a set (e.g., 1000): 1000
Enter the number of sets (e.g., 3): 1
Generated ..//arrays/1_arr_1000.txt with values in [1, 1000]
Sorted array written to ..//sorted/sorted_1_arr_1000.txt
Time taken: 0.000083831 seconds
Number of key comparisons: 8715
...
Sorted array written to ..//sorted/sorted_1_arr_1000.txt
Time taken: 0.000040851 seconds
Number of key comparisons: 10337
...
```

You may use c_iii.sh for running with different S values, run.sh for fixed S values. 

Feel free to adjust the build flags in build.sh\
Default flags are "-Ofast -march=native -mtune=native -flto=auto -funroll-loops"\
It does not work on cross platform, remove march and mtune flags if you want the code to run on most platforms the code will be slower without the two flags.

## Project 2: The Dijkstra's algorithm

```
cd project2
```
### Setup local environment and install networkx and matplotlib
```
python -m venv lab2_env
source lab2_env/bin/activate
pip install --upgrade pip
pip install networkx matplotlib
```

### Run the code
```
python lab2.py
```
























