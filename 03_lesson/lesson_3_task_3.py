from adress import Adress
from mailing import Mailing

to_adress = Adress('123456','Москва','Лесная','18Б','145')
from_adress = Adress('654321','Чебоксары','Разведчика Абеля','12к3','64')

delivery = Mailing(to_adress, from_adress,'1648','147258TRACK')

print(delivery)