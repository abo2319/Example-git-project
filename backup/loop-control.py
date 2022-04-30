# break 的簡易範例
# n = 0
# while n < 5:
#     if n == 3:
#         break
#     print(n) # 印出迴圈中的 n
#     n+=1
# print("最後的 n:", n) # 印出迴圈結束後的 n, 當n=3 為True, 執行break 跳出if迴圈

#continue 的簡易範例
# n=0
# for x in [0,1,2,3]:
#     if x%2==0: # x 可以被 2 整除, 偶數
#          continue
#     print(x)
#     n+=1
# print("最後的 n:", n)
#while
#n = 1;
#while n < 5:
#    print("變數 n 的資料:", n)
#    n+=1
#else:
#    print(n)

# else 的簡易範例
# sum=0
# fro n in range(11):
#     sun+=n
# else:
#     print(sum) # 印出0+1+2..+10 的結果

# 綜合範例: 找出整數平方根
# 輸入 9, 得到3
# 輸入 11, 得到【沒有】整數的鵬方根
n=input("請輸入一個正整數: ")
n=int(n) # 轉換輸入成數字
for i in range(n): # i 從 0 ~ n-1\
    if i*i==n:
        print("整數平方根", i)
        break # 用 break 強制結束迴圈時, 不會執行else
else:
    print("沒有整數平方根")
