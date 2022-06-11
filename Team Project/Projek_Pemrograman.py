import pandas as pd
import Modul as m

df = pd.read_excel('Database.xlsx')
df2 = pd.read_excel('Daftar Pickup.xlsx')
df_baru = df.dropna()
Harga = df_baru.drop('kode', axis =1)
Harga2 = df2.drop('No', axis =1)

print('Selamat Datang di Ongkirku ^_^')
while True:
    cari = input('Apakah kamu mau mencari biaya ongkir dari Jawa Tengah?(iya/tidak): ')
    print()

      

    if cari.lower() == 'iya': 
        print("Berikut adalah lokasi pickup yang ada dalam program kami:")
        

        for index, row in df2.iterrows():
            print(str(index + 1) + ".", row["tempat"].title())
        kota_asal = m.cekKotaAsal()
        print()

        print("Berikut adalah daftar kota yang ada dalam program kami:")
        for index, row in df_baru.iterrows():
            print(str(index) + ".", row["ibukota"].title())
        tujuan = m.cekKota()
        print()
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
            ber = m.hitungongkir(tujuan,berat, i, kota_asal)
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