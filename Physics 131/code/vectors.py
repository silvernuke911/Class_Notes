import numpy as np 

a = np.array([1,2,3])
b = np.array([4,5,6])


delta = np.array([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]) 

levi_civita = np.array([
    [
        [0,  0, 0],
        [0,  0, 1],
        [0, -1, 0]
    ],
    [
        [0, 0, -1],
        [0, 0,  0],
        [1, 0,  0]
    ],
    [
        [ 0, 1, 0],
        [-1, 0, 0],
        [ 0, 0, 0]
    ]
])

basis = np.array([
    [1,0,0],
    [0,1,0],
    [0,0,1]
])

def dot(a, b):
    output = 0
    for i in range(3):
        for j in range(3):
            output += delta[i][j] * a[i] * b[j]
    return output

def cross(a, b):
    output = np.zeros(3)
    for i in range(3):
        for j in range(3):
            for k in range(3):
                output += levi_civita[i][j][k] * a[i] * b[j] * basis[k]
    return output

adotb = np.dot(a,b)
print(adotb)
adotb = dot(a,b)
print(adotb)
acrossb = np.cross(a,b)
print(acrossb)
acrossb = cross(a,b)
print(acrossb)
