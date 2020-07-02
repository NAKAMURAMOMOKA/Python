debit = int(250000)
rate = float(14)
repayment =  int(30000)
total = 0
month = 0
while debit > repayment :
    month += 1
    debit = debit * (1 + rate/12/100) - repayment
    print(str(month)+"月: 返済額=",repayment,"円","残り",\
    float(debit),format(" "))
    total += repayment
total += debit
print(str(month)+"月: 返済額=",float(debit),"円","返済完了")
