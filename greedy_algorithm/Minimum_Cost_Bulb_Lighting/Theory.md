### Minimum_Cost_Bulb_Lighting - Theory
<hr>

#### Concepts required to solve the problem:

1. **String Manipulation**: The problem requires manipulating a string representing the status of bulbs. This involves operations such as reversing substrings and inverting the status of bulbs in substrings.

2. **Counting Groups of 0's**: The minimum cost required to light up all the bulbs depends on the number of groups of consecutive 0's in the string. We need to count these groups.

3. **Cost Calculation**: The cost to reverse a substring is denoted by 'X' and the cost to invert the status of bulbs in a substring is denoted by 'Y'. We need to calculate the minimum cost to light up all the bulbs based on the number of zero groups and the given costs.
   
   Calculation Steps:
   - If there are no zero groups, the cost is 0.
   - If there are one or more zero groups, the cost is calculated as (number of zero groups - 1) * min(X, Y) + Y. This is because we can reverse all but one zero group and invert the status of the remaining group.

#### Data Structure:

The problem does not require any specific data structure.

#### Algorithm:

The algorithm to solve the problem can be summarized as follows:

1. Read the input values n, X, Y and the string s representing the status of the bulbs.

2. Count the number of zero groups in the string s. Starting from the second bulb, whenever a '0' is encountered after a '1', increment the count of zero groups.

3. Calculate the minimum cost based on the number of zero groups and the given costs.

4. Print the minimum cost.

#### Example:

Let's consider the given example to understand the algorithm.

Input:
```
5 1 10
01000
```

Output:
```
11
```

Explanation:
- The string "01000" has 2 zero groups. 
- We can reverse the substring (0, 1) to get "10000" with a cost of 1.
- Then, we can invert the substring (1, 4) to get "11111" with a cost of 10.
- The total cost is 1 + 10 = 11.

#### Questions similar to the given problem:

1. Given a string representing the status of bulbs, find the minimum cost to make all the bulbs 'ON'. The cost to reverse a substring is X and the cost to invert the status of bulbs in a substring is Y.

2. You are given a binary string of length n, where '0' represents a faulty bulb and '1' represents a working bulb. The cost to repair a faulty bulb is X and the cost to replace a working bulb is Y. Find the minimum cost to have all working bulbs.

#### Code Solution in C++:

```cpp
#include<bits/stdc++.h>
using namespace std;

int main() {
    int n, X, Y;
    cin >> n >> X >> Y;

    string s;
    cin >> s;

    int count = 0;
    if (s[0] == '0')
        count++;

    for (int i = 1; i < n; i++) {
        if (s[i] == '0' && s[i-1] == '1')
            count++;
    }

    int cost;
    if (count == 0)
        cost = 0;
    else
        cost = (count - 1)*min(X, Y) + Y;

    cout << cost << endl;
    
    return 0;
}
```

#### Explanation of the above code:

1. Read the input values n, X, Y and the string s representing the status of the bulbs.

2. Initialize a variable `count` to store the number of zero groups.

3. If the first element of s is '0', increment `count` by 1.

4. Iterate over the characters of s starting from the second element. If a '0' is encountered after a '1', increment `count` by 1.

5. Calculate the minimum cost based on `count`. If `count` is 0, set `cost` to 0. Otherwise, calculate `cost` as (count - 1) * min(X, Y) + Y.

6. Print the minimum cost.

#### Output:

```
11
```
<hr>
