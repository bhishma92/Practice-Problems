
class Duck:
	def __init__(self,**kwargs):
		self.variables = kwargs
	
	def set_variable(self, k, v):
		self.variables[k]=v #set dictionary variables
	
	def get_variables(self,k):
		return self.variables.get(k, None) #None is the default value
def main():
	donald= Duck(feet=2)
	print(donald.get_variables('feet'))

	
if __name__=="__main__": main()

