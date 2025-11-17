class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def sayName(self):
        print('Мое Имя :', self.first_name)

    def saySurname(self):
        print('Моя Фамилия : ', self.last_name)

    def sayFullName(self):
        print(f'Меня зовут : {self.first_name} {self.last_name}')