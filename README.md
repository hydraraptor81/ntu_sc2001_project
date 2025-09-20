For Linux/MacOS, make sure you have git, gcc and bash.\
For Windows, try using WSL, if not you have to modify the source code to handle the file operations.

Clone the repo
```
git clone https://github.com/hydraraptor81/ntu_sc2001_project.git
```

## Project 1: Integration of Merge Sort & Insertion Sort

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




























