from llist import dllist, dllistnode

class DataLoop:
    DATA = """a@@@@A00000   F2
    b@@@@A   00  0D3
    c@@@@A  0   00D4
    d@@@@A000   0-F2
    e@@@@A000000 w5D"""
    
    def __init__(self):
        self.list = dllist()
        self.populate_list(self.list, self.DATA)
        self.next_node = self.list.first
        
    def populate_list(self, list, data):
        lines = data.strip().split('\n')   

        for l in lines:
            n = dllistnode(l.strip())
            list.append(n)
            
    def size(self):
        return self.list.size
    
    def popleft(self):
        n = self.next_node
        self.next_node = n.next if n.next != None else self.list.first
            
        return n.value
        