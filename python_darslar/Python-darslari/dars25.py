sonlar = list(range(11)) 

def daraja2(x):
    """Berilgan sonning kvadratini qaytaruvchi funksiya"""
    return x*x

print(list(map(daraja2,sonlar)))
# sonlarningkvadratini chiqarib beruvchi codlar 11 gacha bulgan sonlarni

a = [4, 5, 6]
b = [7, 8, 9]
a_plus_b = list(map(lambda x,y:x+y,a,b))
print(a_plus_b)
# bu yerda a dagi sonlarni b dagi sonlarga qushadi

import random
def sontop(x = 10):
  tasodifiy_son = random.randint(1,x)
  print(f"Men 1 dan {x} gacha son o'yladim. Topishga harakat qiling? :")
  taxminlar = 1
  while True:
    taxminlar += 1
    taxmin = int(input("-->"))
    if taxmin < tasodifiy_son:
      print("Xato man o'ylagan son bundan kattaroq. Yana harakat qiling:")
    elif taxmin > tasodifiy_son:
      print("Xato man o'ylagan son bundan kichikroq. Yana harakat qiling:")
    else:
      break
  return taxminlar
print("Siz {taxminlar} taxmin bilan topdingiz")
sontop()
# so'z o'yini kampyuter so'z uylaydi siz uni topishiingiz kerak