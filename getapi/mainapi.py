import getapi1
import getapi2
import getapi3
import getapi4
import getapi5
import getapi6
import getapi7
import getapi8
import getapi9
import getapi10

def menu_print():
    print("---台北市各項資料查詢---")
    print("---0 :離開系統---")
    print("---1 :空氣品質指標---")
    print("---2 :臺北市隧道資訊---")
    print("---3 :臺北市公園兒童遊戲場---")
    print("---4 :臺北市停車場資訊V2---")
    print("---5 :YouBike2.0臺北市公共自行車即時資訊---")
    print("---6 :臺北市即時交通訊息---")
    print("---7 :臺北市公共藝術---")
    print("---8 :臺北市水域遊憩活動訊息公告---")
    print("---9 :臺北市環境輻射監測---")
    print("---10 :臺北市文化資產---")
    print("-"*42)
    
def main():
    n=0
    while True:
        menu_print()
        get=int(input("請輸入你要查尋的資料代碼 :"))

        if get==1:
            getapi1.run_getapi1()
        elif get==2:
            getapi2.run_getapi2()
        elif get==3:
            getapi3.run_getapi3()
        elif get==4:
            getapi4.run_getapi4()
        elif get==5:
            getapi5.run_getapi5()
        elif get==6:
            getapi6.run_getapi6()
        elif get==7:
            getapi7.run_getapi7()
        elif get==8:
            getapi8.run_getapi8()
        elif get==9:
            getapi9.run_getapi9()
        elif get==10:
            getapi10.run_getapi10()
            
        elif get==0:
            print("--------感謝您的使用，稍後將離開系統--------")
            break
        
        else:
            n+=1
            print("-"*42)
            if n<3:
                print(f"------查無資料代碼，請重新輸入(錯誤{n}次)-----")
                print("-"*42)
                continue
            else:
                print("---輸入錯誤次數已超過上限，系統將自動退出---")
                print("-"*42)
                break

if __name__=='__main__':
    main()