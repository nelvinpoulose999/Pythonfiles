#method over loading
class Math:
    def add(self):
        print('no argments')
    def add(self,num1):
        print('1 arg passed')
    def add(self,num1,num2):
        print('2 arg passed')
math=Math()
math.add(10,20)
math.add(10)
math.add()
