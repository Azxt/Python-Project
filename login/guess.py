def run_guess():
    import random
    ans=random.randint(0,100)
    range_start=0
    range_end=100
    x=int(input("請輸入一個數字 "))
    while ans != x:
        if x>ans:
            range_end=x-1
            print(f"猜小一點，目前範圍{range_start}到{range_end}。")
        elif x<ans:
            range_start=x+1
            print("猜大一點")
            print(f"猜大一點，目前範圍{range_start}到{range_end}。")
        x=int(input(f"請輸入 {range_start}~{range_end} 的數字 "))
    else:
        print("猜中了 恭喜!!")