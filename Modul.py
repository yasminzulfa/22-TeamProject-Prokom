import numpy as np
import pandas as pd
from tabulate import tabulate

df = pd.read_excel('Database.xlsx')
df2 = pd.read_excel('Daftar Pickup.xlsx')
df_baru = df.dropna()
Harga = df_baru.drop('kode', axis =1)
Harga2 = df2.drop('No', axis =1)

#untuk fungsi cekKota dan ceKotaAsal, dilakukan pencarian apakah input ada di dalam database, loop akan diulang sampai 
#data yang diinput valid
#Yunita
def jenis_paket():
  while True:
    try:
      paket = int(input("Masukkan nomor jenis pengiriman (Contoh : 1)\t: "))
      if paket == 1:
        return paket, "Reguler"
      elif paket == 2:
        return paket, "Cepat"
      elif paket == 3:
        return paket, "Kargo"
      else:
        raise ValueError

    except ValueError:
      print('Masukkan pilihan yang valid')

def cekKota():
    while True:
      tujuan = input("Masukkan kode kota tujuan (Contoh : Jakarta)\t: ")
      tujuan = tujuan.lower()
      cek = tujuan in df.kota.unique()
      if cek == True:
        return tujuan
        break
      else:
        print("Kota tujuan tidak terdaftar, silahkan masukkan kembali")

#Kiki        
def cekKotaAsal():
    while True:
      pickup = input("Masukkan kota Pickup (Contoh : Surakarta): ")
      pickup = pickup.capitalize()
      cek = pickup in df2.tempat.unique()
      if cek == True:
        return pickup
        break
      else:
        print("Kota pickup tidak terdaftar, silahkan masukkan kembali")

#pengolahan data menggunakan pandas, yakni dengan mencari lokasi harga ekspedisi, dengan data yang diinput 
#berupa kota asal/kota tujuan. Untuk biaya ongkir kargo/truk yang kurang dari 25kg akan dianggap 25kg dengan biaya 
#sepersepuluh dari yang ditentukan, jika lebih maka kemudian baru diberikan kelipatan sebesar sepersepuluh dari 
#biaya ongkir yang ditentukan oleh database. Untuk paket cepat, biaya akan dikenakan 5x lipat dari yang tertera di 
#database, untuk fee akan dikenakan biaya untuk kelipatan 10kg pertama, dan akan ditambah sepersepuluh dari database per
#kilogramnya
#Yasmin
def hitungongkir(kota, berat, ekspedisi, fee, jenis_paket):
  if jenis_paket == 1:
    berat_asli = berat
  elif jenis_paket == 2:
    berat_asli = berat*5
  elif jenis_paket == 3:
    berat_floor = berat//25
    if berat_floor >= 1:
      berat_asli = berat_floor + ((berat%25)/25)
    else:
      berat_asli = 1
  
  harga_ongkir = (Harga.loc[df['kota'] == kota, ekspedisi].iloc[0])*berat_asli
  fee = (Harga2.loc[df2['tempat'] == fee, ekspedisi].iloc[0]) * ((berat//10)+1)
  total = harga_ongkir + fee
  return total

#melakukan olah data dengan melakukan pengurutan dari yang termurah hingga termahal, numpy digunakan untuk memberikan
#index dari angka 1-5
#Yasmin
def rekomendasi(ekspedisi, harga2):
    
    tampilan = {'Ekpedisi' : ekspedisi,
                 'Harga': harga2}
    df_tampil = pd.DataFrame(tampilan, index = np.arange(1, 6))
    dft = df_tampil.sort_values(by = 'Harga')
    dft.insert(0,'No',[1,2,3,4,5])
    dft.index = np.arange(1,6)
    dft = tabulate(dft, headers=dft.columns, showindex=False)
    return(dft)