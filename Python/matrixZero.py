#import numpy

class DeleteRCZero:
	"""docstringeRCZerome"""
	def __init__(self, arg):
		self.arg = arg
		
	def delRC(self):
		
		#arr=[ False for i in range(len(self.arg[0])) for j in range(len(self.arg))]
		
		arr=[ [True if '0' in self.arg[i][j] else False for i in range(len(self.arg))] for j in range(len(self.arg[0])) ]
		
		#self.arg=[0 for x in self.arg[i] for y in self.arg[:,j] if True in self.arg[i][j]]

		print(self.arg[0])

		for x in range(len(self.arg)):
			for y in range(len(self.arg[0])):
				
				if(arr[x][y]== True):
					#print(y)
					self.arg[x]=0
					self.arg[:][y]=0


	def output(self):
		for i in range(len(self.arg)):
			print(self.arg[i])
			print('\n')


def main():



	def createMatrix():
		x=input("Enter the length: ")
		y= input("Enter the width")		
		matrix=[[input() for i in range(int(x))] for j in range(int(y))]

		return matrix;
		

	Ob1=DeleteRCZero(createMatrix())
	Ob1.delRC()
	Ob1.output()



if __name__=="__main__":main()	