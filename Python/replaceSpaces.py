ßœimport numpy
import Stringperm

class StringReplace:
	def __init__(self, str):
		self.str=str
	def changeWhite(self):
		string=self.str.replace(" ", "%20")
		return string

def main():
	str=raw_input("enter the string: \n")
	Ob1=StringReplace(str)
	print(Ob1.changeWhite())

if __name__=="__main__": main()
