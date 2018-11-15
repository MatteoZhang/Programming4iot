class OP:
    def Add(self, a, b):
        try:
            c = a + b
        except Exception, e:
            print "invalid input"
        return c
    def Sub(self, a, b):
        try:
            c = a - b
        except Exception, e:
            print "invalid input"
        return c
    def Div(self, a, b):
        try:
            c = a/b
        except Exception, e:
            print "invalid input division by 0"
            c = "not valid"
        return c
    def Mul(self, a, b):
        try:
            c = a * b
        except Exception, e:
            print "invalid input"
        return c