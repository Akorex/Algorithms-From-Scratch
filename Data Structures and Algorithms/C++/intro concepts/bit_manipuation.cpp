#include <iostream>
using namespace std;

int repeatedArithmeticShift(int x, int count)
{
    for (int i = 0; i < count; i++)
    {
        x >>= 1;
    }
    return x;
}

bool getBit(int num, int i)
{
    return ((num & (1 << i)) != 0);
}

int main()
{
    int arith = repeatedArithmeticShift(-402, 1);
    cout << arith << endl;

    int ans = getBit(1011, 2);
    cout << ans;
    return 0;
}
