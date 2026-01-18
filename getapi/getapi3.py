import requests
def run_getapi3():
    url="https://tppkl.blob.core.windows.net/blobfs/TaipeiParkFacility_Arcade.json"
    
    response=requests.get(url)
    data=response.json()
    
    for entry in data:
        parkname=entry["公園名稱"]
        adimarea=entry["行政區"]
        unit=entry["管理單位"]
        comnum=entry["組合遊具數量"]
        ssnum=entry["磨石滑梯數量"]
        swingnum=entry["鞦韆數量"]
        seesawnum=entry["翹翹板數量"]
        rocknum=entry["搖搖樂數量"]
        climbnum=entry["攀爬組數量"]
        sandpit=entry["戲沙坑數量"]
        boatropenum=entry["擺盪船索數量"]
        othernum=entry["其他數量"]
        x_coords=entry["X坐標"]
        y_coords=entry["Y坐標"]
        
        print("公園名稱=",parkname)
        print("行政區=",adimarea)
        print("管理單位=",unit)
        print("組合遊具數量=",comnum)
        print("磨石滑梯數量=",ssnum)
        print("鞦韆數量=",swingnum)
        print("翹翹板數量=",seesawnum)
        print("搖搖樂數量=",rocknum)
        print("攀爬組數量=",climbnum)
        print("戲沙坑數量=",sandpit)
        print("擺盪船索數量=",boatropenum)
        print("其他數量=",othernum)
        print("X坐標=",x_coords)
        print("Y坐標=",y_coords)
        print("---------------------------------")    
    
if __name__=='__main__':
    run_getapi3()