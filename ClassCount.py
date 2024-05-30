class Sample():
    cnt=0
    def __init__(self,name):
        self.name=name
        Sample.cnt+=1
    @property
    def get_count(self):
        return self.cnt
    def __del__(self):
        Sample.cnt-=1

o1=Sample('kim')
o2=Sample('ff')
print(Sample.cnt)

del o2
print(o1.get_count)
