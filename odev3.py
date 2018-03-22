# Programlama-Odev-3
while döngüsü
1)
satis=500
fiyat=20
ciro=5000
i=1
while True:
    satis=satis+200
    fiyat=fiyat+10
    ciro=ciro+(satis*fiyat)
    i=i+1
    if (ciro>500000):
        print(i,"Ay sonra cironuz",ciro,"olur ve 500.000 üzerine çıkar.")
        break

*****************************************

2)
stok=10000
i=1
while True:
    stok=stok-400
    i=i+1
    if (stok<=0):
        print(i,"Ay sonra stoklarınız sıfırlanır")
        break
*******************************************
3)

girilen=""
while (girilen!="0"):
    girilen=input("Bir sayı giriniz. Çıkış için [0]")
    if girilen=="0":
        print("Program sonlandırıldı.")
    else:
        girilen=float(girilen)
        print("Girdiğiniz sayının 3 ile bölümünden kalan:",girilen%3)
********************************************
4)
saat=1
while(saat>0):
    saat=int(input("haftalık personel çalışma saati giriniz"))
    if(saat>62):
        print("haftalık 22 saatten fazla personele mesai yaptırılamaz")
        break
        
    mesai=saat-40
    omaas=40*90+(mesai*9)
    print("ödenecek maaş=",omaas)
*********************************************
5)
gUretim=200
gDefoluUrun=0
tDefoluUrun=0
i=0
while (gDefoluUrun<=gUretim*0.20):
    gDefoluUrun=int(input("Günlük defolu ürün sayısı:"))
    tDefoluUrun=tDefoluUrun+gDefoluUrun
    i=i+1
    if (gDefoluUrun>gUretim*0.20):
        print("defolu Ürün Sayısı Limiti Aştı")
        break
