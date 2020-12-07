efile=fopen('errorvaluesmatlab.txt','w');
hfile=fopen('hvaluesmatlab.txt','w');

t=2; %time

for iter=0:20 %defines y values
    h=10^(-iter);
    e=abs(derivative_of_function(t) - (1/h).*(func(t+h)-func(t)));
    
    if iter==0
        fprintf(efile,'%.20f',e)
        fprintf(hfile,'%.20f',h)
    end
    
    if iter>1
        fprintf(efile,',%.20f',e)
        fprintf(hfile,',%.20f',h)
    end
    
end


edata=load('errorvaluesmatlab.txt');
hdata=load('hvaluesmatlab.txt');

f=figure

set(f,'Visible','on')

loglog(hdata,edata)

function k=func(t)
    k=1./(1+9*exp(-t));
    %defines the function
end
function d=derivative_of_function(t)
    d=9.*exp(-t).*func(t)^2;
    %defines the functions derivative
end
