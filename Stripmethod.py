
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle




# _test_n:    testet den Input n auf Randfälle um Division durch Null zu verhindern       
#            n € N für n>0                                                               
def _test_n(n:int):
    assert isinstance(n, int), "ERROR: n muss eine Natürliche Zahl sein!"
    assert n>0,                "ERROR: n muss größer 0 sein!"

# _intervall: berrechnungen um die unteren Eckpunkte der Rechtecke zu finden
def _intervall(a:int,b:int, n:int) -> list:
    _test_n(n)
    inter_tuple = [(a+(_breite(a,b,n)*i), a+(_breite(a,b,n)*(i+1))) for i in range(n)]
    return inter_tuple

# _breite:    berrechnet die _breite eines der Rechtecke
def _breite(a:int,b:int, n:int) -> float:
    _test_n(n)
    return (b-a)/n

# OberRechtecke:   bestimmt x und y Wert der Rechteck ecken (Obersumme)     
class Stripmethod:
    def __init__(self, f, a:int, b:int, n:int):
        #implement lambda parser
        self.f = f
        try: 
            f(2)
        except Exception:
            raise ValueError("ERROR: f is not callable!")
        self.a = a
        self.b = b
        _test_n(n)
        self.n = n

    def _OberRechtecke(self) -> list:
        f, a, b, n = self.f, self.a, self.b, self.n
        inter_tuple = _intervall(a,b,n)
        return [f(i[1])*_breite(a,b,n) for i in inter_tuple]

    # UnterRechtecke:  bestimmt x und y Wert der Rechteck ecken (Untersumme)     
    def _UnterRechtecke(self) -> list:
        f, a, b, n = self.f, self.a, self.b, self.n
        inter_tuple = _intervall(a,b,n)
        return [f(i[0])*_breite(a,b,n) for i in inter_tuple]

    # Obersumme:       bestimmt die summe aller FlächeInhalte der Rechtecke von OberRechtecke
    def Obersumme(self, f, a:int, b:int, n:int) -> list:
        _test_n(n)
        inter_tuple = _intervall(a,b,n)
        #return sum([f(i[1])*_breite(a,b,n) for i in inter_tuple])
        breite = _breite(a, b, n)
        return sum([breite*abs(i) for i in [f(x if abs(f(x))>=abs(f(y)) else y) for x,y in inter_tuple]])

    # Untersumme:      bestimmt die summe aller FlächeInhalte der Rechtecke von UnterRechtecke
    def Untersumme(self, f,a:int,b:int, n:int) -> list:
        _test_n(n)
        inter_tuple = _intervall(a,b,n)
        breite = _breite(a, b, n)
        return sum([breite*abs(i) for i in [f(x if abs(f(x))<=abs(f(y)) else y) for x,y in inter_tuple]])

    def _UntersummePlotData(self, f,a:int,b:int, n:int) -> list:
        return [((x if abs(f(x)) >= abs(f(y)) else y-_breite(a,b,n),0), _breite(a,b,n), f(x if abs(f(x))<=abs(f(y)) else y)) for x,y in _intervall(a,b,n)]

    # für die Obersumme werden die Rechteck punkte bestimmt 
    def _ObersummePlotData(self, f,a:int,b:int, n:int) -> list:
        return [((x if abs(f(x)) <= abs(f(y)) else y-_breite(a,b,n),0), _breite(a,b,n), f(x if abs(f(x))>=abs(f(y)) else y)) for x,y in _intervall(a,b,n)]

    def plotUntersumme(self) -> plt.plot:
        f, a, b, n = self.f, self.a, self.b, self.n
        fig, ax = plt.subplots()

        ax.plot([x for x in range(a, b+1)], [f(x) for x in range(a, b+1)])

        rechteckeListe = self._UntersummePlotData(f, a, b, n)

        for r in rechteckeListe:
            print(r)
            ax.add_patch(Rectangle(*r, fill=False, label="untersumme", edgecolor="green"))

        u, o = self.Untersumme(f, a, b, n),self.Obersumme(f, a, b, n)
        print("PLOT_DATA: Untersumme: {}, Obersumme: {}, difference: {}".format(u, o, abs(o-u))) 
        plt.show()

    def plotObersumme(self) -> plt.plot:
        f, a, b, n = self.f, self.a, self.b, self.n
        fig, ax = plt.subplots()

        ax.plot([x for x in range(a, b+1)], [f(x) for x in range(a, b+1)])

        rechteckeListe = self._ObersummePlotData(f, a, b, n)

        for r in rechteckeListe:
            print(r)
            ax.add_patch(Rectangle(*r, fill=False, label="obersumme", edgecolor="red"))

        u, o = self.Untersumme(f, a, b, n),self.Obersumme(f, a, b, n)
        print("PLOT_DATA: Untersumme: {}, Obersumme: {}, difference: {}".format(u, o, abs(o-u))) 
        plt.show()

    def plotOberUnter(self) -> plt.plot:
        f, a, b, n = self.f, self.a, self.b, self.n
        fig, ax = plt.subplots()

        ax.plot([x for x in range(a, b+1)], [f(x) for x in range(a, b+1)])

        rechteckeListe = self._ObersummePlotData(f, a, b, n)

        for r in rechteckeListe:
            print(r)
            ax.add_patch(Rectangle(*r, fill=False, label="obersumme", edgecolor="red"))

        print("_"*40)       

        rechteckeListe = self._UntersummePlotData(f, a, b, n)

        for r in rechteckeListe:
            print(r)
            ax.add_patch(Rectangle(*r, fill=False, label="untersumme", edgecolor="green"))
        

        u, o = self.Untersumme(f, a, b, n),self.Obersumme(f, a, b, n)
        print("PLOT_DATA: Untersumme: {}, Obersumme: {}, difference: {}".format(u, o, abs(o-u))) #abs(max(inte-u,inte-o))))
        plt.show()

