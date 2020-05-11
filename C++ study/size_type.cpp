#include <vector>
#include <string>
#include <iostream>
using namespace std;

int main(){
    cout<<"Size of size_type in vector: "<<sizeof(vector<int>::size_type)<<endl;
    cout<<"Size of size_type in string: "<<sizeof(string::size_type)<<endl;
    cout<<"Size of size_z: "<<sizeof(size_t)<<endl;
    return 0;
}