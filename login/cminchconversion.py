def run_cminch():
    c=int(input("輸入 1.公分 2.英寸 :"))
    lenght=int(input("請輸入長度 : "))

    print("|cm   |m    |ich  |foot |yd   |")
    print("|     |     |     |     |     |")

    if c==1:
        print("|",end="")
        print(f"{str(lenght):<5.5s}",end="|")
        print(f"{str(lenght*0.01):<5.5s}",end="|")
        print(f"{str(lenght*0.394):<5.5s}",end="|")
        print(f"{str(lenght*0.03281):<5.5s}",end="|")
        print(f"{str(lenght*0.01094):<5.5s}",end="|")
    else:
        print("|",end="")
        print(f"{str(lenght*2.54):<5.5s}",end="|")
        print(f"{str(lenght*0.0254):<5.5s}",end="|")
        print(f"{str(lenght):<5.5s}",end="|")
        print(f"{str(lenght/12):<5.5s}",end="|")
        print(f"{str(lenght/36):<5.5s}",end="|")
    print()