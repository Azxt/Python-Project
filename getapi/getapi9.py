import requests
def run_getapi9():
    url="https://tpdep.blob.core.windows.net/techdep/tldep_gamma5m.json"
    
    response=requests.get(url)
    
    data=response.json()
    
    for entry in data:
        seq=entry["SeqNo"]
        time=entry["DTIME"]
        dos=entry["DOSERATE"]
        tem=entry["Temperature"]
        val=entry["VALID"]
        
        print("測站編號 :",seq)
        print("資料的記錄時間 :",time)
        print("環境輻射的劑量率 微西弗/時(μSv/h):",dos)
        print("該時間點的環境溫度 :",tem)
        print("資料的有效性標誌 :",val)
        print("-"*47)
        
if __name__=='__main__':
    run_getapi9()