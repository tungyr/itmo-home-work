class Node:  # Объявление элемента списка в Python
    def __init__(self, value = None, next = None):
        self.value = value  # значение узла
        self.next = next    # ссылка на следующий узел

class LinkedList:   # Исходный код класса Linked List
    def __init__(self, *args, **kwargs):
        self.first = None   # определение головного узла
        self.last = None    # определение конечного узла
        self.length = 0     # определение длины списка

        for argument in args:
            self.add(argument)

    def __str__(self):
        if self.first is not None:                      # если головной узел не пустой
            current = self.first                        # текущий = головной узел
            out = 'LinkedList [' + str(current.value)   # список = значение текущего узла
            while current.next is not None:             # пока ссылка на следующий узел не пуста
                current = current.next                  # текущий = ссылка на текущий
                out += str(current.value)               # список + значение текущиего узла
            return out + ']'
        return 'LinkedList []'

    def add(self, x):  # Добавление элементов в конец списка
        if self.first == None:          # если список новый и головного узла еще нет
            self.first = Node(x, None)  # головной узел
            self.last = self.first      # конечный узел = головному узлу - список из одного элемента
            self.length = 1
        elif self.last == self.first:   # если конечный узел = головному узлу
            self.last = Node(x, None)   # добавляем новое значение в конец спискка
            self.first.next = self.last # назначаем ссылку первого узла на последний
            self.length += 1
        else:
            current = Node(x, None)     # определяем текущий узел
            self.last.next = current    # назначаем ссылку конечного узла на текущий узел
            self.last = current         # конечный узел = текущий узел
            self.length += 1

    def insert(self, i, x):
        if self.first is None:
            self.first = Node(x, None)
            self.last = self.first
            return

        if i == 0:
            self.first = Node(x, self.first)
            return

        if i >= self.length:
            self.add(x)
        else:
            current = self.first
            counter = 0
            while current is not None:
                counter += 1
                if counter == i:
                    current.next = Node(x, current.next)
                if current.next.next == None:
                    self.last = current.next
                    break
                current = current.next


    def get(self, index):
        if index >= self.length:
            raise IndexError
        counter = 0
        item = self.first
        while item is not None:
            counter += 1
            if (counter - 1) == index:
                return item.value
            item = item.next


    def remove(self, sign):
        item = self.first
        prev_item = self.first
        while item != None:
            if item.value == sign:
                self.length -= 1
                if item.next == None:
                    prev_item.next = None
                else:
                    item.value = item.next.value
                    item.next = item.next.next
                break
            prev_item = item
            item = item.next

    def remove_at(self, index):
        if index >= self.length:
            raise IndexError()
        elif index == 0:
            self.first = self.first.next
            self.length -= 1

        else:
            counter = 0
            item = self.first
            while item.next != None:
                counter += 1
                if counter == index:
                    res = item.next.value
                    item.next = item.next.next
                    self.length -= 1
                    return res
                item = item.next



    def clear(self):
        self.__init__()

    def contains(self, check):
        if self.first is None:
            return
        else:
            item = self.first
            while item is not None:
                if item.value == check:
                    return True
                item = item.next
            return False

    def is_empty(self):
        if self.length == 0:
            return True

        return False

    def len(self):
        return self.length


    def __next__(self):
        if not self._iter:
            self.__iter__()
        return next(self._iter)

    def __iter__(self):
        if not self.length == 0:
            item = self.first
            while item:
                yield item.value
                item = item.next

# ll = LinkedList(1, 2, 3, 4, 5)
# print(ll)
# ll.add(6)
# print(ll)
# ll.insert(0, 6)
# print(ll)
# ll.insert(100, 666)
# print(ll)
# print(ll.get(0))
# print(ll.get(4))
# ll.get(100)

# ll.remove(2)
# ll.remove_at(4)
# print(ll)
# ll.remove_at(100)
#
# print(ll.contains(3))
# ll.contains(100)
#
# print(ll.len())
#
# ll.is_empty()
#
# ll.clear()
# # ll.is_empty()
#
# ll2 = LinkedList('item1', 'item2', 'item3')
# for item in ll2:
#     print(item)
