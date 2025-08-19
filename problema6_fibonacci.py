# Problema 6 – Fibonacci recursiv (10p)

def fibonacci(n):
    if n==0:
        return 0
    if n==1:
        return 1
    dp=[0] * (n+1)
    dp[1]=1
    for i in range(2,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]

#Exemplu:
n=7
print(f"Fibonacci({n})=",fibonacci(n))
#output: 13
