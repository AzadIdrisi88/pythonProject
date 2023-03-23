n = 1369
rev = 0
while n > 0:
    rem = n % 10
    n //= 10  # n=n + 1, n+=1, n=n/1, n/=10, n=n//10 n//=10
    rev = rev * 10 + rem
print(rev)
