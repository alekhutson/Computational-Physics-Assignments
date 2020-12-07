%parameters
a=-1;
%time interval and initial conditions
t_interval = [0,10];
init_cond = [1,1];
%solution which uses the RK45 method
[t,y] = ode45(@(t,Y) odefcn(t,Y,a) , t_interval , init_cond);
%plot
plot(t,y(:,1),'b',t,y(:,2),'r');

function dYdt = odefcn(t,Y,a)
dYdt = [ a*Y(1)+Y(2)-Y(1)^3-Y(1)*Y(2)^2;
         -Y(1)+a*Y(2)-Y(2)*Y(1)^2-Y(2)^3];
end

