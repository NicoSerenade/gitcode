import numpy as np

list1 = [1,2,3,4,5] 

mynp = np.array(list1) #normal python list into array


np1 = np.array([0,1,2,3,4]) #creating numpy array [0 1 2 3 4] shape (5,)
new_np1 = np1.astype(np.float32) #changing datype of array for optimitation
print('old type', np1)
print('new type', new_np1)
#print(np1)
#print(np1.shape)

np2 = np.arange(10) #creating numpy array [0 1 2 3 4 5 6 7 8 9] shape (10,)

np3 = np.arange(0,20, 3) # creating an array [ 0  3  6  9 12 15 18]
#print(np3.shape) = (7,)

np3_1 = np.arange(-5, 6, 2)
print(np3_1)

np3_2 = np.arange(5, -6, -2)
print(np3_2)

#multidimentional arrays

np4 = np.zeros((3, 3))
# [[0. 0. 0.]
#  [0. 0. 0.]
#  [0. 0. 0.]]

np2d = np.array([[1,2,3], [1,2,3]])
print(np2d)
print(np2d.shape) #(rows, columns)

np6 = np.arange(0,20)
print(np6)

np7 = np6.reshape((2, 2, 5)) #reshaping an existing array, this becomes into an 3d array (depth, rows, columns)
print(np7)

np8 = np7.flatten() #creates a copy of a 2D+ array as a 1D
print(np8)

# Create a 3D array with shape (2, 3, 4) (depth, rows, columns)
np3d = np.array([
    [[0,1,2,3], [0,1,2,3], [0,1,2,3]],
    [[0,1,2,3], [0,1,2,3], [0,1,2,3]]
])
print(np3d)
print(np3d.shape)
print(np3d.size) #total items
print(np3d.ndim) #total dimensions

np3d1d = np3d.flatten()
print(np3d1d)

array = np.linspace(-5, 5, 11) #[-5. -4. -3. -2. -1.  0.  1.  2.  3.  4.  5.]

array = np.linspace(-5,5, 7) # [-5. -3.33333333 -1.66666667  0. 1.66666667  3.33333333 5.   ]
print(array)
array = array.astype(np.float16) #[-5. -3.334 -1.667  0.  1.667  3.334  5.   ]
print(array)

rand = np.random.rand(5) # 5 random floats between [0, 1]
print(rand)

randn = np.random.randn(5) #5 random float with a mean of 0 and standard deviation of 1 (standard normal distribution)
print(randn)

randint1d = np.random.randint(0, 5, size = 2) # fill 2 columns with random int in range [0-5)
print(randint1d)

randint2d = np.random.randint(0, 5, size = (2, 3, 4)) #fill 2 layers, 3 rows and 4 columns with random int in range [0-5)
print(randint2d)



