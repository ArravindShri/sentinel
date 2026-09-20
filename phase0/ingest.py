import requests 
import zipfile
def main():
    url = fetch_pointer()
    csv_path = download_and_extract(url)
    rows = parse_events(csv_path)
    dates = []                     
    for row in rows:
        dates.append(row[2])        
    print("rows parsed:", len(rows))
    print("earliest DATEADDED:", min(dates))
    print("latest DATEADDED:", max(dates))

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
def parse_events(filename):
    rows=[]
    try:
        with open(filename,'r') as f:
            for line in f:
                parts=line.strip().split('\t')
                if len(parts)<61:
                    continue
                rows.append([parts[0],parts[1],parts[59],parts[5],parts[6],parts[15],parts[16],parts[26],parts[29],parts[30],parts[31],parts[34],parts[51],parts[52],parts[53],parts[56],parts[57],parts[60]])
        return rows
    except Exception as e:
        print("failed to parse events:",e)
        return None
if __name__ == "__main__":
    main()
