def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country = 63, area = 918 , first = 694 , last = 8018)

print(phone_num)