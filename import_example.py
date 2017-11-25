import calendar

from def_example_defs import my_functions as examples

examples.hello_world()
examples.hello_python()
examples.your_name()

profile = examples.built_person('ZNEIAT', age='15', localtion='China', sign='write the code. change the world')
print(str(profile))
time = examples.get_time()
time = int(time)  # php 时间戳是 10 位，Java 和 JS 是 13 位
print('当前时间戳 (' + str(len(str(time))) + '位数): ' + str(time))

cal = calendar.month(2018, 1)
print("以下输出2018年1月份的日历:")
print(cal)