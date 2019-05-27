N=int(input())
G=list(map(int,input().split()))
A=-1
for i in range(-1,N):
	if G[i]>A:
		A=G[i]
print(A)		
