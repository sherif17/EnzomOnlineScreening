import csv
import urllib.request
import hashlib

url = 'https://www.stats.govt.nz/assets/Uploads/Annual-enterprise-survey/Annual-enterprise-survey-2020-financial-year-provisional/Download-data/annual-enterprise-survey-2020-financial-year-provisional-csv.csv'
response = urllib.request.urlopen(url)
lines = [l.decode('utf-8') for l in response.readlines()]
cr = csv.reader(lines)

result = ''
x=0

for line in cr:
    if x % 2 == 1:  # check for odd rows
        #column = line.split(',')[2]
        column=line.__getitem__(2)
        result += column
    x += 1
result_md5 = hashlib.md5(result.encode())
final_hash = result_md5.hexdigest().upper()
print('Result : {}'.format(result))
print('MD5 hashed string:{}'.format(final_hash))



