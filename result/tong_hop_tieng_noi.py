#!/usr/bin/env python3
from pydub import AudioSegment
from playsound import playsound
from time import sleep
donvi = ["", "một ","hai ","ba ","bốn ", "năm ", "sáu ","bảy ","tám ","chín " ]
hangChuc = ["linh ", "một ","hai ","ba ","bốn ", "năm ", "sáu ","bảy ","tám ","chín "]
 
def num999c2(n):
    c = int(n % 10) # hang don vi
    b = int(((n % 100) - c) / 10) # hang chuc
    a = int(((n % 1000) - (b * 10) - c) / 100) # hang tram
    st=donvi[a]+"trăm " +hangChuc[b] +donvi[c]
    return st
def tonghop(x):
#----------------------------------------- Xử lý chuỗi đầu vào--------------------------------------
  x=x.split(" ")
  textArr=[]
  for e in x:
    try:
      tg=int(e)
      numberToArr=num999c2(tg)
      numberToArr=numberToArr.strip().split(" ")
      for n in numberToArr:
        textArr.append(n.lower())      
    except:
      textArr.append(e.lower())
  print(textArr)
  strdir="D:/banmai/" #dương dan tớ thu mục 3000 file audio
  arrHasdri=[]
  for ele in textArr:
      arrHasdri.append(strdir+ele+".mp3")
  #----------------------------------------- Load file theo đường dẫn rồi cộng file --------------------------------------
  S=0
  for ele1 in arrHasdri:
    print(ele1)
    S+=AudioSegment.from_mp3(ele1)  
  S.export("KQ.mp3", format="mp3")      
  playsound('KQ.mp3')
  sleep(1)

def main():
  x=input()
  tonghop(x)
if __name__ == "__main__":
    main()