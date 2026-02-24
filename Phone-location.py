import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

number = "+919471956079"  

parsed_number = phonenumbers.parse(number)

# Country / Region
location = geocoder.description_for_number(parsed_number, "en")

# Carrier
sim_carrier = carrier.name_for_number(parsed_number, "en")

print("Location:", location)
print("Carrier:", sim_carrier)