'''Class Node
    has two values dataval and pointer to next node
'''
class Node:
    def __init__(self, dataval = None):             
        self.dataval = dataval
        self.nextval = None
'''Class SLinedList
    has headval which is the value at the start of linked list
'''
class SLinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):                            #function that prints list
        printval = self.headval                     #set printval to value at the start
        while printval is not None:                 #while start of list is not none (list not empty)
            print (printval.dataval)                #print data value inside head value 
            printval = printval.nextval             #print next value
            
    def AtBeginning(self,newdata):                  #function that inserts value at begging of list
        NewNode = Node(newdata)                     #pass the data to node instance (create new node) and set it to variable NewNode

    def AtEnd(self, newdata):                       #function that inserts value at end of list
        NewNode = Node(newdata)                     #set the new data passed as arguement to node and contain it inside NewNode variable
        if self.headval is None:                    #if linked list is empty
            self.headval = NewNode                  #set NewNode as start of list
            return
        last = self.headval                         #assign variable last to head node
        while(last.nextval):                        #while there are next nodes after last node
            last = last.nextval                     #set last as the value next to previous last
        last.nextval = NewNode                      #NewNode is the last node
        
    def Insert(self,val_before,newdata):            #function takes val_before and newdata as argument and inserts newdata after val_before
        if val_before is None:                      #if there is no value before
            print("No node to insert after")        #print no node to insert after
        else: 
            NewNode = Node(newdata)                 #else assign variable NewNode to instance of object node with newdata
            val_before = list.headval.nextval       #instance list of linked list second value is val_before
            NewNode.nextval = val_before.nextval    #link new node next value with value before next value (change arrows)
            val_before.nextval = NewNode            #set the pointer from val_before to point at NewNode
            return


list = SLinkedList()
list.headval = Node("Mon")

e2 = Node("Tue")
e3 = Node("Thur")
e4 = Node("Fri")
e5 = Node("Sat")
list.headval.nextval = e2
e2.nextval = e3
e3.nextval = e4
e4.nextval = e5


list.AtEnd("Sun")
list.Insert("Tue","Weds")
list.listprint()
