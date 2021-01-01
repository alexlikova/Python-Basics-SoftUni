"""city = input().title()
package_type = input()
vip_discount = input().lower()
days = int(input())

result = 0

tourist_agency_dict = {
    "Bansko": {"withEquipment": 100, "noEquipment": 80},
    "Borovets": {"withEquipment": 100, "noEquipment": 80},
    "Varna": {"withBreakfast": 130, "noBreakfast": 100},
    "Burgas": {"withBreakfast": 130, "noBreakfast": 100},
}

if not (city or package_type) in tourist_agency_dict:
    print(f"Invalid input!")
    exit()
if days < 1:
    print(f"Days must be positive number!")
    exit()

if days <= 7:
    if vip_discount == "yes":
        if (city == "Bansko" or city == "Borovets") and (package_type == "withEquipment"):
            result = tourist_agency_dict[city][package_type] * days * 0.9
        elif (city == "Bansko" or city == "Borovets") and (package_type == "noEquipment"):
            result = tourist_agency_dict[city][package_type] * days * 0.95
        elif (city == "Varna" or city == "Burgas") and (package_type == "withBreakfast"):
            result = tourist_agency_dict[city][package_type] * days * 0.88
        elif (city == "Varna" or city == "Burgas") and (package_type == "noBreakfast"):
            result = tourist_agency_dict[city][package_type] * days * 0.93
    else:
        result = tourist_agency_dict[city][package_type] * days
else:
    days -= 1
    if vip_discount == "yes":
        if (city == "Bansko" or city == "Borovets") and (package_type == "withEquipment"):
            result = tourist_agency_dict[city][package_type] * days * 0.9
        elif (city == "Bansko" or city == "Borovets") and (package_type == "noEquipment"):
            result = tourist_agency_dict[city][package_type] * days * 0.95
        elif (city == "Varna" or city == "Burgas") and (package_type == "withBreakfast"):
            result = tourist_agency_dict[city][package_type] * days * 0.88
        elif (city == "Varna" or city == "Burgas") and (package_type == "noBreakfast"):
            result = tourist_agency_dict[city][package_type] * days * 0.93
    else:
        result = tourist_agency_dict[city][package_type] * days
print(f"The price is {result:.2f}lv! Have a nice time!")"""

city= input()
package_type= input()
vip = input()
days= int(input())
vip_member = 0

city_list = ["Bansko", "Borovets", "Varna", "Burgas"]
#pack_list = ["noEquipment", "withEquipment", "noBreakfast", "withBreakfast"]

if city not in city_list or package_type not in pack_list:
   print('Invalid input!')
   exit()

if days <= 0:
    print('Days must be positive number!')
    exit()

city_dict = {city: {'withEquipment': 100, 'noEquipment': 80, 'withBreakfast':130, 'noBreakfast':100}}
vip_dict = {vip: {'withEquipment': 10, 'noEquipment':5, 'withBreakfast':12, 'noBreakfast':7}}

if vip == 'yes':
    vip_member = vip_dict[vip][package_type]

if days > 7:
    days -= 1

hostel = city_dict[city][package_type]
hostel = (hostel * (100 - vip_member)) / 100 * days

print(f'The price is {hostel:.2f}lv! Have a nice time!')


