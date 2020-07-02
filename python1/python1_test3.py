print("身長と体重を入力してください。")
print("身長は？(mで入力してください。)")
height=float(input())
print("体重は？")
weight=float(input())
bmi =  ((weight / ( height * height )))
if bmi < 18.5:
  print("あなたは「やせ」です。") 
elif (bmi >= 18.5) and (bmi < 25):
  print("あなたは「標準」です。")
elif (bmi >= 25) and (bmi < 30):
  print("あなたは「肥満」です。")
elif 30 < bmi:
  print("あなたは「高度肥満」です。")

