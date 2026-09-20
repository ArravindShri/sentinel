import requests 
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
print(fetch_pointer())