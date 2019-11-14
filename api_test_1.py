#importing the requests library to support api fucntions
import requests
#url to receive the response from notn working end-point
#response = requests.get("http://api.open-notify.org/this-api-doesnt-exist")
#success code 200 - with working end-point
response2= requests.get("http://api.open-notify.org/astros.json")
print(response2.status_code)
#print the data recived as response as JSON
print(response2.json())
