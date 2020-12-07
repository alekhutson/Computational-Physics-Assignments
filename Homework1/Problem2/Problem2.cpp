#include <iostream>
#include <vector>
#include <string>
#include<cmath>
#include <fstream>


using namespace std;

int main(){

    int x=1; //initializes x

    for(int i=0;i<1000;i++){ // iteratively multiplies by two

        int m=x;

        x=x*2;

        if(m != x/2){
             cout << m; //prints the largest possible power of 2

            break; //exits the for loop if the previous number is not half the current number
        }

    }
cout << "<= largest power of two represented by int type. \n";

 double y=1; //initializes x

    for(int j=0;j<10000;j++){ // iteratively multiplies by two

        double k=y;

        y=y*2;

        if(k != y/2){
            cout << k; //prints the largest possible power of 2
            break; //exits the for loop if the previous number is not half the current number
        }

    }
cout << "<= largest power of two represented by double type.";

return 0;
}