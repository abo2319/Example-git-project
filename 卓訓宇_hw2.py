#1

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
print(frac(6))

#2
def strr(abc):
    big = 0 
    small = 0 
    for x in abc: 
        if x.islower(): 
            small+=1 
        if x.isupper(): 
            big+=1 
    print((str(big))+' '+(str(small)))
strr('AAAbccD')

#3
def va(n):
    x = []
    for i in range(2, n):
        isPrime = True
        for j in range (2,i):
            if i % j == 0:
                isPrime = False
                break
        if isPrime:
            x.append(i)
    print(x)
va(10)

#4
a = [1,4,7,9,12,66]
result = map(lambda x: x*x, a)
print(list(result))

#5
def nba_stats(arg1, arg2, *args, **kwargs):
    print('場均最高分:', arg1)
    print('場均第二高分:', arg2)
    print('其他球員:', args)
    print('其他數據:', kwargs)
    return

nba_stats('Beal', 'Lillard', 
          'James', 'Curry', 'Carry', 'Harden',
          籃板王 = 'Capela', 阻攻王 = 'Turner', 助攻王 = 'Harden', Leo王 = 'Leo')

nba_stats('Beal', 'Lillard', 
          'James', 'Curry', 'Harden',
          籃板王 = 'Capela', 阻攻王 = 'Turner', 助攻王 = 'Harden')

#6
#6.1
def isOdd(n):
    if n > 0 and n % 2 == 1:
        return n
    return
a = [2, -3, 3.3, 23, 78, 111, 0]
alist = filter(isOdd,a)
print(list(alist))

#6.2
a = [2, -3, 3.3, 23, 78, 111, 0]
alist = [i for i in a if i > 0 and i % 2 == 1]
print(list(alist))
# %%
