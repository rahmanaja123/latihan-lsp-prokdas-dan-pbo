def garis():
    print("-----------------------------------------------")

#tampilan menu
print("--------HOTEL SMK JP ONE--------")
print("-- lama inap ---- superior ---- deluxe -------- premium --")
print("-1 s.d 2 hari - 100.00/night - 150.000/night - 200.000/night -")
print("-3 s.d 4 hari - 90.000/night - 135.000/night - 180.000/night -")
print("-5 hari keatas- 80.000/night - 120.000/night - 160.000/night -")

#input data
tipe_kamar = input("Masukan Tipe Kamar : ")
lama_inap = int(input("Masukan Lama Menginap : "))


#tipe_superior
if tipe_kamar == "superior":
    if lama_inap <= 2:
        total_harga = 100000*lama_inap
    elif lama_inap <= 4:
        total_harga = 90000*lama_inap
    else:
        total_harga = 80000*lama_inap
    
#tipe_deluxe
elif tipe_kamar == "deluxe":
    if lama_inap <= 2:
        total_harga = 150000*lama_inap
    elif lama_inap <= 4:
        total_harga = 135000*lama_inap
    else:
        total_harga = 120000*lama_inap
    
#tipe_premium
elif tipe_kamar == "premium":
    if lama_inap <= 2:
        total_harga = 200000*lama_inap
    elif lama_inap <= 4:
        total_harga = 180000*lama_inap
    else:
        total_harga = 160000*lama_inap
    
#total harga menginap
garis()
print(" Tipe kamar yang dipilih : ",(tipe_kamar))
print(" Lama Menginap : ",(lama_inap)," Hari")
print(" Total harga yang dibayar : Rp.", (total_harga))
