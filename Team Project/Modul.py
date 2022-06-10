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