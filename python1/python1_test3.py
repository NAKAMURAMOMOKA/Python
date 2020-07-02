print("身長と体重を入力してください。")
print("身長は？(mで入力してください。)")
height=float(input())
print("体重は？")
weight=float(input())
BMI =  ((weight/(height*height)))

print("BMIは",BMI)

if BMI < 18.5:
  print("やせ") 
elif (BMI >= 18.5) and (BMI < 25):
  print("標準") 
elif (BMI >= 25) and (BMI < 30):
  print("肥満")
elif 30 < BMI:
  print("高度肥満")

