#開発者作成部分
class MyMax:
    def __init__(self, a):
        self.__max = a[0]
        for j in range(1, len(a)):
            if a[j] > self.__max:
                self.__max = a[j] 
    
    def getMax(self):
        return self.__max
    
    
#ユーザ利用部分
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b_instance = MyMax(b)
bm = b_instance.getMax()
print('max=', bm)