#include <iostream>
#include <cmath>
#include <string>
#include <cstdlib>
using namespace std;

class clockType{
public:
    void setTime(int hours, int minutes, int seconds);
    //Function to set the time
    //The time is set according to the parameters
    //The function checks whether the values given to hours, minutes and seconds are valid
    // If a value is invalid, a default value of 0 is assigned

    void getTime(int &hours, int &minutes, int &seconds) const;
    //Function to return the time

    void printTime() const;
    //Function to print the time
    // Time is printed in the hr::mm::ss format

    void incrementSeconds();
    //Function to increment the time by one second
    //If the time before increment was 23:59:59, the time is reset to 00:00:00

    void incrementMinutes();
    //Function to increment the time by one minute
    // If the time before increment was 23:59:00, the time is reset to 00:00:00

    void incrementHours();
    //Function to increment the time by one hour
    //If the time before increment was 23:00:00, the time is reset to 00:00:00

    bool equalTime(const clockType& otherClock) const;
    //Function to compare the two times
    //Returns true if this time is equal to otherClock, otherwise, return False

    clockType(int hours, int minutes, int seconds);
    //constructor with the parameters
    // Values are set according to the given parameters

    clockType();
    //Default Constructor with parameters
    //the time is set to 00:00:00

private:
    int hr; //stores the hour
    int min; //stores the minute
    int sec; //stores the second
};

void clockType::setTime(int hours, int minutes, int seconds)
{
    if (0 <= hours && hours < 24)
        hr = hours;
    else
        hr = 0;
    if (0 <= minutes && minutes < 60)
        min = minutes;
    else
        min = 0;
    if (0 <= seconds && seconds < 60)
        sec = seconds;
    else
        sec = 0;
}

void clockType::getTime(int& hours, int& minutes, int& seconds) const
{
    hours = hr;
    minutes = min;
    seconds = sec;
}

void clockType::printTime() const
{
    if (hr < 10)
        cout << "0";
    cout << hr <<":";

    if (min < 10)
        cout << "0";
    cout << min << ":";

    if (sec < 10)
        cout << "0";
    cout << sec;

    cout <<"\n";
}

void clockType::incrementHours()
{
    hr++;
    if (hr >23)
        hr = 0;
}

void clockType::incrementMinutes()
{
    min++;
    if (min > 59){
        min = 0;
        incrementHours();
    }
}

void clockType::incrementSeconds()
{
    sec++;
    if (sec > 59){
        sec = 0;
        incrementMinutes();
    }
}

bool clockType::equalTime(const clockType& otherClock) const
{
    return (hr == otherClock.hr && min == otherClock.min && sec == otherClock.sec);
}

clockType::clockType() //default constructor
{
    hr = 0;
    min = 0;
    sec = 0;
}

clockType::clockType(int hours, int minutes, int seconds) //other constructor
{
    setTime(hours, minutes, seconds);
}
int main(){

    clockType myClock;
    myClock.setTime(2, 56, 23);
    myClock.printTime();

    myClock.incrementHours();
    myClock.printTime();

    clockType herClock;
    herClock.setTime(3, 56, 23);
    herClock.printTime();

    int x = myClock.equalTime(herClock);
    cout << x << endl;

    clockType anotherClock(5, 59, 59);
    anotherClock.printTime();
    anotherClock.incrementSeconds();
    anotherClock.printTime();

    return 0;
}
