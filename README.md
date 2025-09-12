## Project 1: Integration of Merge Sort & Insertion Sort
# Hybrid Mergesort with Insertion Sort

Hybrid algorithm works by calling Merge Sort recursively, until subarrays of size ≤ S are reached.  
Insertion Sort is used for subarrays of size ≤ S, which is efficient for small subarrays.

Thus, for N elements and size S, there are approximately N/S subarrays of size S.

## Time Complexity (Worst Case) for Pure Implementations of Merge Sort and Insertion Sort

- **Insertion Sort:** _O_(*N*²)
- **Merge Sort:** _O_(*N* log *N*)

## Time Complexity (Worst Case) for Hybrid Algorithm

### For **Insertion Sort:**

Total comparisons for Insertion Sort = $\sum_{k=1}^{S-1} k = 1 + 2 + 3 + \dots + (S-1) = \frac{S(S-1)}{2}$

Work per array is $O(S^2)$ and total work by Insertion Sort for $\frac{N}{S}$ subarrays of size S is:

$$
\frac{N}{S} \times O(S^2) = O(N S)
$$

Hence, time complexity is $O(N S)$

### For **Mergesort:**

Let $i$ be the number of iterations of Merge Sort.  
After 1 iteration: size of subarray becomes $\frac{N}{2}$  
After 2 iterations: $\frac{N}{4}$  
After 3 iterations: $\frac{N}{8}$  
After $i$ iterations: $\frac{N}{2^i}$  

Merge Sort stops when the size of the subarray reaches S, and Insertion Sort takes over.  
Thus:

$$
\frac{N}{2^i} = S \Rightarrow 2^i = \frac{N}{S} \Rightarrow i = \log_2\left(\frac{N}{S}\right)
$$

Merge cost at every level is $O(N)$  
Total cost = iterations $i \times$ merge cost at every level  
= $\log_2\left(\frac{N}{S}\right) \times N$  
= $N \log_2\left(\frac{N}{S}\right)$

Hence, time complexity is $O\left(N \log \left(\frac{N}{S}\right)\right)$

### Combined Time Complexity

Combining the two time complexities, $O(N S)$ and $O\left(N \log \left(\frac{N}{S}\right)\right)$,  
the overall time complexity for the hybrid algorithm is:

$$
O\left(N S + N \log \left(\frac{N}{S}\right)\right)
$$

## c(ii) and c(iii): Finding Optimal S Theoretically

To find optimal S theoretically,  
Total time:

$$
T(S) = N \log_2\left(\frac{N}{S}\right) + \frac{N}{S} \cdot \frac{S(S - 1)}{2} = N \log_2\left(\frac{N}{S}\right) + \frac{N(S - 1)}{2}
$$

### Derivative:

$$
\frac{dT}{dS} = -\frac{N}{S \ln(2)} + \frac{N}{2}
$$

Set derivative to zero to obtain optimal value of S:

$$
S = \frac{2}{\ln 2} \approx 2.885
$$






















