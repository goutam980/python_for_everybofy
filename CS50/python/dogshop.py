class dogshop():
    def __init__(self,category):
        self.category=category
        self.all=[]
    
    def add(self):
        n=input("how much pet u have")
        n=int(n)
        for i in range(n):
            self.category=input("enter pet category")
            self.name=input("enter pet name")
            self.all.append(self.category)
            self.all.append(self.name)
        print("all done dro")
    def show(self):
        self.all=[
            {self.category:self.name}

        ]

a=dogshop("dog")
a.show()