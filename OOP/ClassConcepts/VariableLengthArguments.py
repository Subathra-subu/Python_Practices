class Example:
    def methods(self,a,b=None):
        if b is None:
            print(f"Single arguemnts:{a}")
        elif isinstance(a,int) and isinstance(b,int):
            print(f"Two integers:{a},{b}")
        elif isinstance(a,str) and isinstance(b,str):
            print(f"Two Strings:{a},{b}")
        else:
            print(f"Mixed types:{a},{b}")
obj = Example()

obj.methods(1)
obj.methods(1,2)
obj.methods("Suba","Karthika")
obj.methods(1,"Hello")