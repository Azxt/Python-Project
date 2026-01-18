import requests
def run_getapi7():    
    
    url="https://publicart.taipei/service/artgetdata.ashx?District_tw=&completeinstallYear=&site_tw="
    
    response=requests.get(url)
    
    data=response.json()
    
    for entry in data:
        sernum=entry["序號"]
        adminarea=entry["行政區"]
        comyear=entry["設置完成年度"]
        name=entry["作品名稱"]
        aut=entry["作者"]
        typework=entry["作品類型"]
        placeaddr=entry["設置地址/地點"]
        placemange=entry["設置單位/管理單位"]
        
        print("序號 :",sernum)
        print("行政區 :",adminarea)
        print("設置完成年度 :",comyear)
        print("作品名稱 :",name)
        print("作者 :",aut)
        print("作品類型 :",typework)
        print("設置地址/地點 :",placeaddr)
        print("設置單位/管理單位 :",placemange)
        print("-"*47)
        
if __name__=='__main__':
    run_getapi7()