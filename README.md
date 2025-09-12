# ntu_sc2001_project
## Project 1: Integration of Merge Sort & Insertion Sort
Hybrid algorithm works by calling Merge Sort recursively, until subarrays of size ≤ S are reached.  
Insertion Sort is used for subarrays of size ≤ S, which is efficient for small subarrays.

Thus, for N elements and size S, there are approximately N/S subarrays of size S.

## Time Complexity (Worst Case) for Pure Implementations of Merge Sort and Insertion Sort
- **Insertion Sort:** _O_(*N*²)
- **Merge Sort:** _O_(*N* log *N*)

## Time Complexity (Worst Case) for Hybrid Algorithm
For **Insertion Sort:**
Total comparisons for Insertion Sort = $\sum_{k=1}^{S-1} k$ \= 1 + 2 + 3 + ... + (S-1)
= $\frac{S(S-1)}{2}$  

Work per array is $O\left(S^2\right)$ and total work by Insertion Sort for $\frac{N}{S}$ subarrays of size S is $\frac{N}{S} \times O\left(S^2\right) = O\left(N S\right)$\
Hence, time complexity is $O\left(N S\right)$


For **Mergesort:**
Let i be the number of iterations of Merge Sort.  
After 1 iteration: size of subarray becomes $\frac{N}{2}$  
After 2 iterations: $\frac{N}{4}$  
After 3 iterations: $\frac{N}{8}$  
After i iterations: $\frac{N}{2^i}$  

Merge Sort stops when the size of the subarray reaches S, and Insertion Sort takes over.  
Thus, $\frac{N}{2^i} = S$  
$2^i = \frac{N}{S}$  
$i \log_2(2) = \log_2\left(\frac{N}{S}\right)$  
$i = \log_2\left(\frac{N}{S}\right)$  

Merge cost at every level is $O(N)$  
Total cost = iterations i × merge cost at every level  
= $\log_2\left(\frac{N}{S}\right) \times N$  
= $N \log_2\left(\frac{N}{S}\right)$ 

Hence, time complexity is $O\left(N \log \left(\frac{N}{S}\right)\right)$

Combining the two time complexities, $O\left(N S\right)$ and $O\left(N \log \left(\frac{N}{S}\right)\right)$
overall time complexity for hybrid algorithm is $O\left(N S + N \log \left(\frac{N}{S}\right)\right)$















