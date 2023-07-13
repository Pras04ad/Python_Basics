import numpy as np

arraydata = np.array([1,2,3,4,5,6,1,2,3,4,5,6,7,8,9,0])
print(arraydata.shape)
# Statictic 
sum_arraydata = arraydata.sum()
print(sum_arraydata)

min_arraydata = arraydata.min()
print(min_arraydata)
max_arraydata = arraydata.max()
print(max_arraydata)
mean_arraydata = arraydata.mean()
print(mean_arraydata)

median_arraydata = np.median(arraydata)
print(median_arraydata)
std_arraydata = np.std(arraydata)
print(std_arraydata)


print(sum_arraydata)
print(arraydata)


List_Arraydata = arraydata.tolist()
print(List_Arraydata)

Marraydata = np.array([(1,2,3,4),(1,5,4,6),(4,5,6,7),(5,1,2,9)])
print(Marraydata[0][1])


LT1val = np.array([1,2,3,4,7])
LT2val = np.array([1,2,3,4,5])

print(LT1val == LT2val)
dtypes=[('name', 'S10'), ('grad_year', int), ('cgpa', float)]
values = [('Hrithik', 2009, 8.5), ('Ajay', 2008, 8.7),
           ('Pankaj', 2008, 7.9), ('Aakash', 2009, 9.0)]
arr = np.array(values, dtype = dtypes)
print ("\nArray sorted by names:\n",
            np.sort(arr, order = 'name'))
             
print ("Array sorted by graduation year and then cgpa:\n",
                np.sort(arr, order = ['grad_year', 'cgpa']))
print(np.random.rand(4,2))
print(np.random.randint(4,size=(3,3)))
print(np.identity(3))   #identity matrix

output = np.ones((5,5))
print(output)
z = np.zeros((3,3))
z[1,1]=9
print(z)
output[1:4,1:4]=z
print(output)

a = np.array([1,2,3,4])
a=a+2
print(a)
a=a-2
print(a)

#Linear algebra

a = np.ones((2,3))
print(a)
b = np.full((3,2),2)
print(b)
print(np.matmul(a,b))

#  LOAD DATA FROM FILES

file=np.genfromtxt('data.txt',delimiter=',')
print(file.astype('int32'))

# BOOLEAN MASKING AND ADVANCED INDEXING
print(file[file>50])