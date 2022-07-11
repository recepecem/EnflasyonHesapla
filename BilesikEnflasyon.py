#variables and print statements are written in Turkish language

dosya = open("enflasyonOranlari.txt", "r")
temp1 = []
temp2 = []
tarih = []
veriler = []

for i in dosya.read().splitlines():
    temp1.append(i)
for i in temp1:
    temp2.append(i.split("\t"))

for i in range(0, len(temp1)):
    tarih.append(temp2[i][0])
    veriler.append(temp2[i][1])
    veriler.append(temp2[i][2])

while True:
    print(temp2[len(temp2)-1][0]," ile ",temp2[0][0], " tarihleri arasında çalışır!")
    print("örnek: 05-2005\n")
    b_yil = input("başlangıç yılı: ")
    s_yil = input("bitiş yılı: ")
    iVal = float(input("anapara: "))
    tIval = iVal
    b_index = tarih.index(b_yil)
    s_index = tarih.index(s_yil)

    if b_index < s_index:
        print("başlangıç tarihi bitiş tarihinden sonra olamaz.")
        continue

    #iVal = 100.0
    tmp = .1
    adder = .0

    FixedRange = int((b_index - s_index) / 12)

    for i in range(0, FixedRange+1):
        #print(temp2[b_index - (12*i)])
        tmp = float(veriler[2 * (b_index - (12*i))])
        adder = iVal + ((iVal * tmp) / 100)
        iVal = adder

    print("\n[",temp2[b_index][0],"] tarihinde ki ",tIval," liraniz [",temp2[s_index][0],"] tarihinde ",adder,"lira olmuştur.\n" )
