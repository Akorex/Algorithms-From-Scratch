#ifndef PERSONTYPE_H_INCLUDED
#define PERSONTYPE_H_INCLUDED

#include <iostream>
#include <string>
using namespace std;
class PersonType{
public:
    void print() const;
    //Function to print the first name and the last name

    void setName(string first, string last);
    //Function to set the name

    string getFirstName() const;
    //Function to return the first name

    string getLastName() const;
    //Function to return the last name

    PersonType();
    //Default constructor

    PersonType(string first, string last);
    //constructor with parameter

private:
    string firstName, lastName;
};

void PersonType::setName(string first, string last)
{
    firstName = first;
    lastName = last;
}

string PersonType::getFirstName() const
{
    return firstName;
}

string PersonType::getLastName() const
{
    return lastName;
}

void PersonType::print() const
{
    cout << "Name is: " << firstName << " " << lastName << endl;
}

PersonType::PersonType()
{
    firstName = "";
    lastName = "";
}

PersonType::PersonType(string first, string last)
{
    setName(first, last);
}

#endif // PERSONTYPE_H_INCLUDED
