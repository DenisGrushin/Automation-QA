def month_to_season(month):
    if month in(12, 1, 2):
        print("Зима")

    elif month in(3,4,5):
        print("Весна")
        
    elif month in(6,7,8):
        print("Лето")
        
    elif month in(9,10,11):
        print("Осень")
        
    else: return "Некорректный номер месяца"
    
print(month_to_season(2))
print(month_to_season(3))
print(month_to_season(7))
print(month_to_season(10))
print(month_to_season(15))

