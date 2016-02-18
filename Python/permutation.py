import numpy
import Stringperm

def main():
	str1=raw_input("Enter String1 ")
	str2=raw_input("Enter String2 ")
	
	Object1= StringPerm(str1)
        Object2= StringPerm(str2)
        array1= Object1.getArray()
        array2= Object2.getArray()
	
	if not str1:
		print("don't write empty string")

	elif len(str1) != len(str2):
                print (" diferent lengths hence not perm")

	else:
		for i in range(len(Object1.getArray())):
			if array1[i] != array2[i]:
				print("not permuation")
				break
			else:
				if i== len(array1):
					print("it's a perm")

			

if __name__=="__main__": main()
