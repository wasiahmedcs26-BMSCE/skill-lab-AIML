import numpy as np
# arr=np.array([1,2,3,4,5])
# print(arr)
# print("Dimension:",arr.ndim)
# print("shape", arr.shape)
# print("MAX:", max(arr))
# print("MIN:", min(arr))
# print("Length:",len(arr))

#vectorization
# emp_sal=np.array([50000,75000,68000,59000,81000,32000,74000])
# #10% hike
# emp_sal=emp_sal+(emp_sal*0.1)
# print(emp_sal)
# arr=np.array([15,25,20,35,30,45,40])
# print(arr+10)
# print(arr*5)
# print(arr//5)

arr0=np.array(25)
arr1=np.array([1,2,3,4,5])
arr2=np.array([[1,2,3],
               [4,5,6]])

arr3=np.array([
    [[1,2,3],[4,5,6]],
    [[7,8,9],[10,11,12]
                ]])

print(arr0)
print(arr1)
print(arr2)
print(arr3)

print(arr0.ndim)
print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)

print(arr0.shape)
print(arr1.shape)
print(arr2.shape)
print(arr3.shape)
