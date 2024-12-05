# 1.    minta inputan npm yg berisi 3 npm terakhir, ubah tipe data npm ke bentuk float lakukan perhitungan berikut 
#       npm * (1+10/31)5+2

npm = float(input("masukkan NPM: "))
hasil = npm * ((1 + 10 / 31) ** (5 + 2))
print(hasil)

#2.     bikin perulangan 1-10
for i in range(1,11):
    hasil= 7 * i
    print(f"7 x{i}={hasil}")

#3      buat fungsi dengan nama konversi_suhu(celcius) buat perintah dari suhu c ke f dengan rumus
#  f= (c* 9/5)=32  inputkan nilai celcius=30    bandingan dgn hasil koversi_suhu dgn hasil soal no 1
def konversi_suhu(celcius):
    fahrenheit=celcius * 9/5 +32
    return fahrenheit

celcius=30
hasil_konversi=konversi_suhu(30)
print(f"hasil konversi dari(30)°C adalah{hasil_konversi}°F")

hasil= 86.0
perbandingan = hasil_konversi >= hasil
print (perbandingan)

#no 4   buat program yg menerima input bilangan bulat positif 
#jika genap dan abis dibagi 3, tambhkan bil.tersebut dgn 6
# jika ganjil dan abis dibagi 5, tambhkan bil. tersebut dgn 12
#jika tdk memenuhi salah satu kondisi diatas,keluarkan pesan "tdk ada transformasi yg diterapkan"

bilangan_bulat=int(int(input("masukkan bilangan bulat:")))
print("masukkan bilangan bulat:",bilangan_bulat)

if bilangan_bulat %2 == 0 and bilangan_bulat %3==0:
    bilangan_bulat +=6
    print (bilangan_bulat)

elif bilangan_bulat %2 !=0 and bilangan_bulat %5==0:
    bilangan_bulat +=12
    print(bilangan_bulat)

else :
    print("tidak ada transformasi yang diterapkan")

#no 5       buat fungsi dgn  nama find_lowest(num1, num2, num3)
#bertujuan u. mencari bil. terkecil dari 3 parameter yg diterima

def find_lowest(num1, num2, num3):
    if num1 < num2 and num1 < num3:
        return num1
   
    elif num2 < num1 and num2< num3:
        return num2
    
    else:
        return num3