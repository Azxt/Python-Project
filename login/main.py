import bmi
import tem
import oil
import guess
import calc
import Weight_Management
import electricityprice
import cminchconversion
import multiplication_table
import sys
import datetime
update_time=datetime.datetime.now()

yy=update_time.strftime("%Y")
mm=update_time.strftime("%m")
dd=update_time.strftime("%d")
hh=update_time.strftime("%I")
mins=update_time.strftime("%M")
ss=update_time.strftime("%S")
aa=update_time.strftime("%p")

if aa=="PM":
    ee="晚上"
else:
    ee="早上"
    
print(f"現在時刻 : {yy}年{mm}月{dd}日 {ee}{hh}時{mins}分{ss}秒")
    
print("==歡迎使用 請先登入==")
account="ass123"
passworld="aa0103"
name="Azhong"
count=3
for a in range(count):
    count-=1
    user_acc=input("請輸入帳號 :\n")
    user_pwd=input("請輸入密碼 :\n")
    if user_acc == "" or user_pwd =="":
        print("您輸入的帳號或密碼是空值")
    elif user_acc!=account:
        print("帳號錯誤")
    elif user_pwd!=passworld:
        print("密碼錯誤")
    elif user_acc==account and user_pwd==passworld:
        print(f"{name}登入成功,您好")
        break
    
    if count==0:
        print("帳號已鎖定")
        sys.exit()
    else:
        print(f"帳號密碼錯誤,剩餘{count}次機會,將鎖定帳號")

while True:
    op=int(input("請輸入你要的程式 1.BMI 2.溫度換算 3.加油提示系統 4.猜數字  5.計算機 6. 健康體重管理 7.電費試算 8.公分/英吋換算 9.9x9乘法表 0.離開\n"))
    if op==0:
        print("您選擇離開,程式已結束")
        break
    elif op==1:
        bmi.run_bmi(name)
    elif op==2:
        tem.run_tem()
    elif op==3:
        oil.run_oil()
    elif op==4:
        guess.run_guess()
    elif op==5:
        calc.run_calc()
    elif op==6:
        Weight_Management.run_health(name)
    elif op==7:
        electricityprice.run_ele()
    elif op==8:
        cminchconversion.run_cminch()
    elif op==9:
        multiplication_table.run_multi()
    else:
        print("超出範圍")
        sys.exit()
            
