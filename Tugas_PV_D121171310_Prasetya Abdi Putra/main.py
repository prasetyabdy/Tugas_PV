print(30*"=")
print("Kalkulator Sederhana")
print("D121171310_Prasetya Abdi Putra")
print(30*"=" + "\n")

a = float(input("masukkan angka 1 = "))
op = input("operator (+,-,x,/) : ")
b = float(input("masukkan angka 2 = "))

#operator penjumlahan
if op == "+":
    hasil = a + b
    print(f"hasilnya adalah {hasil}")
#operator pengurangan
elif op == "-":
    hasil = a - b
    print(f"hasilnya adalah {hasil}")
#operator perkalian
elif op == "x" or op == "*":
    hasil = a * b
    print(f"hasilnya adalah {hasil}")
#operator pembagian
elif op == "/":
    hasil = a / b
    print(f"hasilnya adalah {hasil}")
else:
    print("operator unvalid")