### Minimum_Cost_Bulb_Lighting - Solutions
<hr>

#### C++ Code with improved formatting and meaningful variable names:

```cpp
#include<bits/stdc++.h>
using namespace std;

// function to calculate the minimum of two numbers
int min(int x, int y) 
{ 
  return (x < y) ? x : y ;
}

int main()
{
    // input the number of bulbs, cost of operation X and Y respectively
    int numOfBulbs, costOfX, costOfY;
    cin >> numOfBulbs >> costOfX >> costOfY;
    
    // input the status of bulbs
    string bulbStatus;
    cin >> bulbStatus;
    
    int numZeroGroups = 0;
    if (bulbStatus[0] == '0')
        numZeroGroups++;

    // counting the number of zero groups
    for (int i = 1; i < numOfBulbs; i++) {
        if (bulbStatus[i] == '0' && bulbStatus[i-1] == '1')
            numZeroGroups++;
    }
    
    int totalCost;
    
    // calculating the minimum cost required
    if(numZeroGroups == 0)
        totalCost = 0;
    else
        totalCost = (numZeroGroups-1)*min(costOfX, costOfY) + costOfY;
    
    // output the minimum cost required to light up all the bulbs
    cout << totalCost << endl;
    
    return 0;
}
```

#### Java Code:

```java
import java.util.Scanner;

class Main {
    
    // function to calculate the minimum of two numbers
    public static int min(int x, int y) 
    { 
      return (x < y) ? x : y ;
    }
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        // input the number of bulbs, cost of operation X and Y respectively
        int numOfBulbs = sc.nextInt();
        int costOfX = sc.nextInt();
        int costOfY = sc.nextInt();
        
        // input the status of bulbs
        String bulbStatus = sc.next();
        
        int numZeroGroups = 0;
        if (bulbStatus.charAt(0) == '0')
            numZeroGroups++;
    
        // counting the number of zero groups
        for (int i = 1; i < numOfBulbs; i++) {
            if (bulbStatus.charAt(i) == '0' && bulbStatus.charAt(i-1) == '1')
                numZeroGroups++;
        }
        
        int totalCost;
        
        // calculating the minimum cost required
        if(numZeroGroups == 0)
            totalCost = 0;
        else
            totalCost = (numZeroGroups-1)*min(costOfX, costOfY) + costOfY;
        
        // output the minimum cost required to light up all the bulbs
        System.out.println(totalCost);
    }
}
```

#### Python Code:

```python
# function to calculate the minimum of two numbers
def minimum(x, y):
    return x if x < y else y

# input the number of bulbs, cost of operation X and Y respectively
num_of_bulbs, cost_of_X, cost_of_Y = map(int, input().split())

# input the status of bulbs
bulb_status = input()

num_zero_groups = 0
if bulb_status[0] == '0':
    num_zero_groups += 1
    
# counting the number of zero groups
for i in range(1, num_of_bulbs):
    if bulb_status[i] == '0' and bulb_status[i-1] == '1':
        num_zero_groups += 1
        
total_cost = 0

# calculating the minimum cost required
if num_zero_groups != 0:
    total_cost = (num_zero_groups-1)*minimum(cost_of_X, cost_of_Y) + cost_of_Y

# output the minimum cost required to light up all the bulbs
print(total_cost)
```

#### JavaScript (Node.js) Code:

```javascript
// function to calculate the minimum of two numbers
function minimum(x, y) {
    return x < y ? x : y ;
}

// input the number of bulbs, cost of operation X and Y respectively
const input = require('readline-sync').question();
const [numOfBulbs, costOfX, costOfY] = input.split(' ').map(Number);

// input the status of bulbs
const bulbStatus = input.split(' ')[1];

let numZeroGroups = 0;
if (bulbStatus[0] === '0')
    numZeroGroups++;

// counting the number of zero groups
for (let i = 1; i < numOfBulbs; i++) {
    if (bulbStatus.charAt(i) === '0' && bulbStatus.charAt(i-1) === '1')
        numZeroGroups++;
}

let totalCost = 0;

// calculating the minimum cost required
if (numZeroGroups !== 0)
    totalCost = (numZeroGroups-1)*minimum(costOfX, costOfY) + costOfY;

// output the minimum cost required to light up all the bulbs
console.log(totalCost);
```

#### Explanation:

In this problem, we are given the status of n bulbs represented by a string of 0s and 1s, where '0' represents that the bulb is 'OFF' and '1' represents that the bulb is 'ON'.

Our task is to find the minimum cost required to light up all the bulbs.

The idea behind the solution is to count the number of zero groups in the string. A zero group is defined as a substring of consecutive '0s' in the given string.

To count the number of zero groups, we iterate through the string and check if the current character is '0' and the previous character is '1'. If this condition is satisfied, it means that the current character is the starting of a zero group.

Once we have the count of zero groups, we calculate the minimum cost required as follows:

- If the count of zero groups is 0, it means that all the bulbs are already 'ON', so the cost is 0.
- If the count of zero groups is greater than 0, we calculate the total cost as (count - 1) * min(cost of operation X, cost of operation Y) + cost of operation Y. This is because for every reversal of a zero group, we need to perform the cost of operation Y. And for every reversal of a single bulb from '0' to '1', we can perform either the cost of operation X or the cost of operation Y, whichever is minimum.

Finally, we output the calculated minimum cost required.

The time complexity of this solution is O(n), where n is the number of bulbs.
<hr>
