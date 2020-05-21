#Defining the variables

class No(object):
    def __init__(self, x, x2, bef, nex):
        self.x = int(x)
        self.x2 = x2
        self.bef = bef
        self.nex = nex

class doublyLinkedList(object):
    head = None
    foot = None

#search and print on screen the text

def search(textList,idList,text):
    j = 0
    for i in text:
        for j in range(len(textList)):
            if i == textList[j]:
                print(idList[j], end='')
            
# add knots

def add(self, x, x2):
    new_knot = Knot(x,x2, None, None)
    i = self.head
    if self.head is None:
        self.head = new_knot
        self.foot = new_knot
    else:
        if x > int(self.head.x):
            new_knot.nex = self.head
            self.head.bef = new_knot
            self.head = new_knot
        else:
            v = int(self.head.x)
            while x < v or x == v:
                if i == self.foot:
                    i.nex = new_knot
                    new_knot.bef = i
                    self.foot = new_knot
                    break
                else:
                    if i.nex is not None:
                        i = i.nex
                        v = int(i.x)
            if x > v:
                new_knot.nex = i
                new_knot.bef = i.bef
                i.bef.nex = new_knot
                i.bef = new_knot

#create the tree                    

def tree(self, textList, idList):
    if self.foot.nex == None:
        self.foot.x = self.foot.x+self.foot.bef.x
        textList.append(self.foot.x2)
        idList.append('1')
        textList.append(self.foot.bef.x2)
        idList.append('0')
        self.foot = self.foot.bef
        self.foot.nex.bef = self.foot.x2
        self.foot.nex.nex = self.foot.nex.x2
        self.foot = self.foot.bef
        self.foot.nex = self.foot.nex.nex
        print('Hello')
        i = 2
        j = i
        k = i
    while True:
        if self.foot == self.head:
            self.foot.bef = self.foot.x2
            textList.append(self.foot.x2)
            idList.append('0')
            for j in range(i):
                    idList[j] = '1' + idList[j]
            break
        else:
            a = self.foot.bef.x
            b = self.foot.nex.x
            if a > b:
                self.foot.x = self.foot.x+self.foot.nex.x
                textList.append(self.foot.x2)
                idList.append('0')
                for o in range(i):
                    idList[o] = '1' + idList[o]
                i = i+1
                j = i+1
                self.foot = self.foot.bef
                self.foot.nex.bef = self.foot.nex.x2
            else:
                new_knot = Knot(self.foot.x+self.foot.bef.x, None, self.foot.x2, self.foot.bef.x2)
                self.foot = self.foot.bef
                self.foot.nex.bef = new_knot
                self.foot.nex.x = self.foot.nex.x+self.foot.x
                textList.append(self.foot.x2)
                idList.append('00')
                textList.append(self.foot.nex.x2)
                idList.append('01')
                for j in range(k):
                    idList[j] = '1' + idList[j]
                k = k+1
                self.foot = self.foot.bef

# go through

def through(self):
    i = self.head
    while i != self.foot:
        i = i.nex
    
#compare
def compare(self,x2):
    knot_this = self.head
    while knot_this is not None:
        if str(knot_this.x2) == x2:
            return True
            break
        else:
            knot_this = knot_this.nex  
    if knot_this is None:
        return False


#count
def count(text):
    c = bool
    j = 0
    list2 = doublyLinkedList()
    textList = []
    idList = []
    for i in text:
        c = compare(list2,i)
        if c == False:
            add(list2,text.count(i),i)
    tree(list2,textList,idList)
    print('Compare table:')
    for j in range(len(idList)):
        print('|*|'+idList[j]+'|*||*|'+idList[j]+'|*|')
        j = j+1
    print('Compressed code:')
    search(textList,idList,text)


text = str(input('\nType the word: '))
print('Text: |',text,'| Compressed: ')
count(texto)