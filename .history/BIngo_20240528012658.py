N, T = list(map(int,input().split()))
A =  list(map(int,input().split()))
B = = [[0 for i in range(N)] for j in range(N)]


for c in range(0,len(B)):
  for i in range(0,N):
    for j in range(0,N):
      if N * i  + j - 1 == A[c]:
        B[i][j] = 1
        if sum(B[i]) or 
        
  
print(B)