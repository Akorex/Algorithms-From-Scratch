#include <iostream>
#include <string>
#include <vector>
using namespace std;

// Implement an algorithm to determine if a string has all unique
//characters. What if you cannot use additional data structures?

bool isUniqueChars(string str){
    if (str.length() > 128)
        return false;

    vector<bool> char_set(128);
    for (int i = 0; i < str.length(); i++){
        int val = str[i];
        if (char_set[val]){ //Already found this char in the string
            return false;
        }
        char_set[val] = true;
    }
    return true;
}


int main(){

    return 0;
}
