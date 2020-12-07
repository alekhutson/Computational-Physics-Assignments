times = [];
l = [];
ns = [10,20,50,100,200,500,1000,2000];

for n = ns

    start_time = tic;
    
    matrix = zeros(n,n);
    iden = eye(n);
    
    for i = 1:n
        for j = 1:n
            if i==j
                matrix(i,j)=2/(n+1);
            else
                matrix(i,j)=1/(n+1);
            end 
        end  
    end
    
    term = iden - matrix;
    r= 2;
    
    for k = 1:r
        term = term + ((iden - matrix)^(k))/(k);
    end
    
    end_time = tic;
    times = [times, (end_time - start_time)];
    
    l = [l, n^r];
    
    if n ==10
        b = (-1)*term;
        fle = fopen('output_matlab.txt','w');
        fprintf(fle,'-%d: %d %d\n', b.');
        fclose(fle);
    end
   
end

loglog(ns,times,'o',ns,l,'-')
saveas(gcf,'plot_matlab.png')  

    
