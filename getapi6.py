import requests
def run_getapi6():
    url="https://tcgbusfs.blob.core.windows.net/dotapp/news.json"
    
    response=requests.get(url)
    
    data=response.json()
    uptime=data["updateTime"]
    print("更新時間 :",uptime)
    
    for entry in data["News"]:
        cht=entry["chtmessage"]
        eng=entry["engmessage"]
        strat=entry["starttime"]
        end=entry["endtime"]
        update=entry["updatetime"]
        con=entry["content"]
        area=entry["areaname"]
        print("中文訊息 :",cht)
        print("英文訊息 :",eng)
        print("開始時間 :",strat)
        print("結束時間 :",end)
        print("資料上傳時間 :",update)
        print("內容 :",con)
        print("影響區域名稱 :",area)
        print("---------------------------------------")      

if __name__=='__main__':
    run_getapi6()