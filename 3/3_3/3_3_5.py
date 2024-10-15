class LinkedList:
    def __init__(self):
        self.count = 0
        self.head = None
        self.tail = None

    def __call__(self, *args, **kwargs):
        n = 0
        cur_el = self.head
        while n != args[0]:
            cur_el = cur_el.next
            n += 1
        return cur_el.data

    def __len__(self):
        return self.count

    def add_obj(self, obj):
        self.count += 1
        if self.head is None:
            self.head = self.tail = obj
        else:
            self.tail.next = obj
            obj.prev = self.tail
            self.tail = obj

    def remove_obj(self, indx):
        self.count -= 1
        cur_el = self.head
        n = 0
        while n != indx:
            cur_el = cur_el.next
            n += 1
        prev_el = cur_el.prev
        next_el = cur_el.next
        if prev_el is not None:
            if next_el is not None:
                prev_el.next = next_el
                next_el.prev = prev_el
            else:
                prev_el.next = next_el
                self.tail = prev_el
        elif next_el is not None:
            next_el.prev = prev_el
            self.head = next_el

        else:
            self.head = self.tail = None


class ObjList:
    def __init__(self, data):
        self.__data = data
        self.__prev = None
        self.__next = None

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, value):
        self.__prev = value

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        self.__next = value

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value


linked_lst = LinkedList()
linked_lst.add_obj(ObjList("Sergey"))
linked_lst.add_obj(ObjList("Balakirev"))
linked_lst.add_obj(ObjList("Python"))
linked_lst.remove_obj(2)
linked_lst.add_obj(ObjList("Python ООП"))
n = len(linked_lst)
print(n)# n = 3
s = linked_lst(1) # s = Balakirev
print(s)