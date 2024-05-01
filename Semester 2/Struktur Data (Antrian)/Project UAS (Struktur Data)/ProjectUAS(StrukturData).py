# Bagian Library 
from gtts import gTTS
from playsound import playsound
import os
import time

#Class Queue 
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Antrian sudah kosong.")
            return None

    def size(self):
        return len(self.items)

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Antrian sudah kosong.")
            return None

class Queue1(Queue):
    pass

class Queue2(Queue):
    pass

class Queue3(Queue):
    pass

#pendefinisian antrian class 1 sampai 3
antrian1 = Queue1()
antrian2 = Queue2()
antrian3 = Queue3()
antrian1.append = []
antrian2.append = []
antrian3.append = []

#Fungsi Untuk Mengeluarkan Suaranya
def fungsi_gtts(items):
    tts = gTTS(text=items, lang="id", slow=False)
    filename = "ngomong.mp3"
    tts.save(filename)
    playsound("ngomong.mp3")
    os.remove(filename)



# Main Program
def main():
    while True:
        print("\nMasukan Nomor Untuk Melanjutkan!")
        print("1. Masukan Nama Kelas untuk MRO")
        print("2. Masukan Nama Kelas untuk PRO")
        print("3. Masukan Nama Kelas untuk ASTRADA")
        print("4. Masukan untuk melihat List")
        print("5. Masukan untuk Mengeluarkan List")
        print("6. Masukan utuk Keluar")

        perulangan = input("Masukan Inputan Yang dimau: ")
        if perulangan == "6":
            break
        elif perulangan == "1":
            antrian1.enqueue(input("Masukan Inputan nama MRO: "))
        elif perulangan == "2":
            antrian2.enqueue(input("Masukan Inputan nama PRO: "))
        elif perulangan == "3":
            antrian3.enqueue(input("Masukan Inputan nama ASTRADA: "))
        elif perulangan == "4":
            print("\n1.Melihat Antrian MRO")
            print("2. Melihat Antrian PRO")
            print("3. Melihat Antrian ASTRADA")
            print("4. Kembali")
            melihat = int(input("Masukan Inputan 1/2/3/4: "))
            if melihat == 4:
                continue
            elif melihat == 1:
                print("Antrian Saat Ini adalah: ", antrian1.items)
            elif melihat == 2:
                print("Antrian PRO saat ini: ", antrian2.items)
            elif melihat == 3:
                print("Antrian ASTRADA Saat ini: ",antrian3.items)
            else :
                print("Masukan Tidak Valid Silahkan Coba kembali!")
                continue
        elif perulangan == "5":
            print("\n1.Mengeluarkan Antrian MRO")
            print("2. Mengeluarkan Antrian PRO")
            print("3. Mengeluarkan Antrian ASTRADA")
            print("4. Kembali")
            mengeluarkan = int(input("Masukan yang ingin di keluarkan: "))
            if mengeluarkan == 4:
                continue
            elif mengeluarkan == 1:
                inputan = int(input("Masukan Berapa yang ingin di Keluarkan: "))
                for i in range(inputan):
                    items = antrian1.dequeue()
                    if items is not None:
                        print("Nama", "\""+items+"\"" , "Telah Dikeluarkan dari antrian.")
                        fungsi_gtts("nama" + items +"telah dikeluarkan dari antrian.")
                        time.sleep(3)
            elif mengeluarkan == 2:
                inputan = int(input("Masukan Berapa yang ingin di Keluarkan: "))
                for i in range(inputan):
                    items = antrian2.dequeue()
                    if items is not None:
                        print("Nama", "\""+items+"\"" , "Telah Dikeluarkan dari antrian.")
                        fungsi_gtts("nama" + items +"telah dikeluarkan dari antrian.")
                        time.sleep(3)
            elif mengeluarkan == 3:
                inputan = int(input("Masukan Berapa yang ingin di Keluarkan: "))
                for i in range(inputan):
                    items = antrian3.dequeue()
                    if items is not None:
                        print("Nama", "\""+items+"\"" , "Telah Dikeluarkan dari antrian.")
                        fungsi_gtts("nama" + items +"telah dikeluarkan dari antrian.")
                        time.sleep(3)
            else :
                print("Masukan Tidak Valid Silahkan Coba kembali!")
                continue


if __name__ == "__main__":
    main()

        






