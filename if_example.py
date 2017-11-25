cars = ['audi', 'bmw', 'subaru', 'toyato']
for car in cars:
    if car is 'bmw':
        car = car.replace(car, '<b>' + car.upper() + '</b>')
        print(car)
    elif car == 'audi':
        print(car.title())
    else:
        print(car)


print('\n字母大小写')
car_name_1 = 'bmw'
car_name_2 = 'BMW'
print(str(car_name_1 == car_name_2))
print(str(car_name_1.upper() == car_name_2.upper()))

print('\n数字比较')
num1 = 2
num2 = num1 ** 4
print(str(num1 == num2))
print(str(num1 > num2))
print(str(num1 < num2))
numbers = [1, 2, 3, 4, 5]
ok = []
for num in numbers:
    if num <= 3:
        ok.append(num)
print(str(ok))

print('\n多个条件')
par1 = True
par2 = True
par3 = False
print(str(par1 and par2 and par3))
print(str(par1 and par2 or par3))
print(str(par1 and (not par3)))

requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print('Adding mushrooms.')
elif 'pepperoni' in requested_toppings:
    print('Adding pepperoni.')  # 不会执行
elif 'extra cheese' in requested_toppings:
    print('Adding extra cheese.')

if 'pepperoni' not in requested_toppings:
    print('没有添加 pepperoni')

print('\n三元表达式')
username = ''
print('用户名：' + (username if len(username) > 0 else '未知'))  # 不要忘记打括号
