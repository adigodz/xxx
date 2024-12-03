class Node:
  def __init__(self, info = None):
    self.info = info
    self.next = None
       
class SLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
  
  def AtTheBegining(self, data):
    if self.head != None:
        NewNode = Node(data)
        NewNode.next = self.head
        self.head = NewNode
    else:
         NewNode = Node(data)
         NewNode.next = None
         self.head = NewNode
         self.tail = NewNode
         
  def AtTheEnd(self, data):
    if self.head == None:
      NewNode = Node(data)
      NewNode.next = None
      self.head = NewNode
      self.tail = NewNode
    else:
      NewNode = Node(data)
      NewNode.next = None
      self.tail.next = NewNode
      self.tail = NewNode
      
  def display(self):
    print(f"ข้อมูลที่จัดเก็บในตำแหน่งที่พอยน์เตอร์ head ชี้ คือ {self.head.info}")
    print(f"ข้อมูลที่จัดเก็บในตำแหน่งที่พอยน์เตอร์ tail ชี้ คือ {self.tail.info}")

#main
slist = SLinkedList()
print("\nโปรดระบุทางเลือกการดำเนินการกับ Singly linked list")
print("B เพิ่มข้อมูลที่จุดเริ่มต้นของ Singly linked list")
print("E เพิ่มข้อมูลแบบต่อจากโหนดสุดท้ายของ Singly linked list")
while True:
    choice = (input("ทางเลือกในการดำเนินการ: "))
    if choice == 'B':
        data = int(input("ตัวเลขที่ต้องการเพิ่ม คือ "))
        slist.AtTheBegining(data)
    elif choice == 'E':
        data = int(input("ตัวเลขที่ต้องการเพิ่ม คือ "))
        slist.AtTheEnd(data)
    else:
        all = slist.display()
        if all:
          print(f"ข้อมูลใน Singly linked ")
        break