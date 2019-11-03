import string
import numpy as np
from functools import reduce

def print1(arr):
    n = len(arr)
    indices = [0 for i in range(n)]
    res=[]
    while (1):
        t=[]
        for i in range(n):
            t.append(arr[i][indices[i]])
        res.append(t)
        next = n - 1
        while (next >= 0 and
              (indices[next] + 1 >= len(arr[next]))):
            next-=1
        if (next < 0):
            return res
        indices[next] += 1
        for i in range(next + 1, n):
            indices[i] = 0

# modulus = 1000000007
def binomcoeffs(n):
    if n == 1:
        return [[1],[1,1]]
    else:
        recanswer = binomcoeffs(n-1)
        last = list(recanswer[n-1])
        last = [0] + last + [0]
        out = [0]*(n+1)
        for i in range(n+1):
            out[i] = (last[i] + last[i+1]) #% modulus
        recanswer.append(out)
        return recanswer

def solve1dproblem(d,x,reps):
    grid = [0]*(d+2)
    grid[x] = 1
    out = [1] + [0]*reps
    for i in range(reps):
        tempgrid = [0]*(d+2)
        for j in range(1,d+1):
            tempgrid[j] = (grid[j-1] + grid[j+1]) #% modulus
        grid = tempgrid
        out[i+1] = reduce(lambda x,y: (x+y), grid) #%modulus
    return out




dimension,m = map(int,str.split(input()))
D = list(map(int,str.split(input())))
arr=[[ _ for _ in range(1,D[0]+1)] for i in range(D[0])]
all_points_in_dimension=print1(arr)
# print(all_points_in_dimension)

#At this point where to calculate valid paths associated with each one
points=all_points_in_dimension # starting points where to calculate valid paths associated with each one.


all_po=[]
for i in range(len(points)):
    x = points[i]
    binoms = binomcoeffs(m)
    totals = [0]*dimension
    for i in range(dimension):
        totals[i] = [0]*(m+1)
    totals[0] = solve1dproblem(D[0],x[0],m)
    for i in range(1,dimension):
        onedanswer = solve1dproblem(D[i],x[i],m)
        for j in range(m+1):
            for k in range(j+1):
                totals[i][j] = (totals[i][j] + (totals[i-1][j-k])*(onedanswer[k])*(binoms[j][k])) #% modulus
    all_po.append(totals[dimension-1][m])

print(all_po)


all_po=np.array(all_po)
print("ratio stand deviation and mean: %.10f "%float(np.std(all_po)/np.mean(all_po)))
print("maximum: %10d, minimum: %10d"%(np.max(all_po),np.min(all_po)))
print("ratio max, min: %.10f "%float(np.max(all_po)/np.min(all_po)))
print(all_po[0],all_po[-1])


