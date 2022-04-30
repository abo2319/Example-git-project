#定義一個印出Hello的函式
#def sayHello():
#    print("Hello")
#呼叫上方定義的函式,程式跳到函式的裡面印出程式碼
#sayHello()
#定義可以印出任何訊息的函式
#def say(msg):
#    print(msg)
# 定義函式
# 函式內部的程式碼, 若沒有做函式呼叫就不會執行
def multiply(n1,n2):   
    return n1*n2
# 呼叫函式(函式的呼叫式流程的變化,呼叫完看回傳值(沒有寫return但函式的程式碼以跑完,系統會自動return))
value=multiply(2,4)+multiply(10,5) # (2*4)+(10*5)
print(value)
# multiply(3,4)
# multiply(24,65)

# 函式可用來做程式的包裝(如果類似的動作一直做 就可以使用函式) 
# 同樣的邏輯可以重複利用
def calculatr(max): 
    sum=0
    for n in range(1,max+1)
        sum=sum+0
    print(sum)

calculate(10)
calculate(20)

