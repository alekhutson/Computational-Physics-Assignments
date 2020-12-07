x=1.0;

for iter=0:1000
    m=x;
    x=x*2;
  
    if x ~= 2*m
        disp(m)
        exit
    end
end

%this produces "inf" after 1000 iterations for 1 or 1.0