import requests
def run_getapi10():
    url="https://iheritage.gov.taipei/data/api/designation/data"
    
    response=requests.get(url)
    
    data=response.json()
    
    for entry in data:
        name=entry["個案名稱"]
        assclass=entry["資產類別"]
        asstype=entry["資產種類"]
        auth=entry["所屬主管機關"]
        area=entry["所在地理區域"]
        addr=entry["現況地址"]
        
        addr_list=entry.get("現況地址",[])
        if isinstance(addr_list,list):
            addr="、".join(addr_list)
        else:
            addr=addr_list
            
        unit=entry["管理單位"]
    
        print("個案名稱 :",name)
        print("資產類別 :",assclass)
        print("資產種類 :",asstype)
        print("所屬主管機關 :",auth)
        print("所在地理區域 :",area)
        print("現況地址 :",addr)
        print("管理單位 :",unit)
        print("-"*47)
        
if __name__=='__main__':
    run_getapi10()