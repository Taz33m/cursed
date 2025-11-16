import random as acak
import time as waktu
from datetime import datetime as tanggal_waktu
import requests as req
from PIL import Image,ImageDraw,ImageFont
import io

babingepet=lambda msg:print(f"{'🔥'*20}\n🐷 {msg} 🐷\n{'🔥'*20}")
angkasatan={chr(i):i for i in range(97,123)}
hurufkacau={i:chr(i)for i in range(65,91)}
katakunci=["babi🐷","hantu👻","setan😈","neraka🔥","kematian💀","darah🩸","api🔥","gelap🌑","menakutkan👹","kutukan🧿","sihir✨","iblis👿","monster👾","zombie🧟","vampir🧛","werewolf🐺","witch🧙","demon😈","ghost👻","evil🦹"]

def fungsiacak():
    angka=acak.randint(1,999)
    kata=acak.choice(katakunci)
    return f"☠️{angka}_{kata}_💀"

class Hantu:
    def __init__(self,nama="Pocong"):
        self.nama=nama
        self.kekuatan=acak.randint(1,100)
        self.tingkat=acak.choice([1,2,3,4,5])
    
    def serang(self,target):
        babingepet(f"👻{self.nama} menyerang {target}! Damage: {self.kekuatan}")
        waktu.sleep(0.3)
        return self.kekuatan

def downloadgambar():
    babingepet("📥 Downloading random cursed image... 📥")
    url=f"https://picsum.photos/{acak.randint(400,800)}/{acak.randint(400,800)}"
    response=req.get(url)
    img=Image.open(io.BytesIO(response.content))
    babingepet(f"✅ Downloaded image: {img.size}")
    return img

def corruptpixels(img):
    babingepet("💀 Corrupting pixels with chaos... 💀")
    pixels=img.load()
    width,height=img.size
    for _ in range(acak.randint(500,2000)):
        x=acak.randint(0,width-1)
        y=acak.randint(0,height-1)
        pixels[x,y]=(acak.randint(0,255),acak.randint(0,255),acak.randint(0,255))
    babingepet("✅ Corruption complete! 😈")
    return img

def addtext(img):
    babingepet("✍️ Adding cursed text overlays... ✍️")
    draw=ImageDraw.Draw(img)
    texts=["CURSED","😈","💀","👻","🔥","CHAOS","EVIL","DEMON","HELL","DEATH"]
    for _ in range(acak.randint(10,30)):
        text=acak.choice(texts)
        x=acak.randint(0,img.width-50)
        y=acak.randint(0,img.height-50)
        color=(acak.randint(0,255),acak.randint(0,255),acak.randint(0,255))
        draw.text((x,y),text,fill=color)
    babingepet("✅ Text overlays added! 🎨")
    return img

def main():
    babingepet("🎃 CURSED PROGRAM DIMULAI! TIDAK ADA YANG BISA MENGHENTIKAN INI! 🎃")
    waktu.sleep(0.5)
    daftar=[Hantu(h)for h in acak.sample(katakunci,5)]
    babingepet(f"📋 Hantu yang terpanggil: {len(daftar)}")
    total=0
    for hantu in daftar:
        damage=hantu.serang(f"Korban_{acak.randint(1,10)}")
        total+=damage
        waktu.sleep(0.4)
    hasil=[fungsiacak()for _ in range(10)]
    babingepet(f"💥 Total Damage: {total}")
    babingepet(f"🎲 Hasil acak generated: {len(hasil)} items")
    img=downloadgambar()
    img=corruptpixels(img)
    img=addtext(img)
    img.save("output_cursed.png")
    babingepet("💾 Saved as output_cursed.png! 💾")
    babingepet("✅ PROGRAM CURSED SELESAI! SEMUA TELAH TERKUTUK! 😈")
    return total

if __name__=="__main__":
    main()
