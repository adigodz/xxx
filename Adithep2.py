class CircularQueue:
    def __init__(self, n):
        self.n = n
        self.queue = [None] * n 
        self.front = -1
        self.rear = -1

    def enqueue(self, data):
        if ((self.rear + 1) % self.n == self.front):
            print('เพิ่มข้อมูลไม่ได้เพราะคิววงกลมเต็ม')
        elif (self.front == -1):
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data 
        else:
            self.rear = (self.rear + 1) % self.n
            self.queue[self.rear] = data 

    def dequeue(self):
        if (self.front == -1):
            print('ลบข้อมูลไม่ได้เพราะคิววงกลมว่าง')
        elif (self.front == self.rear):
            data = self.queue[self.front]
            self.front = -1
            self.rear = -1
            return data
        else:
            data = self.queue[self.front]
            self.front = (self.front + 1) % self.n
            return data

    def display(self):
        if (self.front == -1):
            print('แสดงข้อมูลไม่ได้เพราะคิววงกลมว่าง')
        else:
            i = self.front
            while i != self.rear:
                if self.queue[i] is not None and self.queue[i] < 150:
                    print(self.queue[i])
                i = (i + 1) % self.n
            if self.queue[self.rear] is not None and self.queue[self.rear] < 150:
                print(self.queue[self.rear])

n = int(input('โปรดระบุขนาดของคิววงกลมที่มีขนาดตั้งแต่ 5 ช่อง: '))
while n <= 4:
    n = int(input('โปรดระบุขนาดของคิววงกลมที่มีขนาดตั้งแต่ 5 ช่อง: '))
q = CircularQueue(n)

while True:
    print("\nโปรดระบุทางเลือกการดำเนินการ:")
    print("1. รับข้อมูลตัวเลขจำนวนเต็มเพื่อจัดเก็บในคิววงกลม")
    print("2. ลบข้อมูลที่จัดเก็บในคิววงกลม")
    print("3. แสดงข้อมูลตัวเลขจำนวนเต็มที่มีค่าน้อยกว่า 150 ที่จัดเก็บในคิววงกลม")

    choice = int(input("ทางเลือกในการดำเนินการ: "))

    if choice == 1:
        data = int(input("ข้อมูลที่ต้องการจัดเก็บในคิววงกลม: "))
        q.enqueue(data)
    elif choice == 2:
        data = q.dequeue()
        if data is not None:
            print(f'ข้อมูลที่ถูกลบ: {data}')
    elif choice == 3:
        q.display()
    else:
        print("สิ้นสุดโปรแกรม")
        break