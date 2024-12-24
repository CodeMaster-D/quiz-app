nama = ""
umur = 0
kelas = ""
skor = 0

while True:
    print("")
    print("")
    print("")
    print("===================================")
    print("  HALO SELAMAT DATANG DI QUIZ APP  ")
    print("===================================")
    print("")
    while True:
        print("======= MENU ========")
        print("1. Profil")
        print("2. Mulai Quiz")
        print("3. Keluar")
        pilihan = int(input("Pilih menu (1/2/3): "))

        if pilihan == 1:
            if nama == "":
                print("")
                print("Halo Pengguna baru, isi biodata dulu yuk!")
                print("")
                nama = str(input("Siapa nama kamu: "))
                umur = int(input("Berapa umur kamu: "))
                kelas = str(input("Kamu kelas berapa sekarang: "))
                print("Skor kamu masih 0, ayo selesaikan kuis sekarang dan dapatkan skor tertinggi")
                print("Biodata tersimpan.")
            else:
                print("Profil Anda:")
                print("Nama:", nama)
                print("Umur:", umur)
                print("Kelas:", kelas)
                print("Skor tertinggi:", skor)
        elif pilihan == 2:
            break
        else:
            exit()

    print("Pilih kategori untuk mulai quiz:")
    print("1. Umum")
    print("2. Matematika")
    print("3. Bahasa Inggris")
    kategori = int(input("Masukkan pilihan kategori (1/2/3): "))
    print("")

    if kategori == 1:
        print("===== Selamat datang di quiz Umum =====")
        print("")
        soal1 = str(input("1. Apa ibukota Indonesia: "))
        if soal1.lower() == "jakarta":
            skor += 1

        soal2 = str(input("2. Siapa presiden pertama di Indonesia: "))
        if soal2.lower() in ["soekarno", "dr. soekarno", "sukarno"]:
            skor += 1

        soal3 = str(input("3. Apa bahasa inggrisnya meja: "))
        if soal3.lower() == "table":
            skor += 1

        soal4 = str(input("4. Kapan Indonesia merdeka: "))
        if soal4 == "17 agustus 1945":
            skor += 1

        soal5 = str(input("5. Siapa presiden pengkorupsi handal di Indonesia: "))
        if soal5.lower() == "megawati":
            skor += 1

    elif kategori == 2:
        print("===== Selamat datang di quiz Matematika =====")
        print("")
        soal1 = str(input("1. Berapa hasil dari 2 + 2: "))
        if soal1 == "4":
            skor += 1

        soal2 = str(input("2. Berapa hasil dari 5 * 5: "))
        if soal2 == "25":
            skor += 1

        soal3 = str(input("3. Berapa hasil dari 10 / 2: "))
        if soal3 == "5":
            skor += 1

        soal4 = str(input("4. Berapa hasil dari 9 - 3: "))
        if soal4 == "6":
            skor += 1

        soal5 = str(input("5. Berapa hasil dari 7 + 8: "))
        if soal5 == "15":
            skor += 1

    elif kategori == 3:
        print("===== Selamat datang di quiz Bahasa Inggris =====")
        print("")
        soal1 = str(input("1. Apa bahasa Inggrisnya 'buku': "))
        if soal1.lower() == "book":
            skor += 1

        soal2 = str(input("2. Apa bahasa Inggrisnya 'apel': "))
        if soal2.lower() == "apple":
            skor += 1

        soal3 = str(input("3. Apa bahasa Inggrisnya 'kucing': "))
        if soal3.lower() == "cat":
            skor += 1

        soal4 = str(input("4. Apa bahasa Inggrisnya 'anjing': "))
        if soal4.lower() == "dog":
            skor += 1

        soal5 = str(input("5. Apa bahasa Inggrisnya 'rumah': "))
        if soal5.lower() == "house":
            skor += 1

    else:
        print("Pilihan kategori tidak valid. Program akan keluar.")
        exit()

    print("Skor anda adalah:", skor)

    if skor >= 5:
        nilai = 100
    elif skor >= 4:
        nilai = 80
    elif skor >= 3:
        nilai = 60
    else:
        nilai = 40

    print("Nilai anda adalah:", nilai)

