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
"""
    def index_pos(self,index):
        if index>=self.length() or index<0:
            print ("ERROR:index out of range")
            return None
"""


my_list = linked_list()
print("Before putting any elements {}".format(my_list.display()))

my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)
my_list.display()
