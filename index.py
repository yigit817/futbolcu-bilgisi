class DunyaKupasi2026:
    def __init__(self):
        self.ev_sahipleri = ["Amerika Birleşik Devletleri", "Meksika", "Kanada"]
        self.takim_sayisi = 48
        self.tarih = "11 Haziran - 19 Temmuz 2026"
        self.final_stadyumu = "MetLife Stadium (New York/New Jersey)"
        self.sampiyon = "Arjantin"
        self.ikinci = "Fransa"
        self.skor = "2 - 1"
        self.futbolcular = []

    def turnuva_ozeti(self):
        print("==================================================")
        print("          2026 FIFA DÜNYA KUPASI RAPORU          ")
        print("==================================================")
        print(f"Ev Sahipleri    : {', '.join(self.ev_sahipleri)}")
        print(f"Format          : {self.takim_sayisi} Takım (İlk kez uygulandı)")
        print(f"Dönem           : {self.tarih}")
        print(f"Final Stadyumu  : {self.final_stadyumu}")
        print("--------------------------------------------------")
        print(f"ŞAMPİYON        : {self.sampiyon} 🏆")
        print(f"Finalist        : {self.ikinci}")
        print(f"Final Skoru     : {self.skor}")
        print("==================================================\n")

    def oyuncu_ekle(self, oyuncu):
        self.futbolcular.append(oyuncu)

    def turnuva_karmasini_listele(self):
        print("🏆 TURNUVAYA DAMGA VURAN OYUNCULAR VE KALECİLER 🏆\n")
        for oyuncu in self.futbolcular:
            oyuncu.bilgi_yazdir()
            print("-" * 50)


class Futbolcu:
    def __init__(self, isim, ülke, yas, pozisyon, takim, turnuva_istatistigi):
        self.isim = isim
        self.ülke = ülke
        self.yas = yas
        self.pozisyon = pozisyon
        self.takim = takim
        self.turnuva_istatistigi = turnuva_istatistigi

    def bilgi_yazdir(self):
        print(f"Oyuncu     : {self.isim} ({self.ülke})")
        print(f"Yaş/Kulüp  : {self.yas} Yaş | {self.takim}")
        print(f"Pozisyon   : {self.pozisyon}")
        print(f"Performans : {self.turnuva_istatistigi}")


class Kaleci(Futbolcu):
    def __init__(self, isim, ülke, yas, takim, turnuva_istatistigi, kurtarilan_penalti):
        super().__init__(isim, ülke, yas, "Kaleci", takim, turnuva_istatistigi)
        self.kurtarilan_penalti = kurtarilan_penalti

    def bilgi_yazdir(self):
        super().bilgi_yazdir()
        print(f"Kaleci Özel: {self.kurtarilan_penalti}")


# --- VERİLERİN YÜKLENMESİ VE PROGRAMIN ÇALIŞTIRILMASI ---
if __name__ == "__main__":
    # Turnuva nesnesini oluştur ve özeti yazdır
    kupa = DunyaKupasi2026()
    kupa.turnuva_ozeti()

    # 2026 Dünya Kupası'nda Öne Çıkan Futbolcular
    oyuncu1 = Futbolcu("Lionel Messi", "Arjantin", 39, "Oyun Kurucu / Forvet", "Inter Miami", "Turnuvanın en iyi oyuncusu seçildi, finalde galibiyet golünü attı.")
    oyuncu2 = Futbolcu("Kylian Mbappé", "Fransa", 27, "Sol Kanat / Forvet", "Real Madrid", "7 golle turnuvanın gol kralı (Altın Ayakkabı) oldu.")
    oyuncu3 = Futbolcu("Lamine Yamal", "İspanya", 19, "Sağ Kanat", "FC Barcelona", "Turnuvanın En İyi Genç Oyuncusu ödülünü aldı, 5 asist yaptı.")
    oyuncu4 = Futbolcu("Erling Haaland", "Norveç", 25, "Santrafor", "Manchester City", "Norveç'i çeyrek finale kadar taşıdı, 5 gol attı.")
    oyuncu5 = Futbolcu("Christian Pulisic", "ABD", 27, "Kanat Forvet", "AC Milan", "Ev sahibi ABD'yi son 16 turuna taşıyan lider performansı sergiledi.")

    # 2026 Dünya Kupası'nda Öne Çıkan Kaleciler
    kaleci1 = Kaleci("Emiliano Martínez", "Arjantin", 33, "Aston Villa", "Turnuvanın En İyi Kalecisi (Altın Eldiven) ödülünü kazandı.", "Çeyrek finalde seri penaltılarda 2 penaltı kurtardı.")
    kaleci2 = Kaleci("Mike Maignan", "Fransa", 31, "AC Milan", "Turnuva boyunca kalesinde sadece 4 gol gördü, geçit vermez bir performans sergiledi.", "Grup aşamasında 1 penaltı kurtardı.")
    kaleci3 = Kaleci("Patrick Pentz", "Avusturya", 29, "Brøndby", "Turnuvanın sürpriz takımı Avusturya'nın devleşen ismi oldu.", "Son 16 turunda kritik kurtarışlara imza attı.")

    # Oyuncuları turnuva sistemine dahil et
    kupa.oyuncu_ekle(oyuncu1)
    kupa.oyuncu_ekle(oyuncu2)
    kupa.oyuncu_ekle(oyuncu3)
    kupa.oyuncu_ekle(oyuncu4)
    kupa.oyuncu_ekle(oyuncu5)
    kupa.oyuncu_ekle(kaleci1)
    kupa.oyuncu_ekle(kaleci2)
    kupa.oyuncu_ekle(kaleci3)

    # Kadroyu raporla
    kupa.turnuva_karmasini_listele()