import numpy as np
#
# 1. Define the input signals
x = np.array([1, 2, 3])
h = np.array([1, 1, 1])
#
# 2. Compute full convolution y[n] = x[n] * h[n]
y_conv = np.convolve(x, h, mode='full')
#
# 3. Compute full cross-correlation r_xh[l]
r_xh   = np.correlate(x, h, mode='full')
#
# 4. Print results
print("Convolution y_conv =", y_conv)        # [1 3 6 5 3]
print("Cross-correlation r_xh =", r_xh)      # [3 5 6 5 3]
