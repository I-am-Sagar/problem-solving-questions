### Binary_String_Queries - Solutions
<hr>

### C++ Code with improved structure, meaningful variable names, and comments:

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long int

// Function to calculate modular exponentiation
ll modExp(ll a, ll m, ll n){
    ll ans = 1;
    while (m > 0) {
        if (m % 2 == 1) {
            ans = (ans * a) % n;
            m--;
        }
        a = (a * a) % n;
        m /= 2;
    }
    return ans;
}

// Function to calculate height of the segment tree
ll getHeight(ll n){
    ll x = ceil(log2(n));
    return 2 * (ll)pow(2, x) - 1;
}

// Function to build the segment tree
void build(ll ar[], ll tree[], ll start, ll end, ll node){
    if(start == end){
        tree[node] = ar[start];
        return ;
    }
    ll mid = (start + end) / 2;
    build(ar, tree, start, mid, node * 2 + 1);
    build(ar, tree, mid + 1, end, node * 2 + 2);
    tree[node] = (tree[node * 2 + 2] + ((modExp(2, end - mid, 3) * tree[node * 2 + 1]) % 3)) % 3;
}

// Function to update the segment tree
void update(ll ar[], ll tree[], ll start, ll end, ll idx, ll node){
    if(start == end){
        ar[idx] = 1;
        tree[node] = 1;
        return ;
    }
    ll mid = (start + end) / 2;
    if(idx >= start && idx <= mid){
        update(ar, tree, start, mid, idx, node * 2 + 1);
    }
    else{
        update(ar, tree, mid + 1, end, idx, node * 2 + 2);
    }
    tree[node] = (tree[node * 2 + 2] + ((modExp(2, end - mid, 3) * tree[node * 2 + 1]) % 3)) % 3;
}

// Function to perform the query on the segment tree
ll query(ll ar[], ll tree[], ll start, ll end, ll l, ll r, ll node){
    if(start > end || start > r || end < l)
        return 0;
    if(start >= l && end <= r) return (tree[node] * modExp(2, r - end, 3)) % 3;

    ll mid = (start + end) / 2;
    ll p1 = query(ar, tree, start, mid, l, r, node * 2 + 1);
    ll p2 = query(ar, tree, mid + 1, end, l, r, node * 2 + 2);

    return (p1 + p2) % 3;
}

int main(){

    ll n;
    cin >> n;
    
    ll ar[n];

    ll size = getHeight(n);
    ll tree[size];

    // Reading binary string input and converting it to an array
    for(int i = 0; i < n; i++){
        char ch;
        cin >> ch;
        ar[i] = ch - '0';
    }

    // Building the segment tree
    build(ar, tree, 0, n - 1, 0);

    int q;
    cin >> q;
    for(int i = 0; i < q; i++){
        int ch;
        cin >> ch;
        if(ch == 0){
            int l, r;
            cin >> l >> r;
            // Performing query of Type 0
            cout << query(ar, tree, 0, n - 1, l, r, 0) << endl;
        }
        else{
            int x;
            cin >> x;
            if(ar[x] == 0){
                // Performing query of Type 1
                update(ar, tree, 0, n - 1, x, 0);
            }
        }
    }

    return 0;
}
```

### Java Equivalent Code:

```java
import java.util.*;

class Main {

    static long modExp(long a, long m, long n) {
        long ans = 1;
        while (m > 0) {
            if (m % 2 == 1) {
                ans = (ans * a) % n;
                m--;
            }
            a = (a * a) % n;
            m /= 2;
        }
        return ans;
    }

    static long getHeight(long n) {
        long x = (long)Math.ceil(Math.log(n) / Math.log(2));
        return 2 * (long)Math.pow(2, x) - 1;
    }

    static void build(int[] ar, int[] tree, int start, int end, int node) {
        if (start == end) {
            tree[node] = ar[start];
            return;
        }
        int mid = (start + end) / 2;
        build(ar, tree, start, mid, node * 2 + 1);
        build(ar, tree, mid + 1, end, node * 2 + 2);
        tree[node] = (tree[node * 2 + 2] + ((modExp(2, end - mid, 3) * tree[node * 2 + 1]) % 3)) % 3;
    }

    static void update(int[] ar, int[] tree, int start, int end, int idx, int node) {
        if (start == end) {
            ar[idx] = 1;
            tree[node] = 1;
            return;
        }
        int mid = (start + end) / 2;
        if (idx >= start && idx <= mid) {
            update(ar, tree, start, mid, idx, node * 2 + 1);
        }
        else {
            update(ar, tree, mid + 1, end, idx, node * 2 + 2);
        }
        tree[node] = (tree[node * 2 + 2] + ((modExp(2, end - mid, 3) * tree[node * 2 + 1]) % 3)) % 3;
    }

