class Netfix:
    def __init__(self,name,cast,plot,rating,budget):
        self.name = name
        self.cast = cast
        self.plot = plot
        self.rating = rating
        self.budget = budget

class Movie(Netfix):
    def __init__(self,name,cast,plot,rating,budget,dur):
        Netfix.__init__(self,name,cast,plot,rating,budget)
        self.dur = dur

class Series(Netfix):
    def __init__(self,name,cast,plot,rating,budget,no_of_ep):
        Netfix.__init__(self,name,cast,plot,rating,budget)
        self.no_of_ep = no_of_ep

class Serial(Netfix):
    def __init__(*parent,`no_of_ep):
        Netfix.__init__(*parent)
        self.no_of_ep = no_of_ep

dhamaal = Movie('Dhamaal',['Arshad Varsi','Sanjay Dutt'],'plot1','5 star',11213123,'2.5 hrs')
print(dhamaal.name)

panchayat = Series('Panchayat',['Jitendra Kumar'],'plot2','5star',342424,5)
print(panchayat.name)

sr1 = Serial('CID',['DAYA','Abhijeet'],'plot2','5star',342424,5)
