import requests 
import zipfile
def fetch_pointer():
    try:
        response=requests.get('http://data.gdeltproject.org/gdeltv2/lastupdate.txt',timeout=10)
        if response.status_code==200:
            lines=response.text.split('\n')
            first_line=lines[0]
            pieces=first_line.split()
            url=pieces[-1]
            return url 
        else:
            print("failed")
            return None
    except Exception as e:
        print("Failed to fetch data",e)
        return None 
def download_and_extract(url):
    try:
        response=requests.get(url,timeout=10)
        if response.status_code==200:
            with open('data.zip','wb') as f:
                f.write(response.content)
            with zipfile.ZipFile('data.zip','r') as zip_ref:
                zip_ref.extractall('data')
            return 'data/'+zip_ref.namelist()[0]
        else:
            print('Failed to download file,status code:',response.status_code)
            return None
    except Exception as e:
        print("Failed to download and extract data:",e)
        return None 
url=fetch_pointer()
print(download_and_extract(url))
