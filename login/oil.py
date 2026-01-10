def run_oil():
    oil=int(input("請輸入公升數 "))
    while oil<20:
        print(f"在加{20-oil}，就滿20公升選擇贈品 !")
        choose=int(input("請選擇 1.繼續加 2.不加了"))
        if choose==1:
             oil+=int(input("請問還要再加幾公升 "))         
        elif choose==2:
            print(f"已加 {oil} 公升")
            break
        
    if oil>=20:
        print("加滿 20 公升可以選擇贈品")
      
