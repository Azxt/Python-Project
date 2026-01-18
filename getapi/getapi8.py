import requests
def run_getapi8():
    url="https://www.tpedoit.gov.taipei/OpenData.aspx?SN=1EF1FA5ED5ECF95F"
    
    response=requests.get(url)
    response.encoding="utf-8-sig"
    data=response.json()
    
    for entry in data:
        datasn=entry["DataSN"]
        arttype=entry["ArticleType"]
        file=entry["FileName"]
        link=entry["Link"]
        sou=entry["Source"]
        title=entry["title"]
        cno=entry["內容"]
        datetime=entry["日期時間"]
        lssunit=entry["發布單位"]
        
        print("資料序號 :",datasn)
        print("文章類型 :",arttype)
        print("檔案名稱 :",file)
        print("連結 :",link)
        print("來源 :",sou)
        print("標題 :",title)
        print("內容 :",cno)
        print("日期時間 :",datetime)
        print("發布單位 :",lssunit)
        print("-"*47)
    
if __name__=='__main__':
    run_getapi8()