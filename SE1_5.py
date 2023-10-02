#開発者作成部分
class MyMax:
    def __init__(self, a):
        self.__max = a[0]
        self.__index = []
        for j in range(1, len(a)):
            if a[j] > self.__max:
                self.__max = a[j] 
        
        for j in range(1, len(a)):
            if a[j] == self.__max:
                self.__index.append(j)
                
        #self.__index を　一応tupleにしておく
        self.__index = tuple(self.__index)
                    
    def getMax(self):
        return self.__max
    
    def getIndex(self):
        self.__index = self.__index
        return self.__index
    
    def getMaxIndex(self):
        return (self.__max, self.__index)
    
    
#ユーザ利用部分
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 4, 10, 2, 1, 10]
b_instance = MyMax(b)
b_max_index = b_instance.getMaxIndex()
print('(max, index)=', b_max_index)