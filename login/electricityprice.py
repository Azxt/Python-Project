def run_ele():    
    while True:
        try:
            num=float(input("請輸入用電度數(夏季) : (輸入0結束)"))
            
            if num==0:
                break
            output=0
            if num<=120:                         #電度數0~120，每度1.78
                output=num*1.78
            elif num>120 and num<=330:           #電度數121~330，每度2.55
                output=120*1.78+(num-120)*2.55
            elif num>330 and num<=500:           #電度數331~500，每度3.8
                output=120*1.78+210*2.55+(num-330)*3.8
            elif num>500 and num<=700:           #電度數501~700，每度5.14
                output=120*1.78+210*2.55+170*3.8+(num-500)*5.14
            elif num>700 and num<=1000:          #電度數701~1000，每度6.44
                output=120*1.78+210*2.55+170*3.8+200*5.14+(num-700)*6.44
            else:                                #電度數1000以上，每度8.86
                output=120*1.78+210*2.55+170*3.8+200*5.14+300*6.44+(num-1000)*8.86
            print(f'用電{num}度共{output:.2f}元')
            
        except:
            break
    
