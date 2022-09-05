#include <iostream>
#include <vector>
using namespace std;


int main()
{
    vector<int> intList;

    intList.push_back(13);
    intList.push_back(75);
    intList.push_back(20);
    intList.push_back(40);

    cout << "List elements: ";
    for (int i=0; i < 4; i++)
        cout << intList[i] << " ";
    cout << endl;

    vector<int>::iterator listIt;
    cout << "List elements: ";
    for (listIt = intList.begin(); listIt != intList.end(); ++listIt)
        cout << *listIt << " ";
    cout << endl;

    listIt = intList.begin();
    ++listIt;
    ++listIt;
    intList.insert(listIt, 88);
    cout << "List elements: ";
    for (listIt = intList.begin(); listIt != intList.end(); ++listIt)
        cout << *listIt << " ";
    cout << endl;
    return 0;
}
