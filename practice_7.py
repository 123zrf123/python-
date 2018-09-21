#栈的基本操作
class Stack(object): 
    """模拟栈""" 
    def __init__(self): 
        self.items = [] 
 
    def isEmpty(self): 
        return len(self.items)==0  
 
    def push(self, item): 
        self.items.append(item) 
 
    def pop(self): 
        return self.items.pop()  
 
    def peek(self): 
        if not self.isEmpty(): 
            return self.items[len(self.items)-1] 

    def top(self):
        if len(self.items) == 0:
            return 'Empty Queue'
        return self.items[0]
    
    def size(self): 
        return len(self.items) 

s=Stack() 
print(s.isEmpty()) 
s.push(1) 
print(s.pop())
s.push(2)
s.push(3)
print(s.top())
print(s.pop())
#print(s.peek()) 
#s.push(True) 
#print(s.size()) 
#print(s.isEmpty()) 
print(s.size())