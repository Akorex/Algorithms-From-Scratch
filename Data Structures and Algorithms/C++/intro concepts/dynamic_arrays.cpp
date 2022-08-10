#include <iostream>
using namespace std;

void get(double *&a, int &n){
cout << "Enter a number of items: ";
cin >> n;
a = new double [n];
cout << "Enter " << n << " items, one per line: \n";
for (int i=0; i < n; i++){
    cout << "\t" << i + 1 <<":";
    cin >> a[i];
}
}

void print(double *a, int n){
    for (int i=0; i < n; i++){
        cout << a[i] << " ";
        cout << endl;
    }
}

int main(){
    double *a;
    int n;
    get(a, n);
    print(a, n);
    delete [] a;
    get(a, n);
    print(a, n);
return 0;
}
