second = int(input("nhập số giây : "))
hour = second // 3600
tg = second % 3600 
minute = tg // 60
sc2 = tg % 60
print(f"{hour}giờ:{minute}phút:{sc2}giây")



