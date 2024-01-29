# найти високосный или нет год
def visolos_ear(year):
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        return "Yes"
    return "No"

print(visolos_ear(2023))