get_link='http://data.gdeltproject.org/gdeltv2/20260919034500.export.CSV.zip'
print(get_link.startswith('http'))
print(len(get_link))
print(get_link[-4:])

meta_data_columns=['Actor1Code','Actor1Name','Actor2Code','Actor2Name','EventCode']
print(meta_data_columns[-5])
print(meta_data_columns[-1])
print(len(meta_data_columns))
print(sorted(meta_data_columns))

string_input="1323802237\t20250919\tGOV\tPRESIDENT"
string_list=string_input.split('\t')
print(string_list)
print(len(string_list))
print(string_list[2])

temp_list=[3,15,7,22,1,18]
for temp in temp_list:
    if temp>10:
        print('big')
    else:
        print('small')

temp_list=[3,15,7,22,1,18]
count_initial=0
for temp in temp_list:
    if temp>10:
        count_initial+=1
print(count_initial)

ship_items={'shipno':1234, 
            'country':'USA',
            'Gold_scale': 5}
ship_items['Status']='Currently Stuck in strait'
print(ship_items['country'])
for key,value in ship_items.items():
    print(key,':',value)

def is_serious(goldstein):
    return goldstein<=-5
print(is_serious(-7))
print(is_serious(0))
print(is_serious(3))

def count_serious(scores):
    count_initial=0
    for score in scores:
        if score <=-5:
            count_initial+=1
    return count_initial
print(count_serious([-7, 0, 3, -9, -2]))

import requests
try:
    response=requests.get('http://data.gdeltproject.org/gdeltv2/nope.txt',timeout=10)
    print(response.status_code)
except Exception as e: 
    print("Failed to fetch data:",e)

import requests
try:
    response=requests.get('http://data.gdeltproject.org/gdeltv2/20260919034500.export.CSV.zip',timeout=10)
    print(response.status_code)
    with open('data.zip','wb') as f:
        f.write(response.content)
    import zipfile
    with zipfile.ZipFile('data.zip') as zip_ref:
        print(zip_ref.namelist())
        zip_ref.extractall('data')
except Exception as e:
    print(f"An error occurred: {e}")
