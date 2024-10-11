'''Why Is Normalization Important in ML?
Improves Convergence Speed:

Many machine learning algorithms (like gradient descent in neural networks) are sensitive to the scale of data.
If features are on different scales, the algorithm might struggle to find the optimal solution quickly.
By normalizing, all features contribute more evenly to the model, which speeds up the training process.

Some algorithms, like those used in deep learning or regularized linear regression, can become numerically unstable if the input features vary widely in scale.
Normalizing data ensures that the calculations remain stable.

Better Interpretation of Weights:
For example, if one feature represents age (0-100) and another represents income (0-100,000), a weight associated with income might be misleading without normalization.'''


# data - data.min():

# Subtracts 150 from each element in the data array.
# Transforms data from [150, 160, 170, 180, 190] to [0, 10, 20, 30, 40].

# Division by (data.max() - data.min()):
# data.max() - data.min() equals 40 in this example.
# [0, 10, 20, 30, 40] / 40 gives [0, 0.25, 0.5, 0.75, 1].
# This operation scales the values so that the smallest becomes 0 and the largest becomes 1.
# as I'm substracting the same and dividing by the same all data, it keeps the proportion.
import numpy as np

data = np.array([150, 160, 170, 180, 190])

# Normalize the data to range [0, 1]

normalized_data = (data - data.min()) / (data.max() - data.min())
print('normalized_data', normalized_data)


data = np.array([300, 450, 600, 750, 900])

# Calculate the mean of the data
mean = data.mean()

# Perform mean normalization
normalized_data = (data - mean) / (data.max() - data.min())

print("Mean Normalized Data:", normalized_data)



