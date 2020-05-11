#include <iostream>

using namespace std;

class Dog {
    int age;
    string name;
public:
    Dog() { age = 3; name = "dummy";}
    void setAge(const int& a) {age = a;}
    const string& getName() {return name;}

    void printDogName() const {
        cout << "const" << endl;
    }
};

int main() {
    Dog d;

    int i = 9;
    d.setAge(i);
    cout << i << endl;
    d.printDogName();

    cout << d.getName() << endl;

    return 0;
}