from smartphone import Smartphone

catalog = [Smartphone('Samsung','A52','+79255552345'), Smartphone('Xiaomi','POCO X6 Pro 5G','+79854263514'), Smartphone('Huawei','Pura 80 Pro','+79763697452'), Smartphone('Apple','17 Pro Max','+79142563789'), Smartphone('Nokia','90210','+79882556341')]

for smartphone in catalog:
    print(f'{smartphone.brand} - {smartphone.model}. {smartphone.phone_number}.')