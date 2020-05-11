#include <iostream>

using namespace std;

int main(){
    int* null_point; // allow null point
    // int& null_refrence; // don't allow null reference
    int number = 3;
    null_point = &number;
    cout<<"number address: "<<null_point<<endl;
    cout<<"number value: "<<*null_point<<endl;

    int value = 5;
    int& ref = value;

    ref = 6;      // ref is a reference of value "5", change the value to "6" 
    //&ref = 6;   // reference cannot be reassigned 

    return 0;
}