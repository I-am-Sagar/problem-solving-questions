### Binary_String_Queries - Theory
<hr>

Concepts required to solve this problem:
1. Segment Tree: The solution uses a segment tree data structure to efficiently perform queries on the given binary string. A segment tree is a binary tree where each node represents an interval of the array. The root node represents the whole array and its children represent the left and right halves. Each node stores the required information about the interval it represents, which in this case is the modulo 3 value of the binary string in that interval.

2. Modular Exponentiation: The solution uses modular exponentiation to calculate powers of 2 modulo 3. This is necessary to handle large powers without overflow.

3. Height of Segment Tree: The height of the segment tree is calculated using the formula `2 * (2^ceil(log2(n))) - 1`, where `n` is the length of the binary string. This formula ensures that the segment tree can store all the intervals of the binary string efficiently.

4. Build Function: The build function is responsible for constructing the segment tree. It starts by dividing the array into smaller intervals recursively and assigns the modulo 3 values to the corresponding nodes of the tree.

5. Update Function: The update function is used to flip the value of a specified index in the binary string. It recursively updates the segment tree by traversing down to the corresponding node and updating the interval value.

6. Query Function: The query function is used to perform type 0 queries. It recursively checks if the current interval is completely within the given query range, partially overlaps, or lies outside. Based on that, it computes and returns the required value modulo 3.

Example:
Consider the input:
```
5
10010
6
0 2 4
0 2 3
1 1
0 0 4
1 1
0 0 3
```

The length of the binary string is 5. The binary string is `10010`. There are 6 queries to be performed.

- First, the build function constructs the segment tree using the binary string. The tree is represented as an array `tree` with a length determined by the height of the segment tree.

- For the first type 0 query `0 2 4`, the query function is called with the range `0` to `4`. It checks if the current interval `0` to `4` is completely within the query range, partially overlaps, or lies outside. Since the current interval is completely within the query range, it returns the modulo 3 value of the subtree.

- For the second type 0 query `0 2 3`, the query function is called with the range `0` to `3`. The current interval overlaps with the query range, so it continues to recursively call the query function for the left and right children until it reaches the leaf nodes. It then computes and returns the required value modulo 3.

- For the first type 1 query `1 1`, the update function is called with the index `1` to flip the value of that index in the binary string. It also updates the segment tree accordingly.

- For the fourth type 0 query `0 0 4`, the query function is called with the range `0` to `4`. The current interval lies outside the query range, so it returns 0 without further recursion.

- For the fifth type 1 query `1 1`, the update function is called with the index `1` to flip the value of that index in the binary string. 

- For the sixth type 0 query `0 0 3`, the query function is called with the range `0` to `3`. The current interval overlaps with the query range, so it continues to recursively call the query function and returns the required value modulo 3.

The expected output for the above input is:
```
2
1
2
1
```

##
<hr>
