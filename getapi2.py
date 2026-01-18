import requests
def run_getapi2():
    url="https://data.taipei/api/dataset/c493d546-420c-49f2-b992-af058252f293/resource/3639a59d-d9fa-4e0c-8b7f-539a2e37b804/download"
    
    response=requests.get(url)
    #print(response)
    data=response.json()
    #print(data)
    for entry in data:
        sysid=entry["ID"]
        name=entry["tunnel_name"]
        tun_id=entry["tunnel_id"]
        tun_kind=entry["TunnelKind"]
        unit=entry["AdminUnit"]
        county=entry["CountyCode"]
        area=entry["AreaCode"]
        route=entry["Route"]
        design=entry["DesignEngineers"]
        supervise=entry["SuperviseEngineers"]
        build=entry["BuildEngineers"]
        gmaplon=entry["Obj_Longitude"]
        gmaplat=entry["Obj_Latitude"]
        
        print("系統ID=",sysid)
        print("隧道名稱=",name)
        print("隧道編號=",tun_id)
        print("隧道類型單線/雙線=",tun_kind)
        print("轄下機關=",unit)
        print("縣市別代碼=",county)
        print("行政區域代碼=",area)
        print("路線=",route)
        print("設計單位=",design)
        print("監造單位=",supervise)
        print("施工單位=",build)
        print("施工經度=",gmaplon)
        print("施工緯度=",gmaplat)
        print("---------------------------------------------")
        
        lines=entry.get("Lines",[])
        for i,item in enumerate(lines,1):
            print(f"--- 隧道路線 (第 {i} 條) ---")
            print("隧道方向=",item.get("DoubleName"))
            print("編號=",item.get("DoubleNo"))
            print("隧道長度=",item.get("TotalLength"))
            print("隧道面積=",item.get("Area"))
            print("隧道寬度=",item.get("TunnelWidth"))
            print("隧道車道數=",item.get("DriveWay"))
            print("隧道高度=",item.get("TunnelHeight"))
            print("隧道線高=",item.get("DnHeight"))
            print("開始經緯度=",item.get("Longitude_start"),item.get("Latitude_start"))
            print("結束經緯度=",item.get("Longitude_end"),item.get("Latitude_end"))

if __name__=='__main__':
    run_getapi2()

