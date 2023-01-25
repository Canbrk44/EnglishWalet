import random
from openpyxl import Workbook,load_workbook
print("""
İngilizce Kelime Oyununa Hoş Geldiniz
Yarışma Boyunca 5 Hakkınız Bulunmaktadır 
Her Doğru Cevap Hanenize 2 Puan Kazandıracaktır

Yapmak İstediğiniz İşlemi Giriniz
1- Bütün Kelimeleri Gözden Geçir
2- Kelime Oyunu
3- Kalıp Cümleleri Listele
4- Cümle Oyunu

""")
def c_listele():
    wb = load_workbook("Cümleler.xlsx")
    ws = wb.active
    for satir in range(2,ws.max_row+1):
        for sutun in range(1,ws.max_column+1):
            print(" | "+str(ws.cell(satir,sutun).value) + " | ",end="")
        print()

def Cümle():
    wb = load_workbook("Cümleler.xlsx")
    ws = wb.active
    words = {}
    for i in range(2,ws.max_row+1):
        en = ws["A{}".format(i)].value
        tr = ws["B{}".format(i)].value
        words[en] = tr
    Hak = 5
    puan = 0
    while Hak>0:
        c, b = random.choice(list(words.items()))
        print("Sorunuz: {}".format(c))
        cevap = input("Cevabı Giriniz: ")
        if cevap == "q":
            break
        a = cevap.title()
        if a == b:
            puan = puan + 2
            print("*************")
            print("Tebrikler Doğru Cevap !!!")
            print("*************")
            print("Puanınız: {}".format(puan))
            print("*************")

        else:
            print("Yanlıs Cevap")
            print("*************")
            Hak = Hak - 1
            print("Kalan Hakkınız : {}".format(Hak))
            print("*************")
            print("Doğrusu: {}".format(b))
            print("*************")
    print("Oyun Bitti. Puanınız {}".format(puan))
def KelimeTr():
    wb = load_workbook("Words.xlsx")
    ws = wb.active
    words = {}
    for i in range(2,ws.max_row+1):
        en = ws["A{}".format(i)].value
        tr = ws["B{}".format(i)].value
        words[en] = tr
    Hak = 5
    puan = 0
    while Hak>0:
        c, b = random.choice(list(words.items()))
        print("Sorunuz: {}".format(b))
        cevap = input("Cevabı Giriniz: ")
        if cevap == "q":
            break
        a = cevap.title()
        if a == c:
            puan = puan + 2
            print("*************")
            print("Tebrikler Doğru Cevap !!!")
            print("*************")
            print("Puanınız: {}".format(puan))
            print("*************")

        else:
            print("Yanlıs Cevap")
            print("*************")
            Hak = Hak - 1
            print("Kalan Hakkınız : {}".format(Hak))
            print("*************")
            print("Doğrusu: {}".format(c))
            print("*************")
    print("Oyun Bitti. Puanınız {}".format(puan))
def KelimeEn():
    wb = load_workbook("Words.xlsx")
    ws = wb.active
    words = {}
    for i in range(2,ws.max_row+1):
        en = ws["A{}".format(i)].value
        tr = ws["B{}".format(i)].value
        words[en] = tr
    Hak = 5
    puan = 0
    while Hak>0:
        c, b = random.choice(list(words.items()))
        print("Sorunuz: {}".format(c))
        cevap = input("Cevabı Giriniz: ")
        if cevap == "q":
            break
        a = cevap.title()


        if a == b:
            puan = puan + 2
            print("*************")
            print("Tebrikler Doğru Cevap !!!")
            print("*************")
            print("Puanınız: {}".format(puan))
            print("*************")

        else:
            print("Yanlıs Cevap")
            print("*************")
            Hak = Hak - 1
            print("Kalan Hakkınız : {}".format(Hak))
            print("*************")
            print("Doğrusu: {}".format(b))
            print("*************")
    print("Oyun Bitti. Puanınız {}".format(puan))

def k_listele():
    wb = load_workbook("Words.xlsx")
    ws = wb.active
    for satir in range(2,ws.max_row+1):
        for sutun in range(1,ws.max_column+1):
            print(" | "+str(ws.cell(satir,sutun).value) + " | ",end="")

        print()
while True:
    islem = input("Kararınız: ")
    if islem == "1":
        k_listele()
    elif islem == "2":
        islem2=input("Türkçe Çeviri / İngilizce Çeviri - (Tr)(En) ")
        Sens= islem2.title()
        if Sens == "En":
            KelimeEn()
        else:
            KelimeTr()
    elif islem == "3":
        c_listele()
    elif islem == "4":
        Cümle()








