#ifndef VIRTUAL_FUNCTIONS_H_INCLUDED
#define VIRTUAL_FUNCTIONS_H_INCLUDED

#include <iostream>
using namespace std;

class baseClass
{
public:
    virtual void print(); //a virtual function
    baseClass(int u = 0);
private:
    int x;
};
class derivedClass: public baseClass
{
public:
    void print();
    derivedClass(int u = 0, int v = 0);
private:
    int a;
};

void baseClass::print()
{
    cout << "In the base class, x = " << x << endl;
}

baseClass::baseClass(int u)
{
    x = u;
}

void derivedClass::print()
{
    cout << "***In the derived class***" << endl;
    baseClass::print();
    cout << "and in the derived class, a = " << a << endl;
}

derivedClass::derivedClass(int u, int v):baseClass(u)
{
    a = v;
}

void callPrint(baseClass& p)
{
    p.print();
}





#endif // VIRTUAL_FUNCTIONS_H_INCLUDED
