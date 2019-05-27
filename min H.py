N=int(input())
H=list(map(int,input().split()))
A=H[-1]
for i in range(-1,N):
	if H[i]<A:
		A=H[i]
print(A)		
