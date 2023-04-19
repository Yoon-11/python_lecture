class Fried:
    def fry(self, min, src='없음'):
        print(min, '분 튀김, 소스:', src, '\n')


chicken = Fried()
shrimp = Fried()

chicken.fry(4, '갈비소스')
chicken.fry(5)
chicken.fry(5, '매운소스')
chicken.fry(6, '양념소스')

shrimp.fry(7, '갈비소스')
shrimp.fry(7)
