class Fried:
    def __init__(self, name):
        self.name = name
        self.num = 0

    def fry(self, min, src='없음'):
        self.num += 1
        print(self.name, min, '분 튀김, 소스 : ', src, 'n = ', self.num, '\n')


chicken = Fried('통닭')
shrimp = Fried('새우')

chicken.fry(4, '갈비')
chicken.fry(5)
chicken.fry(8)

shrimp.fry(5)
shrimp.fry(6, '매운')

chicken.fry(6)


