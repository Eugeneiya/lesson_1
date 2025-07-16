from address import Address
from mailing import Mailing

from_address = Address(109109, "Moscow", "Pushkinskaya", 25, 12)
to_address = Address(109209, "Moscow", "Tverskaya", 15, 22)
track = 2909756467
cost = 5


mailing = Mailing(track, from_address, to_address, cost)

print(
    f"Отправление {mailing.track} из {mailing.from_address.index}, "
    f"{mailing.from_address.street}, {mailing.from_address.building} - "
    f"{mailing.from_address.appartment} в {mailing.to_address.index}, "
    f"{mailing.to_address.street}, {mailing.to_address.building} - "
    f"{mailing.to_address.appartment}. "
    f"Стоимость {mailing.cost} рублей."
)
