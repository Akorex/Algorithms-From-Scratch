#include <iostream>
using namespace std;
// demonstrates how a pointer works

int main()
{
    int *p;
    int num1 = 5;
    int num2 = 8;

    p = &num1; //store the address of num1 into p

    cout << "&num1: " << &num1 << " p: "<< p << endl;
    cout << "num1: " << num1 << " num2: " << num2<<endl;

    *p = 15;
    cout << "num1: " << num1 << " num2: " << num2<<endl;
    cout << "&num1: " << &num1 << " p: "<< p << endl;

    int *x;
    x = new int;

    *x = 34;
    cout << *x;

    return 0;
}
