#include <iostream>
using namespace std;

//class RectangleType
//Class to represent the properties of a rectangle

class RectangleType
{
public:
    void setDimension(double l, double w);
    //Function to set the length and width of the rectangle

    double getLength() const;
    //Function to return the length of the rectangle

    double getWidth() const;
    //Function to return the width of the rectangle

    double area() const;
    //Function to return the area of the rectangle

    double perimeter() const;
    //Function to return the perimeter of the rectangle

    void print() const;
    //Function to print the length and width of the rectangle

    RectangleType();
    //Default constructor

    RectangleType(double l, double w);
    //Constructor with parameters

private:
    double length;
    double width;
};


void RectangleType::setDimension(double l, double w)
{
    if (l >= 0)
        length = l;
    else
        length = 0;

    if (w >= 0)
        width = w;
    else
        width = 0;
}

double RectangleType::getLength() const
{
    return length;
}

double RectangleType::getWidth() const
{
    return width;
}

double RectangleType::area() const
{
    return length * width;
}

double RectangleType::perimeter() const
{
    return 2 * (length + width);
}

void RectangleType::print() const
{
    cout << "Length: " << length << "\tWidth: " << width << endl;
}

RectangleType::RectangleType()
{
    length = 0;
    width = 0;
}

RectangleType::RectangleType(double l, double w)
{
    setDimension(l, w);
}

class boxType: public RectangleType
{
public:
    void setDimension(double l, double w, double h);
    //Function to set the dimension of the box

    double getHeight() const;
    //Function to return the height of the box

    double area() const;
    //Function to return the surface area of the box

    double volume() const;
    //Function to return the volume of the box

    void print() const;
    //Function to output the length, breadth, and height of the box

    boxType();
    //Default constructor
    //sets length = 0, height = 0, breadth = 0

    boxType(double l, double w, double h);
    //constructor with the parameters
private:
    double height;
};

void boxType::setDimension(double l, double w, double h)
{
    RectangleType::setDimension(l, w);
    if (h >= 0)
        height = h;
    else
        height = 0;
}


void boxType::print() const
{
    RectangleType::print();
    cout << "; Height = " << height;
}

double boxType::getHeight() const
{
    return height;
}

double boxType::area() const
{
    return 2*(getLength() * getWidth() + getLength() * height + getWidth() * height);
}

double boxType::volume() const
{
    return RectangleType::area() * height;
}

boxType::boxType()
{
    height = 0.0;
}

boxType::boxType(double l, double w, double h):RectangleType(l, w)
{
    if (h >= 0)
        height = h;
    else
        height = 0;
}


int main()
{
    //rectangle
    RectangleType r1;
    double area;
    r1 = RectangleType(4, 5);
    r1.print();

    area = r1.area();
    cout << area << endl;

    //box with default constructor
    boxType b1;
    b1 = boxType();
    b1.print();
    cout << endl;

    //box with given parameters
    boxType b2;
    double volume;
    b2 = boxType(3, 4, 5);
    b2.print();
    cout << endl;

    area = b2.area();
    volume = b2.volume();

    cout << "area: " << area << endl;
    cout << "volume: " << volume << endl;
    return 0;
}
