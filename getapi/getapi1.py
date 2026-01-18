import requests
def run_getapi1():
    url="https://data.moenv.gov.tw/api/v2/aqx_p_432?api_key=af57253c-e838-46da-a1f5-12b43afd75f3&limit=1000&sort=ImportDate desc&format=JSON"
    
    response=requests.get(url)
    #print(response)
    
    data=response.json()
    #print(data)
    
    for entry in data:
        #print(entry)
        site=entry["sitename"]
        city=entry["county"]
        poll=entry["pollutant"]
        status=entry["status"]
        so2=entry["so2"]
        co=entry["co"]
        o3=entry["o3"]
        o3hr8=entry["o3_8hr"]
        pm10=entry["pm10"]
        pm25=entry["pm2.5"]
        no2=entry["no2"]
        nox=entry["nox"]
        no=entry["no"]
        winsp=entry["wind_speed"]
        windir=entry["wind_direc"]
        pub=entry["publishtime"]
        co8=entry["co_8hr"]
        pm25avg=entry["pm2.5_avg"]
        pm10avg=entry["pm10_avg"]
        so2avg=entry["so2_avg"]
        long=entry["longitude"]
        lat=entry["latitude"]
        siteid=entry["siteid"]    
        print("地區=",site)
        print("城市=",city)
        print("空氣汙染物=",poll)
        print("空氣品質=",status)
        print("二氧化硫=",so2)
        print("一氧化碳=",co)
        print("臭氧=",o3)
        print("臭氧(8hr)=",o3hr8)
        print("PM10懸浮微粒=",pm10)
        print("PM2.5懸浮微粒=",pm25)
        print("二氧化氮=",no2)
        print("氮氧化物=",nox)
        print("一氧化氮=",no)
        print("風速=",winsp)
        print("風向=",windir)
        print("日期=",pub)
        print("一氧化碳(8hr)=",co8)
        print("PM2.5(平均)=",pm25avg)
        print("PM10(平均)=",pm10avg)
        print("二氧化硫(平均)=",so2avg)
        print("經度=",long)
        print("緯度=",lat)
        print("狀態=",siteid)
        print("-"*42)
        
if __name__=='__main__':
    run_getapi1()