#include <iostream>
#include "arraylist.h"
using namespace std;


int main()
{
    arrayListType<int> intList(100);
    arrayListType<string> stringList;

    int number;
    cout << "Enter 5 numbers: ";

    for (int counter = 0; counter < 5; counter++){
        cin >> number;
        intList.insertAt(counter, number);
    }
    cout << endl;

    cout << "The list you entered is: ";
    intList.print();
    cout << endl;

    cout << "Enter the number you want removed:";
    cin >> number;
    intList.remove(number);
    cout << "After deleting " << number << " the list is: ";
    intList.print();
    cout << endl;

    cout << "The number of numbers in the list is " << intList.listSize() << endl;
    return 0;
}
