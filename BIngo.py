N, T = list(map(int,input().split()))
A =  list(map(int,input().split()))
B =  [[0 for i in range(N)] for j in range(N)]


for c in range(0,len(B)):
  for i in range(0,N):
    for j in range(0,N):
      if N * i  + j - 1 == A[c]:
        B[i][j] = 1
        if sum(B[i]) or 
        
  
print(B)


import numpy as np

N, T = list(map(int,input().split()))
A =  list(map(int,input().split()))
row =  [0] * N
col =  [0] * N



for c in range(0,len(B)):
  for i in range(0,N):
    for j in range(0,N):
      if N * i  + j - 1 == A[c]:
        B[i][j] = 1
        if sum(B[i]) or 
        
  
print(B)
#-----


N, T = list(map(int,input().split()))
A =  list(map(int,input().split()))
row =  [0] * N
col =  [0] * N
t1 = 0
t2 = 0
flag = False

for c in range(0,len(A)):
  for i in range(0,N):
    for j in range(0,N):
      if N * i  + j - 1 == A[c]:
        row[i] = row[i] + 1
        col[j] = col[j] + 1
      if j == N - i:
        t1 = t1 + 1
      if j == i:
        t2 = t2 + 1
      if  row[i] == N or col[j] == N or t1 == N or t2 == N:
        flag = True
        print(row[i], col[j], t1, t2)
        print(c + 1)
        break
  if flag:
    break

  #--------
N, T = list(map(int,input().split()))
A =  list(map(int,input().split()))
row =  [0] * N
col =  [0] * N
t1 = 0
t2 = 0
flag = False
#print(row[i], col[j], t1, t2)
for c in range(0,len(A)):
  for i in range(1, N + 1):
    for j in range(1, N + 1):
      if N * (i - 1)  + j  == A[c]:
        #print (i,j,A[c])
        #print(row[i], col[j], t1, t2)
        row[(i - 1)] = row[(i - 1)] + 1
        col[(j - 1)] = col[(j - 1)] + 1
        if j == N - i:
          t1 = t1 + 1
        if j == i:
          t2 = t2 + 1
      if  row[(i -1)] == N or col[(j -1)] == N or t1 == N or t2 == N:
        flag = True
        #print(row[(i -1)], col[(j -1)], t1, t2)
        print(c + 1)
        break
      else:
        if c == T - 1:
          flag = True
          print(-1)
          break
    if flag:
      break
  if flag:
    break



        
  
