def run_tem():
    c=eval(input("請輸入攝氏 C\n"))
    f=9/5*c+32
    print(f"華氏 = {f:.3f}度F")
    print("===============")
    f=eval(input("請輸入華氏 F\n"))
    c=(f-32)*5/9
    print(f"攝氏 = {c:.3f}度C")