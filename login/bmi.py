import math
def run_bmi(name):
    s1h=eval(input(f"請輸入{name}身高 CM:\n"))
    s1w=eval(input(f"請輸入{name}體重 KG:\n"))
    s1h=s1h/100
    bmi=s1w/pow(s1h,2)
    print(f"Hi~{name} 您的BMI為: {math.floor(bmi*100)/100}")
