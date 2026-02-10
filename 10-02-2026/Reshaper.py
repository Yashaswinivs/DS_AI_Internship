import numpy as np

# 1D array from 0 to 23
data = np.arange(24)

# Reshape into (4, 3, 2)
reshaped = data.reshape(4, 3, 2)

# Transpose to shape (4, 2, 3)
transposed = reshaped.transpose(0, 2, 1)

print("Final Shape:", transposed.shape)
print("\nFinal Array:\n", transposed)
