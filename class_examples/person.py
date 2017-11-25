import time


class Person:
    name = None
    age = 0
    local = 'X省XX市XX区XX街道XX号'
    log = []
    car = None

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_name(self, name, why):
        if len(name) < 2:
            return False

        if len(why) <= 0:
            why = '未注明原因'
        else:
            why = time.strftime('%Y-%m-%d %H:%M:%S') + ' 修改了名字，原因是：' + why

        self.log_behavior(why)
        self.name = name

        return True

    def set_age(self, age):
        self.log_behavior('蓦然回首... ' + self.get_name() + ' 长大了 ' + str(age - self.age) + ' 岁')
        self.age = age
        return

    def log_behavior(self, msg):
        print(msg)
        self.log.append(msg)
        return

    def own_car(self, car):
        self.log_behavior(self.get_name() + ' 拥有了汽车：' + car.get_descriptive_name())
        self.car = car
