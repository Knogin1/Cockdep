import random as rand
points = ['Race','Origin','Class','Back','Stats']

def roll():
    A = []
    print("\nСтаты:    ", end = '')
    for s in range(0,6):
        num = [rand.randint(1,6),rand.randint(1,6),rand.randint(1,6),rand.randint(1,6)]
        num.sort(reverse = True)
        A.append(num[0]+num[1]+num[2])
    A.sort(reverse = True)
    for s in range(0,6):
        print(str(A[s]), end = ' ') 
    
while 1:
    print("*******************")
    pick2 = None
    ili = " или "
    origin = rand.randint(0,1)
    for s in range(len(points)):
        lines = len(open('DND_'+points[s]+'.txt','r').readlines())
        pick = rand.randint(1,lines)

        if s == 0:
            print("Раса:    ", end='')
            
        if s == 1 and origin == 0:
            continue
        elif s == 1 and origin == 1:
            print("Происхождение:    ", end='')
            
        if s == 2:
            print("Класс:    ", end='')
            pick2 = rand.randint(1,lines)

        if s == 3:
            print("Предыстория:   ", end='')
            
        if s == 4:
            print("Наименьшая характеристика: ", end='')
            pick2 = rand.randint(1,lines)
            while pick2 == pick:
                pick2 = rand.randint(1,lines)
        
        try:
            for q,A in enumerate(open('DND_'+points[s]+'.txt','r')):
                if s == 4:
                    if q == pick - 1:
                        print(A.rstrip()+ ili, end ='')
                        ili = ''
                    if q == pick2 - 1:
                         print(A.rstrip()+ ili, end ='')
                         ili = ''
                    
                elif q == pick-1:
                    print(A.rstrip())
        finally:
            open('DND_'+points[s]+'.txt','r').close()
    roll()
    print("\n*******************")
    input()   
