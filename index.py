o = input("Yapmak istediğiniz şeyi girin(hesap makinesi,alan hesaplama) :")
if o == "hesap makinesi":
    x = int(input("bir değer giriniz "))
    y = int(input("bir değer giriniz "))
    a = input("bir işlem giriniz ")
    if a == "+":
        print("toplamları : ",x+y)
    if a == "-":
        print("farkları : ",x-y)
    if a == "*":
        print("çarpımları : ",x*y)
    if a == "/":
        print("bölümleri : ",x/y)
if o == "alan hesaplama":
    xa = int(input("bir kenar giriniz "))
    ya = int(input("bir kenar giriniz "))
    print("alanı : ",xa*ya)
