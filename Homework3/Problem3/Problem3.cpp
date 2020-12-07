#include <vector>
#include "NumMeth.h"
#include "rk4.cpp"

extern void rk4(double x[], int nX, double t, double tau,
				void (*derivsRK)(double x[], double t, double param[], double deriv[]),
				double param[]);
//for reasons I cannot understand, Garcia has chosen to index his functions
//starting at i=1.  x[0] is not updated using is rk4 function, so our vectors will have
//the first element as a null value.  I will keep that notation in this script.
//it is possible he intended the first element to be the time, but this is not
//clear in his function definition.


void F(double x[],double t,double param[],double deriv[]){
	deriv[1]=x[2];
    deriv[2]=x[3];
	deriv[3]=(1-6*x[1])*x[2];
}
//the actual function

double pi=2*asin(1);
//pick a value of pi.  This is typo free...
//github example in class.


int main(){
	
	double theta=.5;
	double omega=0;
    double h=-.25;
	double t=0;
	double T=50;
	//physical parameters
	
	double dt=0.005;
	int nstep=((int)(T/dt));
	//integrator parameters
	
	int dim=3;
	double* param= new double[dim+1];
	double* X=new double[dim+1];
	double* deriv=new double[dim+1];
	//memory allocation

	std::ofstream outRK("RK_cpp_d.txt");
    std::ofstream sln("actual_solution.txt");
	
		X[1]=theta;
		X[2]=omega;
        X[3]=h;
		t=0;

		for(int i=0;i<nstep;i++){
			rk4(X,dim,t,dt,F,param);
			t+=dt;
            outRK<<t<<","<<X[1]<<"\n";
            double k=.5*pow(1/cosh(t/2),2);
            sln<<t<<","<<k<<"\n";
		}
	outRK.close();
    sln.close();

	return 0;
}
