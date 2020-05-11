#include <vector>

using namespace std;

class BIgArray {
    vector<int> v;
    mutable int accessCounter;

public:
    int getItem(int index) const {
        accessCounter++;
        return v[index];
    }
};

int main(){
    BIgArray b;
    return 0;
}