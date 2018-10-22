from sys import argv
import json

class OP:
    def __init__(self, a, b):
        self.a = float(a)
        self.b = float(b)
        return
    def Add(self):
        try:
            c = self.a + self.b
        except Exception, e:
            print "invalid input"
        return c
    def Sub(self):
        try:
            c = self.a - self.b
        except Exception, e:
            print "invalid input"
        return c
    def Div(self):
        try:
            c = self.a/self.b
        except Exception, e:
            print "invalid input division by 0"
            c = "not valid"
        return c
    def Mul(self):
        try:
            c = self.a * self.b
        except Exception, e:
            print "invalid input"
        return c

if __name__ == "__main__":
    filename = argv[1]
    print "erasing this file %r" %filename
    file = open(filename, 'w')
    file.truncate()
    obj = {}
    while True:
        operation = raw_input("""
        this is a simple calculator 
        please write the operation u want to perform and the operands
        as the following : add 1 1 
        u can perform add sub mul div or exit the program 
        """)
        all = operation.split()
        print all
        ris = OP(all[1], all[2])
        if all[0] == "exit":
            break
        elif all[0] == "add":
            obj["string"] = operation
            obj["result"] = ris.Add()
        elif all[0] == "sub":
            obj["string"] = operation
            obj["result"] = ris.Sub()
        elif all[0] == "mul":
            obj["string"] = operation
            obj["result"] = ris.Mul()
        elif all[0] == "div":
            obj["string"] = operation
            obj["result"] = ris.Div()
        else:
            print "operation failed u choose : ", all[0]
        print obj
        string = json.dumps(obj)
        file.write(string)
    file.close()
