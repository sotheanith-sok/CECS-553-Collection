import numpy as np

i = np.array([[0,0,0,0,0,0],[0,5,4,2,0,0],[0,1,3,0,1,0],[0,0,0,2,3,0],[0,3,1,0,4,0],[0,0,0,0,0,0]])


fil = np.array([[0,-1,0],[-1,2,-1],[0,-1,0]])

print(np.sum(i[0:3,0:3]*fil))
print(np.sum(i[0:3,1:4]*fil))
print(np.sum(i[0:3,2:5]*fil))
print(np.sum(i[0:3,3:6]*fil))

print(np.sum(i[1:4,0:3]*fil))
print(np.sum(i[1:4,1:4]*fil))
print(np.sum(i[1:4,2:5]*fil))
print(np.sum(i[1:4,3:6]*fil))

print(np.sum(i[2:5,0:3]*fil))
print(np.sum(i[2:5,1:4]*fil))
print(np.sum(i[2:5,2:5]*fil))
print(np.sum(i[2:5,3:6]*fil))

print(np.sum(i[3:6,0:3]*fil))
print(np.sum(i[3:6,1:4]*fil))
print(np.sum(i[3:6,2:5]*fil))
print(np.sum(i[3:6,3:6]*fil))
