#include <iostream>
#include "virtual_functions.h"
using namespace std;



void callPrint(baseClass *p);

int main()
{
    baseClass *q;
    baseClass *r;

    q = new baseClass(5);
    r = new derivedClass(3, 15);

    q->print();
    // the above is the same as:
    (*q).print();

    r->print();
    cout << "\n";
    cout << "Using callPrint() function";
    cout << "\n";

    callPrint(q);
    callPrint(r);
    //callPrint(r);
    return 0;
}

void callPrint(baseClass *p)
{
    p->print();
}
