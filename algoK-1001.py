print("perulangan 1")
for i in range(5):
    print(i)

print("perulangan 2")
for i in range(1,6):
    print(i)


print("perulangan 3")
for i in range(2,20,3):
    print(i)


print("perulangan 4")
numbers = [10, 20, 30, 40, 50]
total = 0
for num in numbers:
    total += num
print("Total nilai:", total)

print("perluangan 5")
for i in[2,4,6,8,10]:
    print("ini pengulangan ke -",i)

print("perulangan 6")
for i in["rawon","nasi kuning","soto madura","kupat tahu","kerak telor","rendang batoko","pempek selam","ayam betutu"]:
    print(i,"adalah masakan khas nusantara...")               

print("perulangan 7")
print("PROGRAM PYTHON MENGHITUNG NILAI RATA-RATA")
banyakdata = 5
i = 0
print()
jum = 0
while i < 5 :
 nilai = int(input("Masukkan data ke-%d: " % (i+1)))
 i = i + 1
 jum = jum + nilai
 rata = jum / banyakdata
print("\nRata-rata = %0.2f" % rata)

print("perulangan 8")
n = int(input("Masukkan jumlah angka Fibonacci: "))
a, b = 0, 1

for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b


number = int(input("Masukkan angka: "))
is_prime = True

for i in range(2, number):
    if number % i == 0:
        is_prime = False
        break

if is_prime and number > 1:
    print(number, "adalah bilangan prima.")
else:
    print(number, "bukan bilangan prima.")
