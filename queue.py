class Queue:
  def __init__(self,cap=5):
    self._a=[None for _ in range(cap)]
    self._front=0
    self._rear=-1
    self._c=0
  def peek(self):
    if self.isempty():
      return "No Elements"
    return self._a[self._front]
  def enqueue(self,data):
    if self.isfull():
      print("overflow")
    else:
      self._a[self._c]=data
    self._c+=1

  def rear(self):
    if self.isempty():
      return "No Elements"
    else:
      return self._a[self._c-1]
  
  def dequeue(self):
    if self.isempty():
      return "Underflow"
    else:
      data = self._a[self._front]
    for i in range(1,self._c):
      self._a[i-1]=self._a[i]
    self._a[self._c-1] = None
    self._c -= 1
    return f"{data} is dequeued"
  def isempty(self):
    return self._c==0
  def isfull(self):
    return self._c==len(self._a)
    




queue=Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
D=queue.dequeue()
print(D)
print(queue.peek())
print(queue.rear())