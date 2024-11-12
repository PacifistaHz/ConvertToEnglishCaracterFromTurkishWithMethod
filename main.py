def turkceKarakterDonustur1():
    eski="şçöğüıŞÇÖĞÜİ"
    yeni="scoguiSCOGUI"
    cevirTablosu=str.maketrans(eski,yeni)
    metin="Öğrenmek İçin Python"
    print(metin.translate(cevirTablosu))

def turkceKarakterDonustur2(metin):
    eski = "şçöğüıŞÇÖĞÜİ"
    yeni = "scoguiSCOGUI"
    cevirTablosu = str.maketrans(eski, yeni)
    print(metin.translate(cevirTablosu))

def turkceKarakterDonustur3(metin):
    eski = "şçöğüıŞÇÖĞÜİ"
    yeni = "scoguiSCOGUI"
    cevirTablosu = str.maketrans(eski, yeni)
    return metin.translate(cevirTablosu)

def turkceKarakterDonustur4(metin):
    eski = "şçöğüıŞÇÖĞÜİ"
    yeni = "scoguiSCOGUI"
    for i in range(0,len(eski)):
        metin = metin.replace(eski[i],yeni[i])
    return metin

turkceKarakterDonustur1()
turkceKarakterDonustur2("Öğrenmek İçin Python")
print(turkceKarakterDonustur3("Öğrenmek İçin Python"))
print(turkceKarakterDonustur4("Öğrenmek İçin Python"))
