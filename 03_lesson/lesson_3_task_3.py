from address import Address
from mailing import Mailing

to_address = Address('123456','Москва','Лесная','18Б','145')
from_address = Address('654321','Чебоксары','Разведчика Абеля','12к3','64')

delivery = Mailing(to_address, from_address,'1648','147258TRACK')

print(delivery)