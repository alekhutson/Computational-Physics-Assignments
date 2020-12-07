#include <iostream>
#include <vector>
#include <string>
#include<cmath>
#include <fstream>

using namespace std;

int main(){
    vector <double> a_vector {1,2,3}; //defines a vector a, input any 3 values
    vector <double> b_vector {4,5,6}; //defines a vector b, input any 3 values

    double mag_a = sqrt(pow(a_vector.at(0),2) + pow(a_vector.at(1),2) + pow(a_vector.at(2),2)); //defines the magnitude of vector a
    double mag_b = sqrt(pow(b_vector.at(0),2) + pow(b_vector.at(1),2) + pow(b_vector.at(2),2)); //defines the magnitude of vector b

    vector <double> ab_vector(3); //new vector b-(a.b)a/|a|^2

    double adotb = a_vector.at(0) * b_vector.at(0) + a_vector.at(1) * b_vector.at(1) + a_vector.at(2) * b_vector.at(2); //generates dot product of a and b



    for(int i=0;i<3;i++){ //generates elements of new vector
        ab_vector.at(i) = (b_vector.at(i) - ((adotb)/pow(mag_a,2))*a_vector.at(i));
    }

    double mag_ab = sqrt(pow(ab_vector.at(0),2) + pow(ab_vector.at(1),2) + pow(ab_vector.at(2),2)); //defines the square of the magnitude of new vector

    double c = mag_b/mag_ab; //defines the value of the constant c

    vector <double> v2_vector(3); //defines v2 vector
    for(int i=0;i<3;i++){ //generates elements of v2 vector
        v2_vector.at(i)=c*ab_vector.at(i);
    }

    double mag_v2 = sqrt(pow(v2_vector.at(0),2) + pow(v2_vector.at(1),2) + pow(v2_vector.at(2),2)); //defines the square of the magnitude of v2

    cout << "v1=";

    for(int i=0;i<3;i++){ //prints v1
        cout << a_vector.at(i) <<",";
    }

    cout <<"\n" <<"v2=";

     for(int i=0;i<3;i++){ //prints v2
         cout << v2_vector.at(i) <<",";
     }

return 0;
}