#include <iostream>
#include <vector>
#include <string>
#include<cmath>
#include <fstream>


using namespace std;


double fcn(double t){
	return 1/(1+9*exp(-t));
	//this defines the function
}

double derivative_of_fcn(double t){
    return 9*exp(-t)*pow(fcn(t),2);
    //this defines the functions derivative
}


int main(){
   
    double t=2; //time

    std::ofstream bfile("derivativeerror.txt");

    for(int i=0;i<21;i++){

        double h=pow(10,-((double)i)); //defines delta t

        double e=fabs(derivative_of_fcn(t) - (1/h)*(fcn(t+h)-fcn(t))); //defines the absolute error

        //cout << h <<"," << e <<endl;

        bfile << h <<"," << e <<endl;



    }

return 0;

}