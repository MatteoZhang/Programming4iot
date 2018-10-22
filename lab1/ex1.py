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
        operation = raw_input("you can choose from these operations: \n"
                              "1) addition \n"
                              "2) subtraction \n"
                              "3) multiplication \n"
                              "4) division \n"
                              "5) exit from the program \n"
                              "your choice 1,2,3,4 or 5: ")
        if operation == "5":
            break
        a = raw_input("now give me the first operand: ")
        b = raw_input("second operand...: ")
        ris = OP(a, b)
        if operation == "5":
            break
        elif operation == "1":
            obj["operand 1"] = a
            obj["operand 2"] = b
            obj["operation"] = "add"
            obj["result"] = ris.Add()
        elif operation == "2":
            obj["operand 1"] = a
            obj["operand 2"] = b
            obj["operation"] = "sub"
            obj["result"] = ris.Sub()
        elif operation == "3":
            obj["operand 1"] = a
            obj["operand 2"] = b
            obj["operation"] = "mul"
            obj["result"] = ris.Mul()
        elif operation == "4":
            obj["operand 1"] = a
            obj["operand 2"] = b
            obj["operation"] = "div"
            obj["result"] = ris.Div()
        else:
            print "operation failed", operation
        print obj
        string = json.dumps(obj, indent=4)
        file.write(string)
    file.close()
