#include <iostream>
#include <random>
using namespace std;

random_device rd;
mt19937 gen(rd());
uniform_real_distribution<> dist(0, 1);

int main() {
    int sample_size;
    cout<< "Please input sample size: "<<endl;
    cin >> sample_size;
    int no_in_circle = 0;
    for(auto test=0; test<sample_size; test++){
        float x = dist(gen);
        float y = dist(gen);
        float distance = pow(x, 2) + pow(y, 2);
        if( distance < 1) no_in_circle++;
    }
    float pi = float(no_in_circle) / float(sample_size) * 4;
    cout << "Pi is: "<<pi<<endl;
}