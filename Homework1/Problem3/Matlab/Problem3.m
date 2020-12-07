a_vector = [1,2,3]; %defines an array a
b_vector = [4,5,6]; %defines an array b

mag_a = sqrt(a_vector(1).^2 + a_vector(2).^2 + a_vector(3).^2); %magnitude of vector a
mag_b = sqrt(b_vector(1).^2 + b_vector(2).^2 + b_vector(3).^2); %magnitude of vector b

adotb = a_vector(1)*b_vector(1) + a_vector(2)*b_vector(2) + a_vector(3)*b_vector(3); %dot product of a and b

ab_vector = [0,0,0];

for iter=1:3 %creates elements of ab_vector
    ab_vector(iter) =  (b_vector(iter) - ((adotb)/(mag_a.^2))*a_vector(iter));
end

mag_ab = sqrt(ab_vector(1).^2 + ab_vector(2).^2 + ab_vector(3).^2); %magnitude of ab_vector
c= mag_b/mag_ab;

v2_vector = [0,0,0]; %defines v2

for riter=1:3 %creates elements of v2
    v2_vector(riter) = c*ab_vector(riter);
end

a_vector
v2_vector