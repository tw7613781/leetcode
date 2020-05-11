#include <iostream>
#include <random>
#include <chrono>
using namespace std;
using namespace std::chrono;

mt19937 gen{random_device{}()};
uniform_int_distribution<int> dist{1,4};

int random_walk(const int& n){
    int x = 0;
    int y = 0;
    for (auto i = 0; i<n; i++){
        int direction = dist(gen);
        switch (direction)
        {
            case 1:
                x += 1;
                break;
            case 2:
                x -= 1;
                break;
            case 3:
                y += 1;
                break;
            case 4:
                y -= 1;
                break;
        }
    }
    int distance = abs(x) + abs(y);
    return distance; 
}

int main() {
    int steps = 30;
    int sample_size = 100000;
    for(auto step=1; step<steps; step++){
        auto start = high_resolution_clock::now();
        int no_of_stransport = 0;
        for(auto test=0; test<sample_size; test++){
            int distance = random_walk(step);
            if(distance <= 4)
                no_of_stransport += 1;
        }
        float percentage = float(no_of_stransport)/float(sample_size) * 100;
        cout<<"walk_lenth is "<<step<<", the rate of no_transportation is "<<percentage<<endl;
        auto stop = high_resolution_clock::now();
        auto duration = duration_cast<milliseconds>(stop - start).count();
        cout<<"time consume: "<<duration<<" ms"<<endl;
    }
}