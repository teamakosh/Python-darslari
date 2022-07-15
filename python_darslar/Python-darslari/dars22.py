avtolar = ["audi","ford","bmw","volvo"]
for avto in avtolar:
    if avto=="bmw":
        print(avto.upper())
    else:
        print(avto.titile())
        
        
        
        
        
def summa(*sonlar):
    """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
    return sum(sonlar)

print(summa(4,5,6,7))
# suma bu istalga sonlarni o'z ichiga oladi va ularrrning yig'indisini aniqlab 
 #beradi maslan bu yerda:22 chiqadi