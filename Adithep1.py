#Lab1
def isEmpty (myStack):
    if len(myStack) == 0:
        print('Stack is empty')
        return 1
    else:
        return 0

def isFull (myStack):
    if len(myStack) == n:
        print('Stack is full')
        return 1
    else:
        return 0

def display_Stack (myStack):
    test = isEmpty(myStack)
    if test == 0:
        print('ข้อมูลที่จัดเก็บใน Stack',myStack)
    else:
        print('แสดงข้อมูลใน Stack ไม่ได้เพราะ Stack ว่าง')

def push_Stack (item, myStack):
    test = isFull(myStack)
    if test == 0:
        print('ข้อมูลที่ต้องการจัดเก็บใน Stack =',item)
        myStack.append(item)
    else:
        print('จัดเก็บข้อมูลไม่ได้เพราะ Stack เต็ม')

def pop_Stack (myStack):
    test = isEmpty(myStack)
    if test == 0:
        myStack.pop()
    else:
        print('ลบข้อมูลไม่ได้เพราะ Stack ว่าง')

def average_Stack(myStack):
    if myStack:
        avg = sum(myStack)/len(myStack)
        print(f"ค่าเฉลี่ยของข้อมูลใน Stack คือ {avg:.2f}")
    else:
        print('แสดงค่าเฉลี่ยของข้อมูลใน Stack ไม่ได้เพราะ Stack ว่าง')

n = int(input('โปรดระบุขนาดของ Stack ที่มีขนาดตั้งแต่ 6 ช่องขึ้นไป : '))
while n <= 5:
    n = int(input('โปรดระบุขนาดของ Stack ที่มีขนาดตั้งแต่ 6 ช่องขึ้นไป : '))  
myStack = []*n

while True:
    print("\nโปรดเลือกการดำเนินการ:")
    print("1. เพิ่มข้อมูล")
    print("2. ลบข้อมูล")
    print("3. แสดงข้อมูลใน Stack")
    print("4. แสดงค่าเฉลี่ยของข้อมูล")
        
    choice = int(input("ทางเลือกในการดำเนินการ: "))
        
    if choice == 1:
        item = float(input("ข้อมูลที่ต้องการจัดเก็บใน Stack : "))
        push_Stack(item,myStack)
    elif choice == 2:
        pop_Stack(myStack)
    elif choice == 3:
        display_Stack(myStack)
    elif choice == 4:
        average_Stack(myStack)
    else:
        print("สิ้นสุดโปรแกรม")
        break
