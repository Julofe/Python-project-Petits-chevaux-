import tkinter as Tkinter

#Taille
S_WIDTH=36
S_HEIGHT=36

#Nombre
AREA = 15



#Couleurs

C0= "gray20"  


C1 = "blue1"			


C2 = "red1"


C3 = "green1"


C4 = "yellow1"



COLOR = [C1, C2, C3, C4]





# coords des routes
def tracks(x, y):
	return [x.format(i) for i in y]

#Création des routes
R = []
R+= tracks("6.{}", range(6))[::-1]
R+= ['7.0']
R+= tracks("8.{}", range(6))
R+= tracks("{}.6", range(9,15))
R+= ['14.7']
R+= tracks("{}.8", range(9,15))[::-1]
R+= tracks("8.{}", range(9,15))
R+= ['7.14']
R+= tracks("6.{}", range(9,15))[::-1]
R+= tracks("{}.8", range(6))[::-1]
R+= ['0.7']
R+= tracks("{}.6", range(6))

ER=[]
ER.append(tracks("7.{}", range(1,7)))
ER.append(tracks("{}.7", range(8,14))[::-1])
ER.append(tracks("7.{}", range(8,14))[::-1])
ER.append(tracks("{}.7", range(1,7)))

ROOT1=R[8:]+R[:7]+ER[0]+['7.6']	 
ROOT2=R[21:]+R[:20]+ER[1]+['8.7'] 
ROOT3=R[34:]+R[:33]+ER[2]+['7.8'] 
ROOT4=R[47:]+R[:46]+ER[3]+['6.7'] 

# Station
STATIONS=[]
STATIONS.append(['11.2','12.2','11.3','12.3'])
STATIONS.append(['11.11','12.11','11.12','12.12'])
STATIONS.append(['2.11','3.11','2.12','3.12'])
STATIONS.append(['2.2','3.2','2.3','3.3'])

EQUIPE = []
EQUIPE.append(["C{}".format(i) for i in STATIONS[0]]+["C{}".format(i) for i in STATIONS[3]])
EQUIPE.append(["C{}".format(i) for i in STATIONS[1]]+["C{}".format(i) for i in STATIONS[2]])

OVALE = [
(ROOT1, STATIONS[0], C1, "A"),
(ROOT2, STATIONS[1], C2, "B"),
(ROOT3, STATIONS[2], C3, "B"),
(ROOT4, STATIONS[3], C4, "A"),
]



# Stops
STOPS = [
'8.1',
'12.6',
'13.8',
'8.12',
'6.13',
'2.8',
'1.6',
'6.2',
]



#Création des routes
class Board(Tkinter.Canvas):
	def __init__(self, *args, **kwargs):
		Tkinter.Canvas.__init__(self, *args, **kwargs)
		self.create_squares()
		self.highlight()
		self.configure(width=S_WIDTH*AREA, height=S_HEIGHT*AREA)


	
	def highlight(self):

		
		for c in R:
			self.itemconfigure(c, fill=C0, activewidth=2, activefill=C0, activeoutline="black")

		
		for n,k in enumerate(ER):
			for j in k:
				self.itemconfigure(j, fill=COLOR[n], activewidth=2, activeoutline='black')


		
		for n,s in enumerate(STATIONS):
			for j,c in enumerate(s):
				self.itemconfigure(c, fill=COLOR[n], activewidth=2)
				coordinates = self.coords(c)
		    
		
		
		for s in STOPS:
			self.itemconfigure(s, fill="gray45", activefill="gray70", activewidth=3, activeoutline="gray10")
		return

	
	def create_squares(self):
		for i in range(AREA):
			for j in range(AREA):
				self.create_rectangle(S_WIDTH*i, S_HEIGHT*j, (S_WIDTH*i)+S_WIDTH,(S_HEIGHT*j)+S_HEIGHT, tag="{}.{}".format(i,j), outline='white', fill="white")
#				
		return



if __name__=="__main__":
	root = Tkinter.Tk()
	c = Board(root, width=S_WIDTH*AREA, height=S_HEIGHT*AREA)
	c.pack(expand=True, fill="both")
	root.mainloop()
