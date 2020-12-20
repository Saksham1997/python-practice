import pdb
class node:
    def __init__(self,data=None):
        self.data=data
        self.next=None


class linked_list:
    def __init__(self):
        self.head=node()

    def append(self,data):
        new_node=node(data)
        cur=self.head
        while cur.next!=None:
            cur=cur.next
        cur.next=new_node

    def display(self):
        lis=[]
        cur_node=self.head
        while cur_node.next!=None:
            cur_node = cur_node.next
            lis.append(cur_node.data)
        print(lis)

    def length(self):
        cur=self.head
        length=0
        while cur.next!=None:
            cur=cur.next
            length+=1
        return length

    def index_pos(self,index):
        if index>=self.length() or index<0:
            print ("ERROR:index out of range")
            return None
        cur_index=0
        cur_node=self.head
        for i in range(0,index):
            cur_node = cur_node.next
        return cur_node.data

    def insert_at_pos(self,index,data):
        print("The Length of the list currently is {}".format(self.length()))
        cur=self.head
        for i in range(0,index-1):
            cur=cur.next
        #pdb.set_trace()
        new_node=node(data)
        new_node.next = cur.next
        cur.next=new_node


my_list = linked_list()
print("Before putting any elements {}".format(my_list.display()))

my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)
my_list.display()
print("the number at 2 is {}".format(my_list.index_pos(2)))
my_list.insert_at_pos(2,70)
my_list.display()
