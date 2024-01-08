### clear_bits - Solutions
<hr>

#### C++ code with meaningful variable names and comments:

```cpp
#include <iostream>
using namespace std;

// Function to clear all bits from MSB to ith bit (start i from right to left)
int clearAllBits(int num, int bit_pos){
    // Create a mask by shifting 1 to the left by the bit position 'bit_pos', then subtract 1 to set all bits from MSB to bit_pos to 1
    int mask = (1 << bit_pos) - 1;
    
    // Apply the mask to the number using bitwise AND operation to clear all bits from MSB to ith bit
    int updated_num = num & mask;
    
    // Return the updated number
    return updated_num;
}

int main() {
    int n, i;
    
    // Read the number 'n' and the bit position 'i' from the input
    cin >> n >> i;
    
    // Call the function clearAllBits with the given number and bit position
    int updated_number = clearAllBits(n, i);
    
    // Print the updated number
    cout << updated_number << endl;
    
    return 0;
}
```

#### Java code:
```java
import java.util.Scanner;

public class ClearBits {
    
    // Function to clear all bits from MSB to ith bit (start i from right to left)
    public static int clearAllBits(int num, int bitPos){
        // Create a mask by shifting 1 to the left by the bit position 'bitPos', then subtract 1 to set all bits from MSB to bitPos to 1
        int mask = (1 << bitPos) - 1;
        
        // Apply the mask to the number using bitwise AND operation to clear all bits from MSB to ith bit
        int updatedNum = num & mask;
        
        // Return the updated number
        return updatedNum;
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // Read the number 'n' and the bit position 'i' from the input
        int n = scanner.nextInt();
        int i = scanner.nextInt();
        
        // Call the function clearAllBits with the given number and bit position
        int updatedNumber = clearAllBits(n, i);
        
        // Print the updated number
        System.out.println(updatedNumber);
        
        scanner.close();
    }
}
```

#### Python code:
```python
# Function to clear all bits from MSB to ith bit (start i from right to left)
def clear_all_bits(num, bit_pos):
    # Create a mask by shifting 1 to the left by the bit position 'bit_pos', then subtract 1 to set all bits from MSB to bit_pos to 1
    mask = (1 << bit_pos) - 1
    
    # Apply the mask to the number using bitwise AND operation to clear all bits from MSB to ith bit
    updated_num = num & mask
    
    # Return the updated number
    return updated_num

# Read the number 'n' and the bit position 'i' from the input
n, i = map(int, input().split())

# Call the function clear_all_bits with the given number and bit position
updated_number = clear_all_bits(n, i)

# Print the updated number
print(updated_number)
```

#### JavaScript (Node.js) code:
```javascript
// Function to clear all bits from MSB to ith bit (start i from right to left)
function clearAllBits(num, bitPos) {
    // Create a mask by shifting 1 to the left by the bit position 'bitPos', then subtract 1 to set all bits from MSB to bitPos to 1
    let mask = (1 << bitPos) - 1;
    
    // Apply the mask to the number using bitwise AND operation to clear all bits from MSB to ith bit
    let updatedNum = num & mask;
    
    // Return the updated number
    return updatedNum;
}

// Read the number 'n' and the bit position 'i' from the input
const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

rl.question('Enter the number and bit position (separated by space): ', (input) => {
    // Split the input string to extract the number and bit position
    let [n, i] = input.split(' ').map(Number);
    
    // Call the function clearAllBits with the given number and bit position
    let updatedNumber = clearAllBits(n, i);
    
    // Print the updated number
    console.log(updatedNumber);
    
    rl.close();
});
```

#### Explanation of the code and approach:

This code is a solution to a problem of clearing all bits from the Most Significant Bit (MSB) to the ith bit. The bit positions are counted starting from 0 from right to left.

The main logic of the solution lies in using bitwise operations, specifically bitwise shift and bitwise AND.

The function `clearAllBits` takes two parameters: `num` (the number) and `bitPos` (the bit position till where the bits should be cleared). It uses these parameters to create a mask that has all bits set from the least significant bit (LSB) up to `bitPos`, and all other bits set to 0. This is done by shifting the number 1 (binary `01`) to the left by `bitPos` positions, creating a number with a 1 bit at `bitPos` position, and subtracting 1 to set all bits up to `bitPos` to 1.

Then, the function applies this mask to the input number `num` using bitwise AND operation. This clears all bits in `num` from MSB to `bitPos`, while preserving the rest of the bits. The result is stored in the variable `updatedNum`, which is then returned.

In the `main` function, the program prompts the user to input the number `n` and the bit position `i`. The function `clearAllBits` is then called with these inputs, and the result is printed to the console.

The code uses standard input/output for C++, Java, and Python. For JavaScript (Node.js), it uses the `readline` module to read input from the console.
<hr>
