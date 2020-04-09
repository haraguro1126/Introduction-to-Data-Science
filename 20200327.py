#將目前的攝氏氣溫轉換為華氏氣溫 25
current_celsius = 25
current_fahrenheit = current_celsius*9/5+32
print(current_fahrenheit)
#將目前的華氏氣溫轉換為攝氏氣溫
current_fahrenheit = 77
current_celsius = (current_fahrenheit-32)*5/9
print(current_celsius)
#2-29 計算俠客歐尼爾巔峰時期的 BMI 身體質量指數
shaq_height = 216
shaq_weight = 147
shaq_bmi = shaq_weight / (shaq_height/100)**2
print(shaq_bmi)
#P2-42 ：What did Ross say?
ross_said = "Let's put aside the fact that you \"accidentally\" pick up my grandmother's ring"
print(ross_said)
#P2-50 讓使用者輸入城市名稱與天氣，並印出「我在OOO，天氣OOO」
city = input("地點")
weather = input("天氣")
print(city)
print(weather)
print("我在{}，天氣{}".format(city, weather))
#P2-68 球員 BMI 與過重判斷
player_name = Shaquille O’Neal
shaq_height = 216
shaq_weight = 147
shaq_bmi = shaq_weight / (shaq_height/100)**2
print("{}的身體質量指數為：{:.2f}".format(player_name, shaq_bmi))
print("{}是否過重：{}".format(player_name, shaq_bmi > 30))