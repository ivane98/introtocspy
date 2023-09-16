def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn
    return n


class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

        common = gcd(self.num, self.den)

        self.num = top//common
        self.den = bottom//common

    def __str__(self):
        return str(self.num)+"/"+str(self.den)

    def show(self):
        print(self.num, "/", self.den)

    def __add__(self, otherfraction):
        newnum = self.num*otherfraction.den + \
            self.den*otherfraction.num
        newden = self.den * otherfraction.den
        return Fraction(newnum, newden)

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum == secondnum

    def getNum(self):
        return self.num

    def getDen(self):
        return self.den


x = Fraction(2, 4)
y = Fraction(1, 4)

print(x+y)
