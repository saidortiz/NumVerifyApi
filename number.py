import requests
import json

phone_number = input("Enter valid number:")
print("--------------------------------------")
#change for your API KEY
access_key = 'b7402345dwertwert'
url = 'http://apilayer.net/api/validate?access_key=' + access_key + '&number=' + phone_number
response = requests.get(url)
answer = response.json()

if answer["valid"] == True:
    #print(answer)
    print("Number:",answer["number"])
    print("International format:",answer["international_format"])
    print("Country prefix:",answer["country_prefix"])
    print("Country name:",answer["country_name"])
    print("Location:",answer["location"])
    print("Carrier:",answer["carrier"])
    print("Line type:",answer["line_type"])
else:
    print("not a valid number")
