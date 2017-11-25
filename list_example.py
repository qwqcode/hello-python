squares = []
for i in range(1, 20):
    squares.append(i ** 30)
print(squares)
print('Min: ' + str(min(squares)))
print('Max: ' + str(max(squares)))
print('Sum: ' + str(sum(squares)))

digits = [1, 2, 3]
squares = [value**2 for value in digits]
print('Squares: ' + str(squares))

print('\n切片')
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print('1.' + str(players[0:3]))  # 截取第一位到第三位的字符
print('2.' + str(players[:]))  # 截取字符串的全部字符
print('3.' + str(players[6:]))  # 截取第七个字符到结尾
print('4.' + str(players[:-3]))  # 截取从头开始到倒数第三个字符之前
print('5.' + str(players[2]))  # 截取第三个字符
print('6.' + str(players[-1]))  # 截取倒数第一个字符
print('7.' + str(players[::-1]))  # 创造一个与原字符串顺序相反的字符串
print('8.' + str(players[-3:-1]))  # 截取倒数第三位与倒数第一位之前的字符
print('9.' + str(players[-3:]))  # 截取倒数第三位到结尾
print('10.' + str(players[:-5:-3]))  # 逆序截取
food_list = ['1.lolipop', '2.oreo', '3.cookie']
print('You select food is: ' + str(food_list[0:-2]))  # 正数是从0开始 倒数是从1开始(food_list[-1])

print('\n复制列表')
users = ['charles', 'martina']
vip_users = users[:]
vip_users.append('michael')
print('相同？' + str(users == vip_users) + ' ' + str(users))

users = ['charles', 'martina']
vip_users = users
vip_users.append('michael')
print('相同？' + str(users == vip_users) + ' ' + str(users))

print('\n元组 (Tuple)\n元组与列表类似，不同之处在于元组的元素不能修改')
tup1 = ('charles', 'martina')
for idx, val in enumerate(tup1):
    print(str(idx+1) + '. ' + val)