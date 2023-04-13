import tkinter as tk
from tkinter import ttk

class Node:
    def __init__(self, Character):
        self.charc = Character
        self.children = [None]*26
        self.Last = False

class Dictionary:
    def __init__(self):
        self.root = Node("Universal Node")

    def Add_Word(self, root, Word):
        root = self.root
        for charc in Word:
            N = Node(charc)
            Index = self.Index_To_Add(charc)
            # print(Index)
            if root.children[Index] == None:
                root.children[Index] = N
                root = root.children[Index]
            else:
                root = root.children[Index]
        N.Last = True
        # print(N.Last)


    def Index_To_Add(self, Variable):
        List = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        for elem in List:
            if Variable == elem:
                return List.index(elem)

    def Search(self, word):
        root = self.root
        ans = False
        for charc in word:
            Index = self.Index_To_Add(charc)
            if root.children[Index] == None:
                return False
            if root.children[Index].charc == charc:
                ans = True
                root = root.children[Index]
                continue
        return ans

    def Get_Character(self, List):
        for i in range(len(List)):
            if List[i] != None:
                return List[i].charc


    def Suggestion(self, Charc):
        Suggest_Word = ""
        root = self.root
        Index = self.Index_To_Add(Charc)
        word = root.children[Index]
        if root.children[Index] == None:
            return
        else:
            while word.Last != True:
                Suggest_Word += word.charc
                root = word
                Next = self.Get_Character(word.children)
                Index = self.Index_To_Add(Next)
                word = root.children[Index]
        Suggest_Word += word.charc
        return Suggest_Word

    def Print(self, word):
        root = self.root
        for charc in word:
            index = self.Index_To_Add(charc)
            while root.children[index] != None:
                print(root.charc)
                # Index = self.Index_To_Add(charc)
                root = root.children[index]

    def display(self,word):
        temp = self.root
        for i in word:
            index = self.Index_To_Add(i)
            print(temp.children[index].charc)
            temp = temp.children[index]

MyDict = Dictionary()
MyDict.Add_Word(MyDict.root,"ehtesham")
MyDict.Add_Word(MyDict.root,"tanzel")
MyDict.Add_Word(MyDict.root,"abubakar")
MyDict.Add_Word(MyDict.root,"khan")
MyDict.Add_Word(MyDict.root,"saqib")
MyDict.Add_Word(MyDict.root,"hanif")
MyDict.Add_Word(MyDict.root,"badshah")


# MyDict.Print("attiq")
# MyDict.display("attiq")
# print(MyDict.root.children[0].children[19].charc)
print(MyDict.Search("abubaaa"))

print(MyDict.Suggestion("a"))

List = []
def key_handler(event=None):
    word = ""
    if event:
        word += t.get()
    if len(word) >= 0:
        List.insert(0, MyDict.Suggestion(word))
        
        
def changeMonth():
    if len(List) >= 1:
        comboExample["values"] = List[0]
        List.clear()


r = tk.Tk()
t = tk.Entry(r)
r.geometry('300x200')
labelone = tk.Label(r,text = "Predicted words")
labelTwo = tk.Label(r,text = "Enter your text")

comboExample = ttk.Combobox(r, 
                            values= List,
                            postcommand=changeMonth)

labelone.grid(row=0,column=0)
t.grid(row=0,column=1)
comboExample.grid(row=1,column=1)
labelTwo.grid(row=1,column=0)

r.bind('<Key>', key_handler)


r.mainloop()