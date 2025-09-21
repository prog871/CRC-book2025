import numpy as np
#
# Parameters
Fs = 1000.0       # Sampling frequency (Hz)
T = 1.0 / Fs      # Sampling period
L = 1000          # Number of sample points
t = np.arange(L) * T  # Time vector
#
f0 = 50.0
x = np.cos(2.0 * np.pi * f0 * t)
#
# Compute the FFT
X = np.fft.fft(x)
#
# Frequency axis
fAxis = np.fft.fftfreq(L, d=T)
#
# Compute the IFFT
x_recovered = np.fft.ifft(X)
#
# Display partial results
print("First few samples of x(t):", x[:5])
print("First few samples of |X|:", np.abs(X[:5]))
print("First few samples of recovered x(t) from IFFT:", \
x_recovered[:5].real)
