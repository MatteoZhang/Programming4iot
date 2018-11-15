class OP:
    def Add(self, a):
        try:
            c = 0
            for i in range(len(a)):
                c = c + a[i]
        except Exception, e:
            print "invalid input"
        return c
    def Sub(self, a):
        try:
            c = 0
            for i in range(len(a)):
                c = c - a[i]
        except Exception, e:
            print "invalid input"
        return c
    def Div(self, a):
        try:
            c = a[0]
            for i in range(len(a)-1):
                c = c/a[i+1]
        except Exception, e:
            print "invalid input division by 0"
            c = "not valid"
        return c
    def Mul(self, a):
        try:
            c = 1
            for i in range(len(a)):
                c = c * a[i]
        except Exception, e:
            print "invalid input"
        return c