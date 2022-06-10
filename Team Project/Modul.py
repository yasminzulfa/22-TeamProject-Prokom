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