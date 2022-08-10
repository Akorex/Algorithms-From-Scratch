#include <iostream>
#include <string>
#include "persontype.h"
using namespace std;

class partTimeEmployee: public PersonType
{
public:
    void print() const;
    //Function to output the first name, last name and wages of the employee

    double calculatePay() const;
    //Function to calculate and return the wages

    void setNameRateHours(string first, string last, double rate, double hours);
    //Function to set first name, last name, payRate and hoursWorked according to parameters

    partTimeEmployee(string first ="", string last = "", double rate= 0, double hours=0);
    //constructors with parameters
    //sets the first name, last name, pay rate & hours worked according to parameters
    //If no value is passed, default values are used

private:
    double payRate;
    double hoursWorked;

};

void partTimeEmployee::print() const
{
    PersonType::print();
    cout << "Their wages is :" << calculatePay() << endl;
}

double partTimeEmployee::calculatePay() const
{
    return payRate * hoursWorked;
}

void partTimeEmployee::setNameRateHours(string first, string last, double rate, double hours)
{
    PersonType::setName(first, last);
    payRate = rate;
    hoursWorked = hours;
}

partTimeEmployee::partTimeEmployee(string first, string last, double rate, double hours):PersonType(first, last)
{
    payRate = rate;
    hoursWorked = hours;
}


int main()
{
    PersonType person;
    person = PersonType("Akorede", "Adewole");
    person.print();

    //partTimeEmoloyee
    partTimeEmployee employee;
    employee = partTimeEmployee("Akorede", "Adewole", 5000, 7);
    employee.print();
    cout << employee.calculatePay();

    return 0;
}
