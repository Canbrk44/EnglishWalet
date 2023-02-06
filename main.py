import random
from openpyxl import load_workbook
def cumleekle():
    wb = load_workbook("Cümleler.xlsx")
    ws = wb.active
    words = {}
    for i in range(2, ws.max_row + 1):
        en = ws["A{}".format(i)].value
        tr = ws["B{}".format(i)].value
        words[en] = tr
    sayac = 1
    for _ in words:
        sayac = sayac + 1
    print("Toplam Cümle Sayısı: {}".format(sayac))
    ing = input("Ingilizce Cümle Giriniz: ")
    tr = input("Türkçe Karşılığını Giriniz: ")
    ws.append([ing, tr])
    wb.save("Cümleler.xlsx")
    print("{}-{}".format(ing, tr))
    print("Cümleniz Başarıyla Eklenmiştir")
    wb.close()
def kelimeekle():
    wb = load_workbook("Words.xlsx")
    ws = wb.active
    words = {}
    for i in range(2, ws.max_row + 1):
        en = ws["A{}".format(i)].value
        tr = ws["B{}".format(i)].value
        words[en] = tr
    sayac = 1
    for _ in words:
        sayac = sayac + 1
    print(f"Toplam Kelime Sayısı: {sayac}")
    ing = input("Ingilizce Kelime Giriniz: ")
    tr = input("Türkçe Karşılığını Giriniz: ")
    ws.append([ing, tr])
    wb.save("Words.xlsx")
    print("{}-{}".format(ing,tr))
    print("Kelimeniz Başarıyla Eklenmiştir")
    wb.close()
def c_listele():
    wb = load_workbook("Cümleler.xlsx")
    ws = wb.active
    for satir in range(2, ws.max_row + 1):
        for sutun in range(1, ws.max_column + 1):
            print(" | " + str(ws.cell(satir, sutun).value) + " | ", end="")
        print()
def Cumle():
    wb = load_workbook("Cümleler.xlsx")
    ws = wb.active
    words = {}
    for i in range(2, ws.max_row + 1):
        en = ws["A{}".format(i)].value
        tr = ws["B{}".format(i)].value
        words[en] = tr
    puan = 0
    while True:
        c, b = random.choice(list(words.items()))
        print("Sorunuz: {}".format(c))
        uppers = str(b)
        cevap = input("Cevabı Giriniz: ")
        if cevap == "q":
            break
        if cevap.title() == uppers.title():
            puan = puan + 5
            print("-------------")
            print("Tebrikler Doğru Cevap !!!", "Puanınız: {}".format(puan))
            print("-------------")

        else:
            puan = puan - 5
            print("Yanlıs Cevap", "Puanınız: {}".format(puan))
            print("-------------")
            print("Doğrusu: {}".format(b))
            print("-------------")
    print("Oyun Bitti. Puanınız {}".format(puan))
def KelimeTr():
    wb = load_workbook("Words.xlsx")
    ws = wb.active
    words = {}
    for i in range(2, ws.max_row + 1):
        en = ws["A{}".format(i)].value
        tr = ws["B{}".format(i)].value
        words[en] = tr
    puan = 0
    statusTrue = {}
    statusFalse = {}
    while True:
        c, b = random.choice(list(words.items()))
        print("Sorunuz: {}".format(b))
        uppers = str(c)
        for i in uppers:
            print(i, end="")
            break
        uz = len(uppers)
        for i in range(uz-2):
            print("*", end="")
        print(uppers[-1])
        print()
        cevap = input("Cevabı Giriniz: ")
        if cevap == "q":
            break
        if cevap.title() == uppers.title():
            statusTrue[b] = uppers
            puan = puan + 5
            print("-------------")
            print("Tebrikler Doğru Cevap !!!", "Puanınız: {}".format(puan))
            print("-------------")
        else:
            statusFalse[b] = uppers
            puan = puan - 5
            print("Yanlıs Cevap", "Puanınız: {}".format(puan))
            print("-------------")
            print("Doğrusu: {}".format(c))
            print("-------------")
    print("Oyun Bitti. Puanınız {}".format(puan))

    # for dogru in statusTrue.items():
    #     print(f"Doğru cevaplarınız: {dogru}",end="|")
    #     for yanlis in statusFalse.items():
    #         print(f"Yanlis Cevaplarınız: {yanlis}")
    print("Sonuclar: 1-Doğru Cevaplarım | 2-Yanlıs Cevaplarım")
    myStat = int(input("Seçiminiz: "))
    if myStat == 1:
        for i in statusTrue.items():
            print("Doğru Cevaplarınız {}".format(str(i)))
    elif myStat == 2:
        for i in statusFalse.items():
            print("Yanlış Cevaplarınız {}".format(str(i)))
    else:
        print("Hatalı Bir Seçim Yaptınız")
