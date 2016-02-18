import numpy

class StringCompression:
	def  __init__(self,st):
		self._st=st
		self._out=''
	
	def compress(self):
		var=self._st[0]
		i=0; cnt=0;
		if(len(self._st) ==1): #base case
			self._out += self._st;
		else:
			while(i < len(self._st)):
				if(self._st[i]==var):
					cnt += 1
					i += 1
					if(i==len(self._st)):
						break;

				else:
					self._out += var + str(cnt)
					cnt=0
					var=self._st[i]
					
		self._out += self._st[i-1] + str(cnt)


	def output(self):
		print(min(self._st, self._out, key=len))
		



def main():

	def getf():
		st = raw_input("enter the string: \n")
		return str(st)

	
	Ob1=StringCompression(getf())
	Ob1.compress()
	Ob1.output()
	
        

if __name__=="__main__": main()
                              

