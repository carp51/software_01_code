#開発者作成部分
class MyMax:
    def __init__(self, a):
        self.__max = a[0]
        self.__index = 0
        for j in range(1, len(a)):
            if a[j] > self.__max:
                self.__max = a[j] 
                self.__index = j
                    
    def getMax(self):
        return self.__max
    
    def getIndex(self):
        return self.__index
    
    def getMaxIndex(self):
        return (self.__max, self.__index)
    
    
#ユーザ利用部分
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b_instance = MyMax(b)
b_max_index = b_instance.getMaxIndex()
print('(max, index)=', b_max_index)