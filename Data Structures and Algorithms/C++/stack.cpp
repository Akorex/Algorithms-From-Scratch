#include <iostream>
using namespace std;

//template <class elemType>
class ArrayStack
{
public:
    bool isEmpty() const;
    //Returns true if stack is empty, false otherwise

    int stackSize() const;
    //Returns the number of elements in the stack

    void pop();
    //Function to remove the element at the top of the stack
    //Also displays the removed element. Prints error if the stack is empty

    void top();
    //Function to display the element at the top of the stack
    //Prints error if the stack is empty

    void push();
    //Function to add an element to the top of the stack

    ArrayStack();
    //Default constructor

    ~ArrayStack();
    //Destructor
protected:
    int length; // number of elements in the stack
    int size = 20;
    int data[20];
};

bool ArrayStack::isEmpty() const{
    return (length == 0);
}

int ArrayStack::stackSize() const{
    return length;
}

void ArrayStack::pop()
{
    int entry;
    entry = data.pop();
    cout << entry;
}


int main()
{
    return 0;
}
