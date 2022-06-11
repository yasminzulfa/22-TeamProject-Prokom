import pandas as pd
import numpy as np
import Modul as m

df = pd.read_excel("Database.xlsx")
df_baru = df.dropna()

print('Selamat Datang di Ongkirku')
print("Berikut adalah daftar kota yang ada dalam program kami:")
for index, row in df_baru.iterrows():
    print(str(index) + ".", row["ibukota"].title())
print()
while True:
      cari = input('Apakah kamu mau mencari biaya ongkir dari Jawa Tengah?(iya/tidak): ')
      

      if cari.lower() == 'iya': 
          tujuan = m.cekKota()

          while True:
                
                #bila ingin masukkan berat bisa float
                try :
                    berat = float(input('Masukkan berat paket(kg): '))
                    print('berat paket Anda:', berat ,'Kg')
                    break
                except:
                    print('Masukkan data berupa angka')
            
          ekspedisi = ['J&T Express', 'JNE', 'SiCepat Express','Tiki ','Pos Indonesia']
          harga2 = []

          for i in ekspedisi:
              ber = m.hitungongkir(tujuan,berat, i)
              harga2.append(int(ber))

          print()
          print('Ini list rekomendasi kami untuk mu ^_^')
          print(m.rekomendasi(ekspedisi, harga2))
          print()
      
      elif cari.lower() == 'tidak':
          print('Oke, Terima Kasih telah menggunakan Ongkirku ^_^')
          break

      else:
          print('Silahkan pilih iya atau tidak')