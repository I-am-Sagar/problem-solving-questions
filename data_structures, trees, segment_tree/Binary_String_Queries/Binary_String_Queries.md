### Binary_String_Queries
<hr>

#### Problem Statement

The fight for the best number in the globe is going to finally come to an end. The top two contenders for the best number are number 2 and number 3. It's the final the entire world was waiting for. Spectators from all across the globe came to witness the breathtaking finals.

The finals began in an astonishing way. A common problem was set for both of them which included both these numbers. The problem goes like this.

Given a binary string (that is a string consisting of only 0 and 1), they were supposed to perform two types of queries on the string:

Type 0: Given two indices l and r, print the value of the binary string from index l to r modulo 3.

Type 1: Given an index l, flip the value of that index if and only if the value at that index is 0.

The problem proved to be a really tough one for both of them. Hours passed by but neither of them could solve the problem. So both of them want you to solve this problem, and then you get the right to choose the best number in the globe.

#### Input Format

- The first line contains an integer N denoting the length of the binary string.
- The second line contains the N-length binary string.
- The third line contains an integer Q indicating the number of queries to perform.
- This is followed by Q lines where each line contains a query.

#### Output Format

For each query of Type 0, print the value modulo 3.

#### Constraints

- 1 <= N <= 10^5
- 1 <= Q <= 10^5
- 0 <= l <= r < N

#### Sample Input
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

#### Sample Output
```
2
1
2
1
```

#### Explanation

In the given sample input, we have a binary string "10010" of length 5 and 6 queries to be performed.

- For the first query of Type 0 with indices 2 and 4, the substring from index 2 to 4 is "010", which when converted into decimal and modulo 3 will give 2.
- For the second query of Type 0 with indices 2 and 3, the substring from index 2 to 3 is "01", which when converted into decimal and modulo 3 will give 1.
- For the third query of Type 1 with index 1, flipping the value at index 1 will result in the binary string "11010".
- For the fourth query of Type 0 with indices 0 and 4, the entire binary string "11010" modulo 3 will give 2.
- For the fifth query of Type 1 with index 1, the value at index 1 is already 1, so no flipping is required.
- For the sixth query of Type 0 with indices 0 and 3, the substring from index 0 to 3 is "1101", which when converted into decimal and modulo 3 will give 1.
<hr>
