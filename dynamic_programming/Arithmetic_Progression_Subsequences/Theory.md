### Arithmetic_Progression_Subsequences - Theory
<hr>

#### Concepts Required to Solve the Problem:

1. Dynamic Programming: Dynamic Programming is used to solve optimization problems by breaking them into simpler subproblems and storing the results of the subproblems to avoid redundant computations. In this problem, dynamic programming is used to calculate the number of arithmetic progression subsequences.

2. Modulo Operation: Modulo operation is used to handle large numbers and avoid overflow. In this problem, the output is modulo 100001.

3. Array Manipulation: The given array is manipulated to find the minimum and maximum elements, which are used to determine the range of the common difference of arithmetic progression subsequence.

4. Range Sum Queries: The array 'sum' is used to store the cumulative sum of previous frequencies. This is used to calculate the number of subsequence with the same common difference.

#### Data Structures and Algorithms Used:

1. Array: The array is used to store the given elements and calculate the minimum and maximum elements.

2. Dynamic Programming: The dp array is used to store the number of arithmetic progression subsequences ending at the current element.

3. Cumulative Sum: The sum array is used to store the cumulative sum of frequencies. It helps to calculate the number of subsequence with the same common difference.

#### Algorithm:

1. Find the minimum and maximum elements in the array.
2. Initialize the dp array and the sum array.
3. Iterate over all possible common differences between the minimum and maximum elements.
4. Initialize the answer to the number of elements in the array.
5. Update the dp array based on the current common difference and the previous subsequence lengths.
6. Update the answer by subtracting one from each dp value and adding it to the answer.
7. Update the sum array by adding the dp values.
8. Return the answer modulo 100001.

#### Example:

Given array: [1, 2, 3]

1. Find the minimum and maximum elements: minarr = 1, maxarr = 3
2. Possible common differences: -2, -1, 0, 1, 2
3. For common difference -2:
   - dp = [1, 1, 1]
   - ans = 4
   - sum = [1, 1, 1]
4. For common difference -1:
   - dp = [2, 2, 2]
   - ans = 6
   - sum = [3, 3, 3]
5. For common difference 0:
   - dp = [3, 3, 3]
   - ans = 9
   - sum = [6, 6, 6]
6. For common difference 1:
   - dp = [3, 3, 3]
   - ans = 12
   - sum = [9, 9, 9]
7. For common difference 2:
   - dp = [1, 1, 1]
   - ans = 15
   - sum = [10, 10, 10]
8. Return ans = 15 % 100001 = 15
<hr>