    static int query(int[] ar, int[] tree, int start, int end, int l, int r, int node) {
        if (start > end || start > r || end < l)
            return 0;
        if (start >= l && end <= r) return (tree[node] * (int)modExp(2, r - end, 3)) % 3;

        int mid = (start + end) / 2;
        int p1 = query(ar, tree, start, mid, l, r, node * 2 + 1);
        int p2 = query(ar, tree, mid + 1, end, l, r, node * 2 + 2);

        return (p1 + p2) % 3;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();

        int[] ar = new int[n];

        long size = getHeight(n);
        int[] tree = new int[(int)size];

        // Reading binary string input and converting it to an array
        String str = scanner.next();
        for (int i = 0; i < n; i++) {
            ar[i] = Integer.parseInt(String.valueOf(str.charAt(i)));
        }

        // Building the segment tree
        build(ar, tree, 0, n - 1, 0);

        int q = scanner.nextInt();
        for (int i = 0; i < q; i++) {
            int ch = scanner.nextInt();
            if (ch == 0) {
                int l = scanner.nextInt();
                int r = scanner.nextInt();
                // Performing query of Type 0
                System.out.println(query(ar, tree, 0, n - 1, l, r, 0));
            }
            else {
                int x = scanner.nextInt();
                if (ar[x] == 0) {
                    // Performing query of Type 1
                    update(ar, tree, 0, n - 1, x, 0);
                }
            }
        }

        scanner.close();
    }
}
```

### Python Equivalent Code:

```python
import math

def mod_exp(a, m, n):
    ans = 1
    while m > 0:
        if m % 2 == 1:
            ans = (ans * a) % n
            m -= 1
        a = (a * a) % n
        m //= 2
    return ans

def get_height(n):
    x = math.ceil(math.log(n, 2))
    return 2 * int(math.pow(2, x)) - 1

def build(ar, tree, start, end, node):
    if start == end:
        tree[node] = ar[start]
        return
    mid = (start + end) // 2
    build(ar, tree, start, mid, node * 2 + 1)
    build(ar, tree, mid + 1, end, node * 2 + 2)
    tree[node] = (tree[node * 2 + 2] + ((mod_exp(2, end - mid, 3) * tree[node * 2 + 1]) % 3)) % 3

def update(ar, tree, start, end, idx, node):
    if start == end:
        ar[idx] = 1
        tree[node] = 1
        return
    mid = (start + end) // 2
    if idx >= start and idx <= mid:
        update(ar, tree, start, mid, idx, node * 2 + 1)
    else:
        update(ar, tree, mid + 1, end, idx, node * 2 + 2)
    tree[node] = (tree[node * 2 + 2] + ((mod_exp(2, end - mid, 3) * tree[node * 2 + 1]) % 3)) % 3

def query(ar, tree, start, end, l, r, node):
    if start > end or start > r or end < l:
        return 0
    if start >= l and end <= r:
        return (tree[node] * mod_exp(2, r - end, 3)) % 3

    mid = (start + end) // 2
    p1 = query(ar, tree, start, mid, l, r, node * 2 + 1)
    p2 = query(ar, tree, mid + 1, end, l, r, node * 2 + 2)

    return (p1 + p2) % 3

n = int(input())
ar = list(map(int, input()))
size = get_height(n)
tree = [0] * size

# Building the segment tree
build(ar, tree, 0, n - 1, 0)

q = int(input())
for i in range(q):
    ch = int(input())
    if ch == 0:
        l, r = map(int, input().split())
        # Performing query of Type 0
        print(query(ar, tree, 0, n - 1, l, r, 0))
    else:
        x = int(input())
        if ar[x] == 0:
            # Performing query of Type 1
            update(ar, tree, 0, n - 1, x, 0)
```

### JavaScript (Node.js) Equivalent Code:

```javascript
function modExp(a, m, n) {
    let ans = 1;
    while (m > 0) {
        if (m % 2 === 1) {
            ans = (ans * a) % n;
            m--;
        }
        a = (a * a) % n;
        m /= 2;
    }
    return ans;
}

function getHeight(n) {
    const x = Math.ceil(Math.log2(n));
    return 2 * (2 ** x) - 1;
}

function build(ar, tree, start, end, node) {
    if (start === end) {
        tree[node] = ar[start];
        return;
    }
    const mid = Math.floor((start + end) / 2);
    build(ar, tree, start, mid, node * 2 + 1);
    build(ar, tree, mid + 1, end, node * 2 + 2);
    tree[node] = (tree[node *
<hr>
