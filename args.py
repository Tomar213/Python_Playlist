
def args_name(noraml,*args,**fda):
    print(noraml)
    print(f"from Tupple")
    for i in args:
        print(i,end=" ")
    print("\nFrom Dictionary")
    for key, value in fda.items():
        print(f"\nName - {key} occupation - {value}")    

normmal = "jass"
tp =("karan ","singh ","tomar")
dict={"Ishu":"Black board","pooonam":"Monitor","Madhvi":"Fighter"}
args_name(normmal,*tp,**dict)