import numpy
class Checker:
	def __init__(self, str1, str2):
		self.str1= str1
		self.str2=str2

	def checkUnique(self):

		if self.str2=="yes":
			list=numpy.zeros((256,1), dtype=bool)
			for c in self.str1:
				if(list[ord(c)]):
					return 0
			return 1
		elif self.str2== "no":
			for i in range(len(self.str1)):	
				for j in  range(i+1,len(self.str1)):
					if self.str1[i]==self.str1[j]:
						return 0
			return 1


def main():
	str1=raw_input("Enter your String:\n ")
	str2=raw_input("Do you want to use data structure?Answer in yes or no \n ") 
	
	test= Checker(str1, str2)
	if test.checkUnique():
		print("has all unique characters")
	else:
		print("repeating characters")
	
	
if __name__=="__main__": main()	
