### clear_bits - Theory
<hr>

To solve this problem, we need to clear all the bits from the most significant bit (MSB) to the i-th bit of a given integer N. The position of bits starts from 0 from the right side.

The solution code uses a bitwise operation called "bitwise AND" to clear the desired bits. Here is a detailed explanation of the solution:

1. The function `clearAllBits` takes two integer parameters: `n` (the given number) and `i` (the position of the bit to start clearing from).
2. Inside the function, a mask is created using bitwise left shift (`<<`) and subtraction (`-`) operations. The mask is generated as follows: `(1 << i) - 1`.
    - `1 << i` shifts the binary representation of 1 to the left by i positions, creating a number with only the i-th bit set to 1.
    - Subtracting 1 from this number creates a mask with all the bits from the i-th bit to the right set to 1, and all the bits to the left of the i-th bit set to 0.
3. The bitwise AND operation (`&`) is then applied between the given number N and the mask.
    - The AND operation compares the corresponding bits of N and the mask:
        - If both bits are 1, the result is 1.
        - Otherwise, the result is 0.
    - Since all the bits in the mask, except for those from the i-th bit to the right, are set to 0, applying the AND operation clears those bits in N.
4. The updated value of N is returned as the result of the function.

Here are some examples to illustrate the working of the solution:

Example 1:
Input: N = 15, i = 2
Explanation:
- The binary representation of 15 is 1111.
- We need to clear all bits from the MSB to the 2nd bit.
- The mask is generated as follows: (1 << 2) - 1 = 4 - 1 = 3, which is equal to binary representation 011.
- The bitwise AND operation between 15 (1111) and the mask (011) results in 3 (0011).
Output: 3

Example 2:
Input: N = 4, i = 4
Explanation:
- The binary representation of 4 is 100.
- We need to clear all bits from the MSB to the 4th bit (which is the leftmost bit).
- The mask is generated as follows: (1 << 4) - 1 = 16 - 1 = 15, which is equal to binary representation 1111.
- The bitwise AND operation between 4 (100) and the mask (1111) results in 4 (100).
Output: 4

Now, let's move on to suggesting similar problems that can be solved using a similar approach.

Possible similar problems:

1. Given a number N and a position i, count the number of set bits from the i-th bit to the least significant bit. Return the count.
2. Given two numbers N and M, clear all the bits from the most significant bit (MSB) to the i-th bit of M, and replace the corresponding bits in N with the cleared bits. Return the updated N.

Now, let's provide code solutions for the suggested problems.

Code Solution for Problem 1:

```cpp
#include <bits/stdc++.h>
using namespace std;

int countSetBits(int n, int i){
    int mask = (1 << (i + 1)) - 1;
    n = n & mask;
    int count = 0;
    while(n > 0){
        n = n & (n - 1);
        count++;
    }
    return count;
}

int main() {
    int n, i;
    cin >> n >> i;
    cout<<countSetBits(n, i)<<endl;
    return 0;
}
```

Explanation:
1. The function `countSetBits` takes two integer parameters: `n` (the given number) and `i` (the position of the bit to start counting from).
2. Inside the function, a mask is created using bitwise left shift (`<<`) and subtraction (`-`) operations. The mask is generated as follows: `(1 << (i + 1)) - 1`.
    - `(1 << (i + 1))` shifts the binary representation of 1 to the left by (i + 1) positions, creating a number with only the (i + 1)th bit set to 1.
    - Subtracting 1 from this number creates a mask with all the bits from the (i + 1)th bit to the right set to 1, and all the bits to the left of the (i + 1)th bit set to 0.
3. The bitwise AND operation (`&`) is then applied between the given number N and the mask.
    - The AND operation compares the corresponding bits of N and the mask:
        - If both bits are 1, the result is 1.
        - Otherwise, the result is 0.
    - Since all the bits in the mask, except for those from the (i + 1)th bit to the right, are set to 0, applying the AND operation clears those bits in N.
4. A count variable is initialized to 0.
5. A while loop is used to count the number of set bits in the updated value of N.
    - In each iteration, the bitwise AND operation between N and N-1 is applied.
    - This operation clears the least significant set bit in N.
    - The count variable is incremented by 1 for each cleared set bit.
    - The loop continues until N becomes 0 (all set bits are cleared).
6. The final count is returned as the result of the function.

Code Solution for Problem 2:

```cpp
#include <bits/stdc++.h>
using namespace std;

int replaceBits(int n, int m, int i){
    int mask = (1 << (i + 1)) - 1;
    m = m & mask; // clear all bits from the MSB to the (i + 1)th bit of M
    n = n & (~mask); // clear all bits from the (i + 1)th bit to the LSB of N
    return n | m; // replace the bits in N with the cleared bits from M
}

int main() {
    int n, m, i;
    cin >> n >> m >> i;
    cout<<replaceBits(n, m, i)<<endl;
    return 0;
}
```

Explanation:
1. The function `replaceBits` takes three integer parameters: `n` (the given number N), `m` (the given number M), and `i` (the position of the bit to start clearing/replacing from).
2. Inside the function, a mask is created using bitwise left shift (`<<`) and subtraction (`-`) operations. The mask is generated as follows: `(1 << (i + 1)) - 1`.
    - `(1 << (i + 1))` shifts the binary representation of 1 to the left by (i + 1) positions, creating a number with only the (i + 1)th bit set to 1.
    - Subtracting 1 from this number creates a mask with all the bits from the (i + 1)th bit to the right set to 1, and all the bits to the left of the (i + 1)th bit set to 0.
3. The bitwise AND operation (`&`) is then applied between the given number M and the mask.
    - The AND operation compares the corresponding bits of M and the mask:
        - If both bits are 1, the result is 1.
        - Otherwise, the result is 0.
    - Since all the bits in the mask, except for those from the (i + 1)th bit to the right, are set to 0, applying the AND operation clears those bits in M.
4. The bitwise NOT operation (`~`) is applied to the mask, creating a new mask with all bits flipped.
5. The bitwise AND operation between the given number N and the complement of the mask is applied to clear all bits from the (i + 1)th bit to the least significant bit in N.
6. The bitwise OR operation (`|`) is then applied between the cleared bits in N and the cleared bits in M.
    - The OR operation compares the corresponding bits of N and M:
        - If at least one of the bits is 1, the result is 1.
        - Otherwise, the result is 0.
    - This replaces the bits in N with the cleared bits from M.
7. The updated value of N is returned as the result of the function.

Note: The given suggested problems and their solutions are just examples, and there can be many other variations of problems that can be solved using a similar approach.

Now, let's provide the code solution for the given initial problem.

Code Solution for the Initial Problem:

```cpp
#include <bits/stdc++.h>
using namespace std;

int clearAllBits(int n, int i){
    int mask = (1 << i) - 1;
    return n & mask;
}

int main() {
    int n, i;
    cin >> n >> i;
    cout<< clearAllBits(n, i) <<endl;
    return 0;
}
```

Explanation:
1. The function `clearAllBits` is the same as the one mentioned in the initial solution.
2. The user input for the given number N and the position of the bit i is taken.
3. The function `clearAllBits` is called with the given inputs, and the returned value is printed as the output.

Output: Based on the provided code, the output for the initial problem will be displayed on the console.
<hr>
