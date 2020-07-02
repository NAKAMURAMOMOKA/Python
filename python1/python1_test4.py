shakkin = float(input("借金:" ))
nennri = float(input("年利率(%): "))
hensai =  int(input("返済額: " ))
total = 0
month = 0
while shakkin > hensai :
    month += 1
    shakkin = shakkin*(1 + nennri/14/100) - hensai
    print(str(month)+"月: 返済額",hensai,"円","残り",\
    float(shakkin),format(" "))
    total += hensai
month += 1
shakkin = shakkin*(1 + nennri/14/100)
total += shakkin
print(str(month)+"月: 返済額",float(shakkin),"円","これで完済。","返済総額: ",\
int(total),"円",format(" "))