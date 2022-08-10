#include <iostream>
using namespace std;


int main()
{
    int *p;
    int *q;

    p = new int;
    *p = 34;
    cout << "p = " << p << " *p = " << *p << endl;

    q = p;
    cout << "q = " << q << " *q = " << *q << endl;

    *q = 45;
    cout << "p = " << p << " *p = " << *p << " q = " << q << " *q = " << *q << endl;

    p = new int;
    *p = 18;
    cout << "p = " << p << " *p = " << *p << " q = " << q << " *q = " << *q << endl;

    delete q;
    q = NULL;
    q = new int;
    *q = 64;
    cout << "p = " << p << " *p = " << *p << " q = " << q << " *q = " << *q << endl;
    return 0;
}
