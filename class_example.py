import time


class Person:
    name = None
    age = 0
    local = 'X省XX市XX区XX街道XX号'
    log = []

    def __init__(self, name):
        self.name = name

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
        self.age = age
        self.log_behavior('修改了年龄 ' + str(age))
        return

    def eat(self):

        return True

    def sleep(self):

        return True

    def do_somethings(self):

        return

    def log_behavior(self, msg):
        self.log.append(msg)
        return
