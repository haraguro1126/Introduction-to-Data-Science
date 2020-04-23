#隋堂1
monthly_income = input("請輸入月薪：")
saving_account = input("請輸入存款：")
monthly_income = int(monthly_income)
saving_account = int(saving_account)
print(type(monthly_income))
print(type(saving_account))
ans = ""
# 條件判斷(begin)
if monthly_income > 40000 or saving_account > 500000:
    ans = "發信用卡"
# 條件判斷(end)
print(ans)
#隨堂2
id_last_digit = input("請輸入身分證字號的尾數：")
id_last_digit = int(id_last_digit)
if id_last_digit % 2 == 0:
    ans = "星期二四六日領"
else:
    ans = "星期一三五日領"
print(ans)
#隨堂3
input_height = float(input("請輸入身高（公分）："))
input_weight = float(input("請輸入體重（公斤）："))
bmi = input_weight / (input_height*0.01)**2
if bmi > 30:
    label = "Obese"
elif bmi > 25:
    label = "Overweight"
elif bmi > 18.5:
    label = "Normal weight"
elif bmi <= 18.5:
    label = "Underweight"
print(label)