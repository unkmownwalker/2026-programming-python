number=list(input("输入："))
n=len(number)
p=True
for i in range(0,int(n/2)):
    if number[i]!=number[n-i-1]:
         p=False
print(p)
#数学方法
# if x < 0 or (x % 10 == 0 and x != 0):
 #  return False
# 反转一半的数字
 #   reversed_half = 0
 # while x > reversed_half:
 # 取出x的最后一位加到reversed_half
 #   reversed_half = reversed_half * 10 + x % 10 
 #   x //= 10  # 去掉x的最后一位
# 当数字长度为奇数时，通过 reversed_half//10 去除中间位
 #return x == reversed_half or x == reversed_half // 10
