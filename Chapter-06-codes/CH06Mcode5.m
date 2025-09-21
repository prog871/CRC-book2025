%   We use:
%       x = [1, 2, 3]
%       h = [1, 1, 1]
%
%   Then we compute:
%       - y_conv = conv(x, h)
%       - r_xh   = xcorr(x, h)
%
%   Finally, we plot both results in subplots with captions.
%
% 1. Define the input signals
x = [1, 2, 3];
h = [1, 1, 1];
%
% 2. Compute convolution of x and h
y_conv = conv(x, h);  % Convolution
%
% 3. Compute cross-correlation between x and h (r_xh)
r_xh = xcorr(x, h);   % Cross-correlation
%
% 4. Display the results
disp('Convolution y_conv = ');
disp(y_conv);       % Expected: [1  3  6  5  3]
%
disp('Cross-correlation r_xh = ');
disp(r_xh);         % Expected (7 points):
% For x=[1,2,3], h=[1,1,1], the theoretical
% cross-correlation (for all lags) should yield: 
% [3, 5, 6, 5, 3] at the central lags,
% plus extra zeros/padding depending on xcorr's 
% shift convention.