import numpy as np

# a = np.arange(6).reshape(2,3)
# print(a)
# b= np.arange(6,12).reshape(2,3)
# print(b)

# print(a+b)
# print(b-a)
# print(b/a)
# print(b%a)

# a = np.array([3.4j,2.56j,6,1+3j])
# print(np.imag(a))
# print(np.real(a))
# print(np.conj(a))
# print(np.angle(a, deg=True))



                                                    #swapping
# arr = np.array([1,2,3,4,5,6,7])
# arr[0],arr[6],arr[3] = arr[6],arr[3],arr[0]
# print(arr)

# arr = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])
# # arr[0,2] = arr[2,3]
# arr[0][2] = arr[2][3]
# print(arr)
# arr[[0,1,2],:] = arr[[2,0,1],:]  #row wise swap
# print("row wise swap: \n",arr)
# arr[:,[0,1,2]] = arr[:,[2,0,1]]  #column wise swap
# print("col wise swap: \n",arr)

# a = np.arange(0,30).reshape(3,2,5)
# a[0,0,2] = a[2,1,2]
# print(a)
# a[[0,2],:,[2,3]] = a[[2,0],:,[3,2]]
# #a[[0,2],:,:] = a[[2,0],:,:]
# print(a)

                                                        #identifying missing data
ar = np.array([1,2,np.nan,4,np.nan,8])
is_nan = np.isnan(ar)
print(is_nan)
arr2 = ar[~np.isnan(ar)]
print(arr2)

                                                #replacing missing data
arr = np.array([1,2,np.nan,4,np.nan,8])
res = np.nan_to_num(arr, nan=0)
print(res)



                            #npy file
arr = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])
np.save("data.npy",arr)
res = np.load("data.npy")
print("\ndata in npy file is: \n",res)

arr2 = np.array([1,2,3,4,5,6,7])
np.savez("data2.npz",a=arr,b=arr2)
res = np.load("data2.npz")
print("\ndata in npz file is: \n",res)
print("\nactual data in npy file is: \n",res['a'],"\n",res['b'])


#                                         create sample txt file
with open('dataa.txt','w') as f:
    f.write("1.0 2.0 3.0\n4.0 5.0 6.0\n7.0 8.0 9.0")
data = np.loadtxt("dataa.txt")
print(data)

#                                         create sample csv file
with open('dataaa.csv','w') as f:
    f.write("1.0 2.0 3.0\n4.0 5.0 6.0\n7.0 8.0 9.0")
data = np.genfromtxt("dataaa.csv",delimiter=',')
print(data)


                                    #linear algebra
#3x+2y=5 , x+2y=5          x is 0 and y is 2.5
arr1 = np.array([[3,2],[1,2]])
arr2 = np.array([5,5])
res = np.linalg.solve(arr1,arr2)
print("answer of linear algebra are: \n",res)
res = np.linalg.inv(arr1)
print("inverse is: ",res)