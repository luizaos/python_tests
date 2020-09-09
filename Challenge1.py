import requests

url = 'https://jsonplaceholder.typicode.com/photos'

#get the data about the photos
response = requests.get(url)

#read that data into a variable
json_data = response.json()

#create a list for storing the url of each photo
url_list = []
for photo in json_data:
    url_list.append(photo['url'])

#how many items are in the url list (should be 5000)
print(len(url_list))

#how many items are there if we turn that list into a set? (the set function removes all the duplicated info in a list)
print(len(set(url_list)))
