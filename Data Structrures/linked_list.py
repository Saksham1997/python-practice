import pdb #pdb is python debugger , i have used to debug my code , while i was making it

"""
class representation of the node
node consists of two variables data which holds the data and the next which contains the address of the next node
"""
class node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

"""
Implementation of the linked list is acheived via class over here.
"""

class linked_list:
    def __init__(self):
        self.head=node()

#to add element at the end of the linked list
    def append(self,data):
        new_node=node(data)
        cur=self.head
        while cur.next!=None:
            cur=cur.next
        cur.next=new_node

#to display the linked linkedlist
    def display(self):
        lis=[]
        cur_node=self.head
        while cur_node.next!=None:
            cur_node = cur_node.next
            lis.append(cur_node.data)
        return lis

#To calc the length of the linkedlist
    def length(self):
        cur=self.head
        length=0
        while cur.next!=None:
            cur=cur.next
            length+=1
        return length

#function to display the data at a particular index
    def index_pos(self,index):
        if index>=self.length() or index<0:
            print ("ERROR:index out of range")
            return None
        cur_index=0
        cur_node=self.head
        for i in range(0,index):
            cur_node = cur_node.next
        return cur_node.data

#Function to add the data at a particular index at which user wants
    def insert_at_pos(self,index,data):
        print("The Length of the list currently is {}".format(self.length()))
        cur=self.head
        for i in range(0,index-1):
            cur=cur.next
        #pdb.set_trace()
        new_node=node(data)
        new_node.next = cur.next
        cur.next=new_node

    def delete_node(self,index):
        print("WARNING :Current list is {}, you have decided to delete the node at {}".format(self.display(),index))
        cur=self.head
        if index==1:
            self.head = cur.next
            cur = None
            return
        prev = None
        for i in range(0,index):
            prev = cur
            cur=cur.next
        prev.next = cur.next
        cur = None
        print("DELETION DONE , NOW list is {}".format(self.display()))

my_list = linked_list()
print("Before putting any elements {}".format(my_list.display()))

my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)
my_list.display()
print("the number at 2 is {}".format(my_list.index_pos(2)))
my_list.insert_at_pos(2,70)
print(my_list.display())
my_list.delete_node(2)
