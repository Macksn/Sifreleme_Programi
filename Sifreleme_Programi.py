# -*- coding: utf-8 -*-
"""Sifreleme.ipynb adlı not defterinin kopyası

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1WHW2KaHjm1YUTEO2rgThF6LDQBf6v3dh
"""

def hill_sifreleme(metin, matris):
    """Hill şifrelemesi yapar."""
    sifreli_metin = ""
    matris_inverse = None

    # Matrisin tersini hesapla
    try:
        matris_inverse = matris_tersi_hesapla(matris)
    except ValueError as e:
        print(e)
        return ""

    for i in range(0, len(metin), 2):
        if i + 1 < len(metin):
            harf1 = metin[i]
            harf2 = metin[i + 1]

            if harf1.isalpha() and harf2.isalpha():
                ascii_ofset = ord('a') if harf1.islower() else ord('A')
                matris_carpim = [
                    [(ord(harf1) - ascii_ofset) * j + (ord(harf2) - ascii_ofset) * k for j in range(2)]
                    for k in range(2)
                ]

                # Ters matris ile çarp
                sonuc = [
                    sum([matris_inverse[i][j] * matris_carpim[j][k] for j in range(2)]) % 26
                    for k in range(2)
                ]

                # Sonucu harfe dönüştür ve birleştir
                sifreli_metin += chr(sonuc[0] + ascii_ofset) + chr(sonuc[1] + ascii_ofset)
            else:
                sifreli_metin += harf1 + harf2
        else:
            break

    return sifreli_metin

def matris_tersi_hesapla(matris):
    """Matrisin tersini hesaplar."""
    matris_determinant = matris[0][0] * matris[1][1] - matris[0][1] * matris[1][0]

    if matris_determinant == 0:
        raise ValueError("Matrisin tersi bulunamadı.")

    matris_inverse = [
        [matris[1][1] / matris_determinant, -matris[0][1] / matris_determinant],
        [-matris[1][0] / matris_determinant, matris[0][0] / matris_determinant]
    ]

    return matris_inverse

def hill_cozme(sifreli_metin, matris):
    """Hill şifresini çözer."""
    return hill_sifreleme(sifreli_metin, matris_tersi_hesapla(matris))

def ana_program():
    """Ana program fonksiyonu."""
    print("ŞİFRELEME")
    print("Hangi tür şifreleme methodunu kullanmak istediğinizi seçiniz.")
    print("1.Caesar Şifreleme")
    print("2.Base64 Şifreleme")
    print("3.Vernam Şifreleme")
    print("4.Hill Şifreleme")
    seçim = int(input("Seçiminiz: "))

    if seçim == 1:
        metin = input("Şifrelenecek metin: ")
        kaydirma = int(input("Kaydırma değeri: "))
        sifreli_metin = caesar_sifreleme(metin, kaydirma)
        print("Şifrelenmiş metin: ", sifreli_metin)

        cozulen_metin = caesar_cozme(sifreli_metin, kaydirma)
        print("Şifresi çözülmüş metin: ", cozulen_metin)
    elif seçim == 2:
        metin = input("Şifrelenecek metin: ")
        sifreli_metin = base64_sifreleme(metin)
        print("Şifrelenmiş metin: ", sifreli_metin)

        cozulen_metin = base64_cozme(sifreli_metin)
        print("Şifresi çözülmüş metin: ", cozulen_metin)
    elif seçim == 3:
        metin = input("Şifrelenecek metin: ")
        anahtar = input("Anahtar: ")
        sifreli_metin = vernam_sifreleme(metin, anahtar)
        print("Şifrelenmiş metin: ", sifreli_metin)

        cozulen_metin = vernam_cozme(sifreli_metin, anahtar)
        print("Şifresi çözülmüş metin: ", cozulen_metin)
    elif seçim == 4:
        metin = input("Şifrelenecek metin: ")
        matris = [[int(input("Matris[0][0]: ")), int(input("Matris[0][1]: "))],
                   [int(input("Matris[1][0]: ")), int(input("Matris[1][1]: "))]]

        sifreli_metin = hill_sifreleme(metin, matris)
        print("Şifrelenmiş metin: ", sifreli_metin)

        cozulen_metin = hill_cozme(sifreli_metin, matris)
        print("Şifresi çözülmüş metin: ", cozulen_metin)
    else:
        print("Geçersiz seçim.")

ana_program()