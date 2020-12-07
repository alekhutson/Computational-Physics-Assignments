#include <iostream>
#include <fstream>
#include <math.h>

double logistic_calculate(double r,double x){ //updates value of x
	return r*x*(1-x);
}

int main(){
	int max_iteration=50;  //how many iterations to do
	double r=2.00;  //our choice for r.
    double d=2.99;   // second choice for r
	double x=0.01;  //our initial value.

    std::ofstream bfile("xp_values_2.00.txt");
    std::ofstream xfile("x_values_2.00.txt");
    
    xfile<<x<<",";
    
	for(int iter=0;iter<max_iteration;iter++){//places values of xn in file
		
		x=logistic_calculate(r,x);
        xfile<<x<<",";
	}
    x=0.01;
    for(int iter=0;iter<=max_iteration;iter++){//places values of xn+1 in file
		
		x=logistic_calculate(r,x);
        bfile<<x<<",";
	}
    

    bfile.close();
    xfile.close();//closes files

    std::ofstream pfile("xp_values_2.99.txt");
    std::ofstream yfile("x_values_2.99.txt");

    x=0.01;
    yfile<<x<<",";

    for(int iter=0;iter<max_iteration;iter++){
		
		x=logistic_calculate(d,x);
        yfile<<x<<",";
	}
    x=0.01;
    for(int iter=0;iter<=max_iteration;iter++){
		
		x=logistic_calculate(r,x);
        pfile<<x<<",";
	}


	pfile.close();
    yfile.close();

	return 0;

}
