from Address import Address
from Mailing import Mailing

to_Address = Address("55555", "Irkutsk", "Pobeda", "10", "12")
from_Address = Address("33333", "Tula", "8Marta", "5", "23")
mailing = Mailing(to_Address, from_Address, 500, "ABC123")

print(f"Отправление {mailing.track} из {mailing.from_Address.index}, {mailing.from_Address.city},"
      f" {Mailing.from_address.street}, {Mailing.from_address.hous} - {Mailing.from_address.apartment}"
      f" в {Mailing.to_address.index}, {Mailing.to_address.city}, {Mailing.to_address.street},"
      f" {Mailing.to_address.house} - {Mailing.to_address.apartment}. Стоимость {Mailing.cost} рублей.")

