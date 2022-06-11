import numpy as np
import pandas as pd

df = pd.read_excel('Database.xlsx')
df2 = pd.read_excel('Daftar Pickup.xlsx')
df_baru = df.dropna()
Harga = df_baru.drop('kode', axis =1)
Harga2 = df2.drop('No', axis =1)

def cekKota():
    while True:
      tujuan = input("Masukkan kode kota tujuan (Contoh : Jakarta) : ")
      tujuan = tujuan.lower()
      cek = tujuan in df.ibukota.unique()
      if cek == True:
        print("Kota tujuan Anda: " + tujuan.capitalize())
        return tujuan
        break
      else:
        print("Kota tujuan tidak terdaftar, silahkan masukkan kembali")
        
def cekKotaAsal():
    while True:
      pickup = input("Masukkan kota Pickup (Contoh : Surakarta) : ")
      pickup = pickup.capitalize()
      cek = pickup in df2.tempat.unique()
      if cek == True:
        print("Kota pickup Anda: " + pickup)
        return pickup
        break
      else:
        print("Kota pickup tidak terdaftar, silahkan masukkan kembali")

def rekomendasi(ekspedisi, harga2):
    
    tampilan = {'Ekpedisi' : ekspedisi,
                 'Harga': harga2}
    df_tampil = pd.DataFrame(tampilan, index = np.arange(1, 6))
    dft = df_tampil.sort_values(by = 'Harga')
    dft.index = np.arange(1,6)
    return(dft)

def hitungongkir(kota, berat, ekspedisi, fee):
    harga_ongkir = (Harga.loc[df['ibukota'] == kota, ekspedisi].iloc[0])*berat
    fee = (Harga2.loc[df2['tempat'] == fee, ekspedisi].iloc[0]) * berat
    total = harga_ongkir + fee
    return total