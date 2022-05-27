import pandas as pd
import numpy as np

df = pd.read_excel('Database.xlsx')
df_baru = df.dropna()
Harga = df_baru.drop('no.', axis =1)

def cekKota():
    while True:
      tujuan = input("Masukkan kota tujuan: ")
      tujuan = tujuan.lower()
      cek = tujuan in df.ibukota.unique()
      if cek == True:
        print("Kota tujuan Anda: " + tujuan.capitalize())
        return tujuan
        break
      else:
        print("Kota tujuan tidak terdaftar, silahkan masukkan kembali")
      

def rekomendasi(ekspedisi, harga2):
    
    tampilan = {'Ekpedisi' : ekspedisi,
                 'Harga': harga2}
    df_tampil = pd.DataFrame(tampilan, index = np.arange(1, 6))
    dft = df_tampil.sort_values(by = 'Harga')
    dft.index = np.arange(1,6)
    return(dft)

def hitungongkir(kota, berat, ekspedisi):
    harga_ongkir = (Harga.loc[df['ibukota'] == kota, ekspedisi].iloc[0])*berat
    return harga_ongkir

print('Selamat Datang di Ongkirku')
print("Berikut adalah daftar kota yang ada dalam program kami:")
for index, row in df_baru.iterrows():
    print(str(index) + ".", row["ibukota"].title())
print()
while True:
      cari = input('Apakah kamu mau mencari biaya ongkir dari Jawa Tengah?(iya/tidak): ')
      

      if cari.lower() == 'iya': 
          tujuan = cekKota()

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
              ber = hitungongkir(tujuan,berat, i)
              harga2.append(int(ber))

          print()
          print('Ini list rekomendasi kami untuk mu ^_^')
          print(rekomendasi(ekspedisi, harga2))
          print()
      
      elif cari.lower() == 'tidak':
          print('Oke, Terima Kasih telah menggunakan Ongkirku ^_^')
          break

      else:
          print('Silahkan pilih iya atau tidak')