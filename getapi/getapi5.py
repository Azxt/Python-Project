import requests
def run_getapi5():
    url="https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json"
    
    response=requests.get(url)
    
    data=response.json()
    
    for entry in data:
        sno=entry["sno"]
        sna=entry["sna"]
        area=entry["sarea"]
        mday=entry["mday"]
        ar=entry["ar"]
        sareaen=entry["sareaen"]
        snaen=entry["snaen"]
        aren=entry["aren"]
        act=entry["act"]
        srcuptime=entry["srcUpdateTime"]
        uptime=entry["updateTime"]
        intime=entry["infoTime"]
        indate=entry["infoDate"]
        qua=entry["Quantity"]
        ava_rent=entry["available_rent_bikes"]
        lat=entry["latitude"]
        long=entry["longitude"]
        ava_return=entry["available_return_bikes"]
        print("站點代號 :",sno)
        print("場站中文名稱 :",sna)
        print("場站區域 :",area)
        print("資料更新時間 :",mday)
        print("地點 :",ar)
        print("站區域英文 :",sareaen)
        print("場站名稱英文 :",snaen)
        print("地址英文 :",aren)
        print("全站禁用狀態 :",act)
        print("YouBike2.0系統發布資料更新的時間 :",srcuptime)
        print("大數據平台經過處理後將資料存入DB的時間 :",uptime)
        print("各場站來源資料更新時間 :",indate)
        print("各場站來源資料更新時間 :",intime)
        print("腳踏車數量 :",qua)
        print("場站目前車輛數量 :",ava_rent)
        print("空位數量 :",ava_return)
        print("緯度 :",lat)
        print("經度 :",long)
        print("-"*50)
        
if __name__=='__main__':
    run_getapi5()