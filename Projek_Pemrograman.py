import pandas as pd
import Modul as m

#mengimport data dari database, kemudian untuk dataframe kota dan kota asal, supaya lebih rapi dilakukan sort value
#sehingga memunculkan print berupa kota yang diurutkan berdasarkan abjad 

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
    print(
    )
    print('======================================================================')
      

    if cari.lower() == 'iya': 
        print()
        print('Berikut adalah jenis pengiriman yang ditawarkan:\n1. Paket Reguler (3-14 hari)\n2. Paket Cepat' 
        ' (1-3hari)\n3. Paket Kargo (7-30 hari)')
        print()
        jenis_pengiriman = m.jenis_paket()
        nama_pengiriman = jenis_pengiriman[1]
        jenis_pengiriman = jenis_pengiriman[0]
        print()
        print('======================================================================')
        print()
        
        #melakukan loop sederhana untuk memunculkan nama kota asal serta nama kota tujuan dengan iterrows
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
            print(str(index + 1) + ".", row["kota"].title())
        print()
        tujuan = m.cekKota()

        while True:   
                #bila ingin masukkan berat bisa float
            try :
                berat = float(input('Masukkan berat paket(kg)\t\t\t: '))
                if berat <= 0:
                    raise TypeError
                break
            except ValueError:
                print('Masukkan data berupa angka')
            except TypeError:
                print('Masukkan berat yang valid')
        
        #mendeklerasikan list baru untuk olah data, kemudian dilakukan penambahan data menggunakan append
        ekspedisi = ['J&T Express', 'JNE', 'SiCepat Express','Tiki ','Pos Indonesia']
        harga2 = []

        for i in ekspedisi:
            ber = m.hitungongkir(tujuan,berat, i, kota_asal, jenis_pengiriman)
            harga2.append(int(ber))
            
        print()
        print('======================================================================')
        print()
        print('Jenis pengiriman Anda\t: ' + nama_pengiriman)
        print("Kota pickup Anda\t: " + kota_asal)
        print("Kota tujuan Anda\t: " + tujuan.capitalize())
        print("Berat paket Anda\t:", berat)
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