class Main:
    def __init__(self):
        self.i = True
        print("Яку дію треба виконати?")
        print("1 - розв'язати рівняння")
        print("2 - згенерувати просте число")
        print("0/n/no - вийти")

        vvid = input("Зроби вибір (1/2/0): ")

        if vvid == "1":
            print("Введіть номер виду рівняння, \
яке бажаєте обчислити:")
            print("1) a mod m = x")
            print("2) a^b mod m = x")
            print("3) a * x ≡ b mod m")
            v = input("Зроби вибір (1/2/3): ")

            if v == "1" or v == "2" or v == "3":
            
                self.m = int(input("Введіть модуль m: "))
                self.a = int(input("Основа a: "))

                if v == "1":
                    self.first(self.a, self.m)

                elif v == "2":
                    self.b = int(input("Показник степеню b: "))
                    self.second(self.a, self.b, self.m)

                elif v == "3":
                    self.b = int(input("Показник степеню b: "))
                    self.third(self.a, self.b, self.m)

            else:
                print("\nУпс! Щось не те! Почніть спочатку, будь-ласка!\n")
                


        elif vvid == "2":
            print("Задайте діапазон")
            self.A = int(input("Від: "))
            self.B = int(input("До: "))
            print(self.simple_numb(self.A, self.B))
            
        else:
            if vvid == "0" or vvid == "n" or vvid == "no":
                print("До нових зустрічей!")
                self.i = False
            else:
                print("\nУпс! Щось не те! Повторіть ввід!\n")

        

    def first(self, a, m):
        print(1)
        

    def second(self, a, b, m):
        print(2)
        
        b = bin(b)

        if b == 0:
            return 1
        else:
            x = a ^ 2
            for s in range(str(b).count("1") - 1):
                print(x)
                x = x ^ 2
                x *= a
            return x
                
                

    def third(self, a, b, m):
        print(3)

    def simple_numb(self, A, B):
        print(4)
        
        if A == 0:
            return B
        while B != 0:
            if A > B:
                A /= A - B
            else:
                B /= B - A
            return A

##        all_numbers = []
##        for k in range(A, B + 1):
##            if k != 1:
##                all_numbers.add(k)
##
##        for l in all_numbers:
##            
##        
##        q = input("Вивести одине число чи всі? (1/2) ")
##        if q == "1":
##            print(sum([i**i for i in range(1,1001)])%(10**10))
##    

if __name__ == "__main__":
    i = True
    while i:
        res = Main()
        i = res.i
