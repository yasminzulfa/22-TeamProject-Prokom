import pandas as pd
import Modul as m
import numpy as np

df = pd.read_excel('Database.xlsx')
df2 = pd.read_excel('Daftar Pickup.xlsx')
df_baru = df.dropna()
df_kota_asal = df2.sort_values(by= "tempat").reset_index(drop=True)
df_kota_tujuan = df_baru.sort_values(by= "kota").reset_index(drop=True)
Harga = df_baru.drop('kode', axis =1)
Harga2 = df2.drop('No', axis =1)

print('======================================================================')
print()
print('Selamat Datang di Ongkirku ^_^'.center(60))
while True:
    cari = input('Apakah kamu mau mencari biaya ongkir dari Jawa Tengah?(iya/tidak): '.center(55))
    print()
    print('======================================================================')
      

    if cari.lower() == 'iya': 
        print("Berikut adalah lokasi pickup yang ada dalam program kami:")
        

        for index, row in df_kota_asal.iterrows():
            print(str(index + 1) + ".", row["tempat"].title())
        print()
        kota_asal = m.cekKotaAsal()
        print()
        print('======================================================================')
        print()
        print("Berikut adalah daftar kota yang ada dalam program kami:")
        for index, row in df_kota_tujuan.iterrows():
            print(str(index) + ".", row["kota"].title())
        print()
        tujuan = m.cekKota()
        while True:   
                #bila ingin masukkan berat bisa float
            try :
                berat = float(input('Masukkan berat paket(kg)\t\t\t: '))
                print('Berat paket Anda\t\t\t\t: {} Kg'.format(berat))
                break
            except:
                print('Masukkan data berupa angka')
            
        ekspedisi = ['J&T Express', 'JNE', 'SiCepat Express','Tiki ','Pos Indonesia']
        harga2 = []

        for i in ekspedisi:
            ber = m.hitungongkir(tujuan,berat, i, kota_asal)
            harga2.append(int(ber))
            

        print()
        print('======================================================================')
        print()
        print('Ini list rekomendasi kami untuk mu ^_^')
        print()
        print(m.rekomendasi(ekspedisi, harga2))
        print()
      
    elif cari.lower() == 'tidak':
        print('Oke, Terima Kasih telah menggunakan Ongkirku ^_^'.center(67))
        print()
        break

    else:
        print('Silahkan pilih iya atau tidak')