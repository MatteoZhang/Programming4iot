import requests

if __name__=="__main__":
    while True:
        print "\nThis is a Calculator"
        operation = raw_input("choose operation: add, sub, div, mul: ")
        op1 = raw_input("choose the operand1: ")
        op2 = raw_input("choose the operand2: ")
        s = requests.get('http://localhost:8081/string/'+operation+'?'+'op1='+op1+'&'+'op2='+op2)
        r = s.json()
        print "\noperation: ", r['operation']
        print "operand1: ", r['op1']
        print "operand2: ", r['op2']
        print "%s %s %s = %s" %(r['op1'], r['operation'], r['op2'], r['result'])