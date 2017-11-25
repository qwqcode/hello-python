class Car:
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化汽车属性"""
        self.make = make
        self.model = model
        self.year = year
        print('生产了一辆汽车 ' + self.get_descriptive_name())

    def get_descriptive_name(self):
        """返回整洁的描述信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