def KelimeEn():
    wb = load_workbook("Words.xlsx")
    ws = wb.active
    words = {}
    for i in range(2, ws.max_row + 1):
        en = ws["A{}".format(i)].value
        tr = ws["B{}".format(i)].value
        words[en] = tr
    puan = 0
    statusTrue = {}
    statusFalse = {}
    while True:
        c, b = random.choice(list(words.items()))
        print("Sorunuz: {}".format(c))
        uppers = str(b)
        for i in uppers:
            print(i,end="")
            break
        uz = len(uppers)
        for i in range(uz-2):
            print("*",end="")
        print(uppers[-1])
        print()
        cevap = input("Cevabı Giriniz: ")
        if cevap == "q":
            break
        if cevap.title() == uppers.title():
            statusTrue[c] = uppers
            puan = puan + 5
            print("-------------")
            print("Tebrikler Doğru Cevap !!!", "Puanınız: {}".format(puan))
            print("-------------")
        else:
            statusFalse[c] = uppers
            puan = puan - 5
            print("Yanlıs Cevap", "Puanınız: {}".format(puan))
            print("-------------")
            print("Doğrusu: {}".format(b))
            print("-------------")
    print("Oyun Bitti. Puanınız {}".format(puan))

    # for dogru in statusTrue.items():
    #     print(f"Doğru cevaplarınız: {dogru}",end="|")
    #     for yanlis in statusFalse.items():
    #         print(f"Yanlis Cevaplarınız: {yanlis}")
    print("Sonuclar: 1-Doğru Cevaplarım | 2-Yanlıs Cevaplarım")
    myStat = int(input("Seçiminiz: "))
    if myStat == 1:
        for i in statusTrue.items():
            print("Doğru Cevaplarınız {}".format(str(i)))
    elif myStat == 2:
        for i in statusFalse.items():
            print("Yanlış Cevaplarınız {}".format(str(i)))
    else:
        print("Hatalı Bir Seçim Yaptınız")
def k_listele():
    wb = load_workbook("Words.xlsx")
    ws = wb.active
    for satir in range(2, ws.max_row + 1):
        for sutun in range(1, ws.max_column + 1):
            print(" | " + str(ws.cell(satir, sutun).value) + " | ", end="")
        print()
while True:
    print("1-Kelime Listele | 2-Kelime Oyunu | 3-Cümle Listele | 4-Cümle Oyunu | 5-Kelime Ekle | 6-Cümle Ekle |  q-"
          "Çıkış")
    print("*" * 70)

    islem = input("Kararınız: ")
    if islem == "q":
        print("Programdan Çıkılıyor")
        exit()
    if islem == "1":
        k_listele()
    elif islem == "2":
        islem2 = input("Türkçe Çeviri / İngilizce Çeviri - (Tr)(En) ")
        Sens = islem2.title()
        if Sens == "En":
            KelimeEn()
        else:
            KelimeTr()
    elif islem == "3":
        c_listele()
    elif islem == "4":
        Cumle()
    elif islem == "5":
        kelimeekle()
    elif islem == "6":
        cumleekle()
