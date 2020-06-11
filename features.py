class TestFeature():
    def __init__(self):
        self.name = 'Denis'
        self.age = 22

    def month(self):
        print('May')

my_feature = TestFeature()
print(my_feature.name)
print(my_feature.age)
my_feature.month()