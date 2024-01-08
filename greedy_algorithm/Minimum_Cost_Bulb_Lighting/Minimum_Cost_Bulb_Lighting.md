### Minimum_Cost_Bulb_Lighting
<hr>

#### Problem Statement

A bulb can be ‘ON’ or ‘OFF’. Mr. Ramesh got ‘n’ number of bulbs and their status, whether they are ‘ON’ or ‘OFF’. Their status is represented in a string of size ‘n’ consisting of 0’s and 1’s, where ‘0’ represents the bulb is in ‘OFF’ condition and ‘1’ represents the bulb is ‘ON’. Mr. Ramesh has been given the task to light up all the bulbs.

He can perform two operations:

1. Choose any segment of bulbs and reverse them means choose any substring and reverse it. E.g. “0 110 001” -> “0 011 001”. Substring (1, 3) is reversed here. This operation will cost him Rs. ‘X’.

2. Choose any segment of bulbs and reverse their present condition. i.e. if the bulb is ‘ON’, make it ‘OFF’ and if it is ‘OFF’, make it ‘ON’. E.g. “0 011 001” -> “0 100 001”. Substring (1, 3) is complemented. This operation will cost him Rs. ‘Y’.

You need to help Mr. Ramesh determine the minimum amount of money required to light up all the bulbs.

#### Input format

The first line of the input consists of three space-separated integers: ‘n’, ‘X’, and ‘Y’. Here, ‘n’ denotes the number of bulbs, ‘X’ denotes the cost of the first operation, and ‘Y’ denotes the cost of the second operation.

The second line contains a representation string of length ‘n’ consisting of 0’s and 1’s representing whether the bulb is ‘OFF’ or ‘ON’.

#### Output format

Print a single integer denoting the minimum cost required to light up all the bulbs.

#### Constraints

* 1 <= n <= 3,00,000
* 0 <= X, Y <= 10^9

#### Sample input
```
5 1 10
01000
```

#### Sample output
```
11
```

#### Explanation

First, Reverse substring (0, 1): “01000” -> “10000”, COST = 1

Second, Invert substring (1, 4): “10000” -> “11111”, COST = 10

Total cost = 1+10 => 11
<hr>
