print('Def example')


def get_user():
    return 'ZNEIAT'  # 返回值


def show_user(username, age='未知'):  # age 默认值 保持最后
    """显示用户名"""
    print('Hello, ' + username + ' -> Age: ' + age)
    return


print('\n位置实参')
show_user(get_user(), '15')

print('\n关键字实参')
show_user(username='Siukeo', age='14')
show_user(age='14', username='Siukeo')


def handle_list(raw_dict):
    raw_dict['title'] = 'HelloPython'
    raw_dict['is_edited'] = True


print('\n函数修改字典')
dic_a = {'title': 'HelloWorld'}
print('Before: ' + str(dic_a))
handle_list(dic_a)
print('After: ' + str(dic_a))


print('\n不允许函数修改字典')
dic_b = {'title': 'HelloWorld', 'is_edited': False}
print('Before: ' + str(dic_b))
handle_list(dic_b.copy())  # 字典用 copy()，列表用 [:] 复制为新的一份
print('After: ' + str(dic_b))

print('\n传递任意数量的位置实参')


def make_pizza(*toppings):
    # 得到的 toppings 其实是一个元组
    print('得到的 toppings 元组' + str(toppings))
    for name in toppings:
        print('- ' + name)


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
print('')


def make_pizza_2(size, *toppings):
    """概述要制作的披萨"""
    print("Making a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


make_pizza_2(16, 'pepperoni')
make_pizza_2(12, 'mushrooms', 'green peppers', 'extra cheese')


print('\n传递任意数量的关键字实参')


def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    # 得到的 user_info 是一个字典
    print('得到的 user_info 字典: ' + str(user_info))
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)
