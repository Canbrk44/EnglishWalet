import random
import sqlite3 as sql
from openpyxl import load_workbook
vt = sql.connect('englishwalet.db')
im = vt.cursor()
def main():
    print("Programı ilk defa çalıştırıyorsanız bölüm ekleyerek başlıyabilirsiniz.")

if __name__ == "__main__":
    main()
def kelimeekle():
    while True:
        tables_query = "SELECT name FROM sqlite_master WHERE type='table';"
        cursor = vt.cursor()
        cursor.execute(tables_query)
        tables = cursor.fetchall()
        table_names = [table[0] for table in tables]
        print("Bölümler:")
        bölümler = []
        for table_name in table_names:
            bölümler.append(table_name)
        for i in bölümler:
            print(i)

        bölüm = input("Hangi Bölüme Kelime Girmek istiyorsunuz?: ")
        bölüm = bölüm.lower()
        if bölüm == "q":
            break
        if bölüm in bölümler:
            en = input("İngilizce Kelime Giriniz: ")
            tr = input("Türkçe Kelime Giriniz: ")
            en = en.lower()
            tr = tr.lower()
            kelime_gir = f"INSERT INTO {bölüm} VALUES ('{en}', '{tr}')"
            vt.execute(kelime_gir)
            vt.commit()
            print("Kelime Başarıyla Eklenmiştir.")
        else:
            print("Hatalı Bölüm Adı")
def bölümekle():
    bölüm_adi = input("Bölüm Adını Giriniz: ")
    bölüm_adi = bölüm_adi.replace(" ", "_").lower()
    im.execute(f"CREATE TABLE IF NOT EXISTS {bölüm_adi} (ingilizce, türkce)")
    vt.commit()
    print("Bölüm Oluşturuldu")
def kelimeoyunu():
    tables_query = "SELECT name FROM sqlite_master WHERE type='table';"
    cursor = vt.cursor()
    cursor.execute(tables_query)
    tables = cursor.fetchall()
    table_names = [table[0] for table in tables]
    print("Bölümler:")
    for table_name in table_names:
        print(table_name.title())
    bölüm_qry = input("Bölüm Seçiniz: ")
    bölüm_qry = bölüm_qry.lower()

    sorulan_sorular = []  # Sorulan soruları takip etmek için boş bir liste oluşturun

    while True:
        im.execute(f"SELECT * FROM {bölüm_qry} ORDER BY RANDOM() LIMIT 1")
        kelime = im.fetchone()
        if kelime:
            en = kelime[0]  # İngilizce kelime
            tr = kelime[1]  # Türkçe kelime

            # Eğer soru daha önce sorulduysa, bir sonraki soruya geç
            if en in sorulan_sorular:
                continue

            print("Sorunuz: ", en.title())
            cevap = input("Cevap: ")
            cevap = cevap.lower()

            if cevap == "q":
                break

            if cevap == tr:
                print("Doğru Cevap")
            else:
                print("Yanlış Cevap")

            sorulan_sorular.append(en)  # Sorulan soruyu listeye ekle
        else:
            print("Bu Bölümde kelime bulunamadı.")


def k_listele():
    tables_query = "SELECT name FROM sqlite_master WHERE type='table';"
    cursor = vt.cursor()
    cursor.execute(tables_query)
    tables = cursor.fetchall()
    table_names = [table[0] for table in tables]
    print("Bölümler:")
    for table_name in table_names:
        print(table_name.title())
    bölüm_qry = input("Listelemek istediğiniz bölümü seçiniz: ")
    im.execute(f"SELECT * FROM {bölüm_qry}")
    kelimeler = im.fetchall()

    if kelimeler:
        print(f"{bölüm_qry.title()} Bölümündeki Kelimeler:")
        for kelime in kelimeler:
            en = kelime[0]  # İngilizce kelime
            tr = kelime[1]  # Türkçe kelime
            print(f"EN: {en.title()} >> TR: {tr.title()}")
    else:
        print("Bu bölümde kelime bulunamadı.")

while True:
    print("")
    print("1-Kelime Listele | 2-Kelime Oyunu | 3-Kelime Ekle  | 4-Bölüm Ekle |  q-"
          "Çıkış")
    print("*" * 70)

    islem = input("Kararınız: ")
    if islem == "q":
        print("Programdan Çıkılıyor")
        exit()
    if islem == "1":
        k_listele()
    elif islem == "2":
        kelimeoyunu()
    elif islem == "3":
        kelimeekle()
    elif islem == "4":
        bölümekle()

vt.close()