from address import Address
from mailing import Mailing

to_address = Address('123456','Москва','Ленина','13Б','145')
from_address = Address('654321','Чебоксары','Разведчика Абеля','12к3','68')

delivery = Mailing(to_address, from_address, '1654', '456123TRACK')

print(delivery)