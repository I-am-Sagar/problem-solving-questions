### clear_bits
<hr>

#### Problem Statement:

You are given two integers N and i. You need to clear all bits from the Most Significant Bit (MSB) to the ith bit (start i from right to left) and return the updated N.

Counting of bits starts from 0 from right to left.

#### Input Format:

The input consists of two integers N and i, separated by a space.

#### Output Format:

Print the updated value of N.

#### Constraints:

- The values of N and i are integers.
- 0 <= N <= 10^9
- 0 <= i <= 31

#### Sample Input 1:

```
15 2
```

#### Sample Output 1:

```
3
```

#### Explanation 1:

We need to clear all bits from MSB to the 2nd bit (i.e., clear all bits except the 0th and 1st). Therefore, the updated value of N is 3.

#### Sample Input 2:

```
4 4
```

#### Sample Output 2:

```
4
```

#### Explanation 2:

We need to clear all bits from MSB to the 4th bit (i.e., clear all bits except the 0th, 1st, 2nd, 3rd, and 4th). Since N does not have any bits set from the 5th bit onwards, the value of N remains the same, which is 4.
<hr>
