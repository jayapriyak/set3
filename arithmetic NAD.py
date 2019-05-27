N,A,D=map(int,input().split())
i=1
summ=0
while i<=N:
	summ=summ+A
	A=A+D
	i=i+1
print(summ)	
