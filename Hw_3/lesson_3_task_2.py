from smartphone import Smarthphone  # type: ignore

phone_1 = Smarthphone
phone_2 = Smarthphone
phone_3 = Smarthphone

phone_1 = ("Samsung", "FE20", "+79958761233")
phone_2 = ("Xiaomi", " 14t", "+79809875643")
phone_3 = ("Motorola", "T20s", "+79151253789")

catalog = [phone_1, phone_2, phone_3]

for phones in catalog:
    print(phones)
