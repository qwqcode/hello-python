alien_0 = {'color': 'blue', 'points': 5, 'passwd': '123456'}


def show_info(dic):
    print('颜色:' + dic['color'] + ' 积分:' + str(dic['points']))


show_info(alien_0)
alien_0['points'] = 25
show_info(alien_0)

alien_0['y'] = 25
alien_0['x'] = 0
print(str(alien_0))
del alien_0['passwd']
print(str(alien_0))

print('\n遍历')
users = {
    'charles': {
        'age': 5
    }, 'martina': {
        'age': 10
    }, 'michael': {
        'age': 12
    }, 'florence': {
        'age': 13
    }, 'eli': {}
}

for name, info in users.items():
    print('用户名: ' + name + ', 年龄: ' + (str(
        info['age'] if 'age' in info.keys() else '未知'  # 三元表达式
    )))

values = [value for value in users.values()]
keys = [key for key in users.keys()]
print('Values: ' + str(values) + '\nKeys: ' + str(keys))
