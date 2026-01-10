def run_calc():
    
    def fun_cul(cal,a,b):
        if cal==1:
            c=fun_plus(a,b)
            d=f"{a}+{b}={c}"
        elif cal==2:
            c=fun_less(a,b)
            d=f"{a}-{b}={c}"
        elif cal==3:
            c=fun_multiply(a,b)
            d=f"{a}*{b}={c}"
        elif cal==4:
            c=fun_except(a,b)
            d=f"{a}/{b}={c}"
        return d
    
    def fun_plus(a,b):
        c=a+b
        return c
    
    def fun_less(a,b):
        c=a-b
        return c
    
    def fun_multiply(a,b):
        c=a*b
        return c
    
    def fun_except(a,b):
        c=a/b
        return c
    def get():
        x=eval(input("請輸入第一個數字 :\n"))
        
        while True:
    
            cal=input("請輸入 1.加法 2.減法 3.乘法 4.除法")        
            if cal in ["1","2","3","4"]:
                cal=int(cal)
                break
            else:
                print("輸入錯誤，請輸入１～４的數字")
                
        y=eval(input("請輸入第二個數字 :\n"))
        total=fun_cul(cal, x, y)
        print(total)
