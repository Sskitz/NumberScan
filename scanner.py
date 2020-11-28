import phonenumbers
print(''' 
 __    _                 _                          _____                     
 |\   |  ,   . , _ , _   \ ___    ___  .___        (        ___    ___  , __  
 | \  |  |   | |' `|' `. |/   \ .'   ` /   \        `--.  .'   `  /   ` |'  `.
 |  \ |  |   | |   |   | |    ` |----' |   '           |  |      |    | |    |
 |   \|  `._/| /   '   / `___,' `.___, /          \___.'   `._.' `.__/| /    |
                           
                           Made By: skitz
 ''')

# replace ("+1209-202-5554") with number you want to track.
from phonenumbers import geocoder
phone_number1 = phonenumbers.parse("+1209-202-5554") 
print(geocoder.description_for_number(phone_number1, "en")) # replace "en" with language you would like 
