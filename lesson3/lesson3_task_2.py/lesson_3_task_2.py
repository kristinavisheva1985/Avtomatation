from Smartphone import Smartphone

catalog = []
phone1 = Smartphone("Samsung", "Galaxy21", "+7923456720")
phone2 = Smartphone("Apple", "Iphone15", "+7923456723")
phone3 = Smartphone("Oppo", "S31", "+7923456725")
phone4 = Smartphone("Noria", "G21", "+7923456729")
phone5 = Smartphone("Samsung", "SX16", "+7923456727")

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_namber}")
    



