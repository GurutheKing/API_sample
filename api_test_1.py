#importing the requests library to support api fucntions
import requests
#url to receive teh response from
response = requests.get("http://api.open-notify.org/this-api-doesnt-exist")
print(response.status_code)
