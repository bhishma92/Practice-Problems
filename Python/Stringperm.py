import numpy
class StringPerm:
        def __init__(self,str):
                self.str=str

        def getArray(self):
                arr = numpy.zeros(256, dtype=int)
                for c in self.str:
                        arr[ord(c)]=+1
                return arr
