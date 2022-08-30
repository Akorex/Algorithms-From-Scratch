#ifndef ARRAYLIST_H_INCLUDED
#define ARRAYLIST_H_INCLUDED

#include <iostream>
#include <cassert>
using namespace std;

template <class elemType>
class arrayListType
{
public:
    const arrayListType<elemType>& operator=(const arrayListType<elemType>&);
    bool isEmpty() const;
    //Function to determine whether the list is empty
    //Returns true if list is empty and false otherwise

    bool isFull() const;
    //Function to determine whether the list is full

    int listSize() const;
    //Function to determine the number of elements in the list

    int maxListSize() const;
    //Function to determine the size of the list

    void print() const;
    //Function to print the elements of the list

    bool isItemAtEqual(int location, const elemType& item) const;
    //Function to determine whether the item is the same as the item in the list at the position specified

    void insertAt(int location, const elemType & insertItem);
    //Function to insert an item in the list at the position specified.
    //If the list is full or location is out of range, an appropriate message is displayed

    void insertEnd(const elemType &insertItem);
    //Function to insert an item to the end of a list

    void removeAt(int location);
    //Function to remove the item from the list at the position specified
    // If the location is out of range, an appropriate message is displayed

    void retrieveAt(int location, const elemType &retItem);
    // Function to retrieve the item from the list at the position specified
    //If the location is out of range, an appropriate message is displayed

    void replaceAt(int location, const elemType &repItem);
    // Function to replace the element in the list at the location specified with another item repItem
    // If the location is out of range, an appropriate message is displayed

    void clearList();
    //Function to remove all the elements from the list

    int seqSearch(const elemType &item);
    //Function to search the list for a given item
    // If the item is found, it returns the location in the array where it is found, otherwise returns -1

    void insert(const elemType &insertItem);
    //Function to insert the item specified by the parameter insertItem at the end of the list.
    //However, first the list is searched to see whether the item to be inserted is already
    // in the list

    void remove(const elemType& removeItem);
    //Function to remove an item from the list. The parameter removeItem specifies the item to be removed

    arrayListType(int size=100);
    //constructor - creates an array of the size specified by the parameter size
    // defaults to size 100

    arrayListType(const arrayListType<elemType>& otherList);
    //copy constructor

    ~arrayListType();
    //destructor

protected:
    elemType *list; //array to hold the list of elements
    int length; // to store the length of the list
    int maxSize; // to store the maximum size of the list

};

template <class elemType>
bool arrayListType<elemType>::isEmpty() const{
    return (length == 0);
}

template <class elemType>
bool arrayListType<elemType>::isFull() const{
    return (length == maxSize);
}

template <class elemType>
int arrayListType<elemType>::listSize() const{
    return length;
}

template <class elemType>
int arrayListType<elemType>::maxListSize() const{
    return maxSize;
}

template <class elemType>
void arrayListType<elemType>::print() const{
    for (int i=0; i < length; i++)
        cout << list[i] << " ";

    cout << endl;
}

template <class elemType>
bool arrayListType<elemType>::isItemAtEqual(int location, const elemType& item) const{
    return (list[location] == item);

}

template <class elemType>
void arrayListType<elemType>::insertAt(int location, const elemType & insertItem){
    if (location < 0 || location >= maxSize){
        cerr << "The position of the item to be entered is out of range" << endl;
    }
    else{
        if (length >= maxSize)
            cerr << "Cannot insert into a full list";
        else{
            for (int i = length; i > location; i--)
                list[i] = list[i-1]; //shift elements to the right
            list[location] = insertItem;
            length++;
        }
    }
}

template <class elemType>
void arrayListType<elemType>::insertEnd(const elemType &insertItem){
    if (length >= maxSize){
        cerr << "Cannot insert into a full list";
    }
    else{
        list[length] = insertItem;
        length++;
    }
}

template <class elemType>
void arrayListType<elemType>::removeAt(int location){
    if (location < 0 || location >= length)
        cerr << "The location to be removed is out of range";
    else{
        for (int i = location; i < length -1 ; i++)
            list[i] = list[i + 1]; // shift elements to the left
        length --;
    }
}

template <class elemType>
void arrayListType<elemType>::retrieveAt(int location, const elemType &retItem){
    if (location < 0 || location >= length)
        cerr << "The location to be retrieved is out of range";
    else{
        retItem = list[location];
        return retItem;
    }
}

template <class elemType>
void arrayListType<elemType>::replaceAt(int location, const elemType &repItem){
    if (location < 0 || location >= length)
        cerr << "The location to be replaced is out of range";
    else{
        list[location] = repItem;
    }
}

template <class elemType>
void arrayListType<elemType>::clearList(){
    length = 0;
}

template <class elemType>
arrayListType<elemType>::arrayListType(int size){
    if (size < 0){
        cerr << "The array size must be positive. Creating an array of size 100." << endl;
        maxSize = 100;
    }
    else
        maxSize = size;
    length = 0;
    list = new elemType[maxSize]; // create the list
    assert(list != NULL);
}

template <class elemType>
arrayListType<elemType>::~arrayListType(){
    delete [] list;
}

template <class elemType>
arrayListType<elemType>::arrayListType(const arrayListType<elemType>& otherList){
    maxSize = otherList.maxListSize;
    length = otherList.length;
    list = new elemType [maxSize];
    assert(list != NULL);

    for (int j = 0; j < length; j++){
        list[j] = otherList.list[j];
    }
}

template <class elemType>
const arrayListType<elemType>&arrayListType<elemType>::operator=(const arrayListType<elemType>& otherList){
    if (this != &otherList){
        delete [] list;
        maxSize = otherList.maxSize;
        length = otherList.length;

        list = new elemType[maxSize];
        assert(list != NULL);

        for (int i =0; i < length; i++)
            list[i] = otherList.list[i];
    }
    return *this;
}

template <class elemType>
int arrayListType<elemType>::seqSearch(const elemType &item){
    int loc;
    bool found = false;

    for (loc = 0; loc < length; loc++)
        if (list[loc] == item){
            found = true;
            break;
        }
    if (found)
        return loc;
    else
        return -1;
}

template <class elemType>
void arrayListType<elemType>::insert(const elemType &insertItem){
    int loc;

    if (length == 0)
        list[length++] = insertItem;
    else if (length == maxSize)
        cerr << "Cannot insert in a full list" << endl;
    else{
        loc = seqSearch(insertItem);
        if (loc == -1) // element not found
            list[length++] = insertItem;
        else
            cerr << "The item to be inserted is already in the list" << endl;

    }
}

template <class elemType>
void arrayListType<elemType>::remove(const elemType &insertItem){
    int loc;

    if (length == 0)
        cerr << "Cannot delete from an empty list" << endl;

    else{
        loc = seqSearch(insertItem);

        if (loc != -1)
            removeAt(loc);

        else
            cerr << "The item to be deleted is not in the list" << endl;
    }
}


#endif // ARRAYLIST_H_INCLUDED
