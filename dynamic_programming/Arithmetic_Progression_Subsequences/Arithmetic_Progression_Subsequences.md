### Arithmetic_Progression_Subsequences
<hr>

#### Problem Statement

Given an array of n positive integers, the task is to count the number of Arithmetic Progression subsequences in the array. As the answer could be very large, output it modulo 100001.

Note: An empty sequence or a single-element sequence is considered as an Arithmetic Progression.

#### Input format

The input consists of the following:

- The size of the array, N, on the first line.
- Elements of the array separated by spaces, on the second line.

#### Output format

Print the total number of subsequences.

#### Constraints

The constraints for the input variables are:

- 1 <= arr[i] <= 1000 (for each element in the array)
- 1 <= sizeof(arr) <= 1000 (the size of the array)

#### Sample input and output

##### Sample input 1:
```
3
1 2 3
```
##### Sample output 1:
```
8
```
##### Sample output explanation 1:
The total subsequences are: {}, { 1 }, { 2 }, { 3 }, { 1, 2 }, { 2, 3 }, { 1, 3 }, { 1, 2, 3 }

##### Sample input 2:
```
7
1 2 3 4 5 9 10
```
##### Sample output 2:
```
37
```
<hr>