import re


def lambda_parse(expression:str, safe_dict:dict={"+":1,"-":1,"/":2,"*":2}, oneSymbolRule=True):
    rex = re.compile("^[a-zA-Z]$")
    rex2 = re.compile("^[0-9]+$")

    safe_op_list = list(safe_dict.keys())
    expression_op_list = [op for op in expression if rex.match(op)]
    #if sum([1 for i in [(expression.split(x)) for x in expression if x in safe_op_list][0] if len(i) > 1 and not rex2.match(i)]) != 0:
    #    return ValueError(f"SyntaxError: too many characters! {[(1,i) for i in [(expression.split(x)) for x in expression if x in safe_op_list][0] if len(i) > 1 and not rex2.match(i)]}")

    expression_op_split = [(expression.split(x)) for x in expression if x in safe_op_list]
    # print(expression_op_split)

    inc = 0
    for i in expression_op_split:
        for x in i:
            inc += 1
            if x == "" and inc == len(i):
                return ValueError("Error 0")
            elif x != "" and not rex.match(x) and not rex2.match:
                return ValueError("Error Lost")
            #print("NAN" if x == "" else x)

         
    open_braces = 0
    for i in expression:
        if i == "(":
            open_braces += 1
        elif i == ")":
            open_braces -= 1
        elif i != ")" and i != "(" and not rex.match(i) and not rex2.match(i) and i not in safe_op_list:
            return ValueError(f"SyntaxError: invalid decimal literal {i}")
    if open_braces != 0:
        return ValueError("SyntaxError: braces do not close properly!")

    expression_split = [(expression.split(x), x) for x in safe_op_list]
    for part_list, op in expression_split:
        count = part_list.count("")
        #print(part_list)
        if count > safe_dict[op]-1:
            #index = sum([len(s) for s in part_list[:]])
            #index_str = expression[0:index] +"<-!" + expression[index:]
            return ValueError(f"SyntaxError: Operant {op}")#, expression @ {index_str}"
    
    expression_op_list_cleaned = list(set(expression_op_list))
    if oneSymbolRule and len(expression_op_list_cleaned) > 1: 
        return ValueError("ERROR: oneSymbolRule set to True!")
    str_op = ",".join(expression_op_list_cleaned)
    print(f"lambda {str_op}:{expression}")
    return eval(f"lambda {str_op}:{expression}")
