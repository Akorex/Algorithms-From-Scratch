#include <iostream>
#include <algorithm>
#include <deque>
#include <iterator>
using namespace std;

int main()
{
    deque<int> intDeq;
    ostream_iterator<int> screen(cout, " ");

    intDeq.push_back(13);
    intDeq.push_back(75);
    intDeq.push_back(28);
    intDeq.push_back(35);

    cout << "The Deque: ";
    copy(intDeq.begin(), intDeq.end(), screen);
    cout << endl;

    intDeq.push_front(0);
    intDeq.push_back(100);

    cout << "After adding two more elements - one at the back & one at the front: ";
    copy(intDeq.begin(), intDeq.end(), screen);
    cout << endl;

    intDeq.pop_back();
    intDeq.pop_back();
    cout << "The Deque after popping: ";
    copy(intDeq.begin(), intDeq.end(), screen);
    cout << endl;
    return 0;
}
