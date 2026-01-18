import requests
def run_getapi4():
    url="https://tcgbusfs.blob.core.windows.net/blobtcmsv/TCMSV_alldesc.json"
    
    response=requests.get(url)
    
    data=response.json()
    park_list=data.get("data",{}).get("park",[])
    #print(f"{len(park_list)} 個停車場")
    for entry in park_list:
        p_type=entry["type"]
        if p_type =="1":
            desc="動態停車場"
        elif p_type=="2":
            desc="靜態停車場 "
        else:
            print("超出範圍")
        parkid=entry["id"]
        area=entry["area"]
        name=entry["name"]
        summary=entry["summary"]
        addr=entry["address"]
        tel=entry["tel"]
        payex=entry["payex"]
        servertime=entry.get("serviceTime","未提供")
        t97x=entry["tw97x"]
        t97y=entry["tw97y"]
        car=entry["totalcar"]
        motor=entry["totalmotor"]
        bike=entry["totalbike"]
        bus=entry["totalbus"]
        preg=entry["Pregnancy_First"]
        handicap=entry["Handicap_First"]
        argemotor=entry.get("totallargemotor")
        charging=entry.get("ChargingStation")
        taxifree=entry["Taxi_OneHR_Free"]
        aed=entry["AED_Equipment"]
        signal=entry["CellSignal_Enhancement"]
        elevator=entry["Accessibility_Elevator"]
        charge=entry["Phone_Charge"]
        child=entry["Child_Pickup_Area"]
    
        print(f"【{name}】")
        print("停車場編號 :",parkid)
        print("行政區 :",area)
        print(f"{desc} :",p_type)
        print("停車場概況 :",summary)
        print("停車場地址 :",addr)
        print("停車場電話 :",tel)
        print("收費資訊 :",payex)
        print("開放時間 :",servertime)
        print("國家座標 X :",t97x)
        print("國家座標 Y :",t97y)
        print("總車位數 :",car)
        print("機車總格位數 :",motor)
        print("腳踏車總車架數 :",bike)
        print("大客車總車位數 :",bus)
        print("孕婦優先車格位數 :",preg)
        print("身障車格位數 :",handicap)
        print("重機停車位數 :",argemotor)
        print("充電站數 :",charging)
        print("計程車 1hr 免費車位數:",taxifree)
        print("ADE 急救 :",aed)
        print("訊號增強設備 :",signal)
        print("無障礙電梯 :",elevator)
        print("手機充電 :",charge)
        print("親子車位 :",child)
        print("---------------------------------------------------------")

if __name__=='__main__':
    run_getapi4()
               