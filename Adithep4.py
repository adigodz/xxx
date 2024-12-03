class Node:
  def __init__(self):
    self.data = None
    self.leftChild = None
    self.rightChild = None

  def insert(self,data):
    self.data = data   
    data = int(input(f'โปรดป้อนหมายเลขของโหนด Left child ของ {self.data} (ถ้าไม่มีให้ป้อนจำนวนเต็มที่มีค่าน้อยกว่าหรือเท่ากับ 0): '))
    if data > 0:
      self.leftChild = Node()
      self.leftChild.insert(data)
        
    data = int(input(f'โปรดป้อนหมายเลขของโหนด Right child ของ {self.data} (ถ้าไม่มีให้ป้อนจำนวนเต็มที่มีค่าน้อยกว่าหรือเท่ากับ 0): '))
    if data > 0:
      self.rightChild = Node()
      self.rightChild.insert(data)
    
  def PreOrder(self, tree):
    if tree:
      if tree.data%2 == 0:
        print(tree.data)
        self.PreOrder(tree.leftChild)
        self.PreOrder(tree.rightChild)
                 
  def InOrder(self, tree):
    if tree:
        self.InOrder(tree.leftChild)
        if tree.data < 150:
          print(tree.data)
          self.InOrder(tree.rightChild)
           
  def PostOrder(self, tree):
    if tree:
        self.PostOrder(tree.leftChild)        
        self.PostOrder(tree.rightChild)
        if tree.data%7 == 0:
          print(tree.data)
        
#main
A = Node()
n = int(input('โปรดป้อนจำนวนเต็มเพื่อจัดเก็บที่ Root node : '))
A.insert(n)

print("\nโปรดระบุทางเลือกการดำเนินการกับ Singly linked list")
print("1. ท่องไปในต้นไม้ทวิภาคแบบ Pre-order และแสดงจำนวนเต็มที่จัดเก็บในแต่ละโหนดที่เป็นเลขคู่ทางจอภาพ")
print("2. ท่องไปในต้นไม้ทวิภาคแบบ In-order และแสดงจำนวนเต็มที่จัดเก็บในแต่ละโหนดที่มีค่าน้อยกว่า 150 ทางจอภาพ")
print("3. ท่องไปในต้นไม้ทวิภาคแบบ Post-order และแสดงจำนวนเต็มที่จัดเก็บในแต่ละโหนดที่หารด้วย 7 ลงตัวทางจอภาพ")

choice = int(input("ทางเลือกในการดำเนินการ: "))
if choice == 1.:
  print('Pre-order = ',end="")
  A.PreOrder(A)
  print()
elif choice == 2.:
  print('In-order = ',end="")
  A.InOrder(A)
  print()
elif choice == 3.:
  print('Post-order= ',end="")
  A.PostOrder(A)
  print()