class Calculator:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def add(self):
        self.result = self.a + self.b
        return self.result
    
    def sub(self):
        if self.a == self.b:
            self.result = self.a - self.b
            return self.result
        elif self.a >= self.b:
            self.result = self.a - self.b
            return self.result
        else:
            self.result = self.b - self.a
            return self.result
            #print(str(self.b) + " - " + str(self.a) + " = " + str(self.result))
        #print(str(self.a) + " - " + str(self.b) + " = " + str(self.result))

    def multiply(self):
        self.result = self.a * self.b
        return self.result
    
    def divide(self):
        self.result = self.a / self.b
        return self.result
    
    def print_states(self, x):
        self.x = x
        print(f"Yapılan işlemin sonucu {x}'tir.")
            
girilen_islem = input("Yapmak istediğiniz işlemi belirtilen örnek karakterlerden birini seçiniz ( +, -, *, / ) :  ")
if girilen_islem == "+":
    print("Toplama işlemi yapmak istediğiniz iki değeri giriniz:  ")
    value_1 = int(input("Birinci değeri giriniz:"))
    value_2 = int(input("İkinci değeri giriniz:"))
    calculator_obje = Calculator(value_1, value_2)
    toplama_degeri=calculator_obje.add()
    calculator_obje.print_states(toplama_degeri)
elif girilen_islem == "-":
    print("Çıkartma işlemi yapmak istediğiniz iki değeri giriniz:  ")
    value_1 = int(input("Birinci değeri giriniz:"))
    value_2 = int(input("İkinci değeri giriniz:"))
    calculator_obje = Calculator(value_1, value_2)
    cikarma_degeri=calculator_obje.sub()
    calculator_obje.print_states(cikarma_degeri)
elif girilen_islem == "*":
    print("Çarpma işlemi yapmak istediğiniz iki değeri giriniz:  ")
    value_1 = int(input("Birinci değeri giriniz:"))
    value_2 = int(input("İkinci değeri giriniz:"))
    calculator_obje = Calculator(value_1, value_2)
    carpma_degeri=calculator_obje.multiply()
    calculator_obje.print_states(carpma_degeri)
elif girilen_islem == "/":
    print("Bölme işlemi yapmak istediğiniz iki değeri giriniz:  ")
    value_1 = int(input("Birinci değeri giriniz:"))
    value_2 = int(input("İkinci değeri giriniz:"))
    calculator_obje = Calculator(value_1, value_2)
    bölme_degeri=calculator_obje.divide()
    calculator_obje.print_states(bölme_degeri)
else:
    print("Hataa!! Farklı bir işlemde bulundunuz yapmış olduğunuz işlemi kontrol edip tekrardan giriniz...")



