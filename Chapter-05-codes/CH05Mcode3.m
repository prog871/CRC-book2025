% This code finds density k at
% which traffic flow is maximized 
% f(k) = 100k - k^2 - 2500
% using 'ewton-Raphson'
clc; clear; close all;
f=@(k)100*k-k^2-2500;  %f(k)
f_prime=@(k)100-2*k;  %f'(k)
k0 = 60; % Initial guess
epsilon=0.1;%Convergence criterion
X2 = 500;% Maximum iterations
% Newton-Raphson iterations
for iter = 1:X2
  f_k = f(k0);
  f_prime_k=f_prime(k0);  
  k_next=k0-f_k/f_prime_k;%next value   
  diff=abs(k_next-k0);%convergence check    
  if diff<epsilon %Check convergence
    final=round(k_next);%Round 
    fprintf('Iterations = %d\n', iter);
    fprintf('Solution, k = %d\n',final);
    break;
  end    
  k0 = k_next; % Update k0 
end
if iter==X2
    fprintf('\nMaximum iterations\n');
end
% end of M - file
