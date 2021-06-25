import random
from faker import Faker

worker = ("Проектировщик", "Архитектор", "Инженер")
division = ("Цифровое моделировние недвижимости",
           "Расчетный отдел", "Отдел экспертизы")

random.seed(version = 2)
_file = "work.csv"

if __name__ == '__main__':
    f = open(_file, 'w')
    fake = Faker('ru_RU')
    for i in range(1,101):
        f.write(str(i) + "; " + 
                fake.name() + "; " + 
                fake.random_element(elements = worker) + "; " + 
                fake.random_element(elements = division) + "; " + 
                str(random.randint(1,5)) + "; " + 
                str(random.randint(40,1600)) + 
                "000; \n")
    f.close()

