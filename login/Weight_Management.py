def run_health(name):
    health=80
    goal=75
    weight=eval(input(f"{name}請輸入您的體重 :"))
    if weight<=health:
        if weight<=goal:
            print("恭喜你達到理想體重")
        else:
            print("恭喜你到目標體重")
    else:
        print(f"{name} 在努力一下\n,還差{weight-goal} 公斤達到目標體重\n 還差{weight-health} 公斤達到理想體重")
        