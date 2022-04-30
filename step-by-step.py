def frac(n):
  r = 1
  if n<=1:
    if n==0 or n==1:
      return 1
    else:
      return False
  else:
    for i in range(1, n+1):
      r *= i
      
    return r
    
frac(-1)
