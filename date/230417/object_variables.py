class Fried:
    num = 0
    def fry(self, min, src='없음'):
        self.num += 1
        print(min, '분 튀김, 소스 : ', src, 'n = ', self.num, '\n')

chicken = Fried()
shrimp = Fried()

chicken.fry(4, '갈비')
chicken.fry(5, '양념')
chicken.fry(6)
print('--------------------')
shrimp.fry(4)
shrimp.fry(6)