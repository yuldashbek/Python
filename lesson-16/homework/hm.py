import numpy as np
list_values = [12.23, 13.32, 100, 36.32]
print("Original List:", list_values)
array_values = np.array(list_values)
print("One-dimensional NumPy array:", array_values)

array = np.arange(2, 11).reshape(3, 3)
print(array)
vector = np.zeros(10)
print("Original null vector:", vector)
vector[6] = 11
print("Updated vector:", vector)


array = np.arange(12, 38)
print(array)


original_array = np.array([1, 2, 3, 4])
print("Original array:", original_array)

float_array = original_array.astype(float)
print("Array converted to float:", float_array)


# Values in Centigrade degrees
celsius = np.array([-17.78, -11.11, 7.34, 1.11, 37.73, 0.])
print("Values in Centigrade degrees:", celsius)

# Convert to Fahrenheit
fahrenheit = celsius * 9/5 + 32
print("Values in Fahrenheit degrees:", fahrenheit)



# Original array
original_array = np.array([10, 20, 30])
print("Original array:", original_array)

# Values to append
values_to_append = [40, 50, 60, 70, 80, 90]

# Append values
new_array = np.append(original_array, values_to_append)
print("After append values to the end of the array:", new_array)


# Create a random array of 10 elements (values between 0 and 1)
random_array = np.random.rand(10)
print("Random array:", random_array)

# Calculate statistics
mean = np.mean(random_array)
median = np.median(random_array)
std_dev = np.std(random_array)

print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", std_dev)



