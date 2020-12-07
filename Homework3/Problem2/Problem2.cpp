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
	deriv[2]=-x[1];
}
//the actual function for the pendulum

double pi=2*asin(1);
//pick a value of pi.  This is typo free...
//github example in class.


int main(){
	
	double theta=0;
	double omega=1;
	double t=0;
	double T=5;
	//physical parameters
	
	double dt=0.005;
	int nstep=((int)(T/dt));
	//integrator parameters
	
	int dim=2;
	double* param= new double[dim+1];
	double* X=new double[dim+1];
	double* deriv=new double[dim+1];
	//memory allocation

	std::ofstream outRK("RK_cpp.txt");
	std::ofstream outVerlet("verlet_cpp.txt");
	std::ofstream g1("g1.txt");
	std::ofstream g2("g2.txt");
	
	std::vector<double> vec;
	vec={0.5,0.1,0.005,0.001,0.0005,0.0001};

	for(double dt:vec){

	
		X[1]=theta;
		X[2]=omega;
		t=0;
		for(int i=0;i<nstep;i++){
			rk4(X,dim,t,dt,F,param);
			t+=dt;
		}
		outRK<<dt<<","<<X[1]<<"\n";

		double k=abs(sin(5) - X[1]);
		g1<<dt<<","<<k<<"\n";
		

		X[1]=theta+omega*dt+dt*dt*(-sin(theta));
		X[2]=theta;
		t=0;
		for(int i=0;i<nstep;i++){
			double xcurr=X[1];
			X[1]=2*X[1]-X[2]+dt*dt*(-sin(X[1]));
			X[2]=xcurr;
			t+=dt;
		}
		outVerlet<<dt<<","<<X[1]<<"\n";

		double m=abs(sin(5) - X[1]);
		g2<<dt<<","<<m<<"\n";

	}
	
	outRK.close();
	outVerlet.close();
	g1.close();
	g2.close();

	return 0;
}
