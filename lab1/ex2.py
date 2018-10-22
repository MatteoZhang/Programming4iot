from sys import argv
import json

class OP:
    def __init__(self, a, length):
        self.list = a
        self.len = length
        return
    def Add(self):
        try:
            c = 0
            for i in range(int(length)):
                c = c + a[i]
        except Exception, e:
            print "invalid input"
        return c
    def Sub(self):
        try:
            c = 0
            for i in range(int(length)):
                c = c - a[i]
        except Exception, e:
            print "invalid input"
        return c
    def Div(self):
        try:
            c = a[0]
            for i in range(int(length)-1):
                c = c/a[i+1]
        except Exception, e:
            print "invalid input division by 0"
            c = "not valid"
        return c
    def Mul(self):
        try:
            c = 1
            for i in range(int(length)):
                c = c * a[i]
        except Exception, e:
            print "invalid input"
        return c

if __name__ == "__main__":
    filename = argv[1]
    print "erasing this file %r" %filename
    file = open(filename, 'w')
    file.truncate()
    obj = {}
    length = raw_input("length of the array: ")
    a = []
    for i in range(int(length)):
        a.append(float(raw_input("now give me the %d operand: " % i)))
    print "my array: ", a
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
        ris = OP(a, length)
        if operation == "5":
            break
        elif operation == "1":
            obj["operand"] = a
            obj["operation"] = "add"
            obj["result"] = ris.Add()
        elif operation == "2":
            obj["operand"] = a
            obj["operation"] = "sub"
            obj["result"] = ris.Sub()
        elif operation == "3":
            obj["operand"] = a
            obj["operation"] = "mul"
            obj["result"] = ris.Mul()
        elif operation == "4":
            obj["operand"] = a
            obj["operation"] = "div"
            obj["result"] = ris.Div()
        else:
            print "operation failed", operation
        print obj
        string = json.dumps(obj, indent=4)
        file.write(string)
    file.close()
