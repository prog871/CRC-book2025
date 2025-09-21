% Parameters
Fs = 1000;         % Sampling frequency (Hz)
T = 1/Fs;          % Sampling period
L = 1000;          % Length of signal
t = (0:L-1)*T;     % Time vector
%
f0 = 50;           % Frequency of the cosine (Hz)
x = cos(2*pi*f0*t);  % Our discrete signal
%
% Compute the FFT
X = fft(x);
%
% Frequency axis for plotting
fAxis = (0:L-1)*(Fs/L); 
%
% Compute the IFFT
x_recovered = ifft(X);
%
% Display results
disp('First few samples of the original signal x(t):');
disp(x(1:5));
disp('First few samples of the magnitude of FFT(X):');
disp(abs(X(1:5)));
disp('First few samples of the recovered signal (IFFT):');
disp(x_recovered(1:5));