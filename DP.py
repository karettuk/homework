#하향식 DP 메모이제이션
d= [0]*100
def fibo(n):
    print('f({})'.format(str(n)))
    if n == 1 or n==2:
        return 1
    if d[n] != 0 :
        return d[n]
    else : 
        d[n] = fibo(n-1)+fibo(n-2)
        return d[n]

    
#상향식 DP 메모이제이션    
dp = [0]*100
dp[1]=1
dp[2]=1
n=6
for i in range(3, n+1):
    dp[i] = dp[i-1]+dp[i-2]
fibo(6)