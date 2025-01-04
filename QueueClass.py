"""Класс узла"""
class Node:
    """Метод инициализации узла"""
    def __init__(self,data,next_node = None):
        self.data = data
        self.next_node = next_node

class Queue:
    """Метод инициализации очереди"""
    def __init__(self,head = None, tail = None,queue_size = 5):
        self.head = head
        self.tail = tail
        self.queue_size = queue_size

    """Метод добавления элемента в очередь"""
    def enqueue(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next_node = new_node
        self.tail = new_node

    """Метод удаления элемента из очереди"""
    def dequeue(self):
        if self.head is None:
            return None
        else:
            dequeue_items = self.head
            self.head = self.head.next_node
        return dequeue_items.data
    """Метод определения длины очереди"""
    def get_queue_length(self):
        items_count = 0
        if self.head is None:
            return items_count
        temp_head = self.head
        while temp_head:
            items_count += 1
            temp_head = temp_head.next_node
        return items_count
    """Метод определяющий наличие каких либо элементов в очереди"""
    def isEmpty(self):
        if self.head is None:
            return 'Очередь пуста'
        else:
            return "Очередь не пуста"

    """Метод определения наполненности очереди"""
    def is_queue_full(self):
        if self.queue_size == self.get_queue_length():
            return True
        return False
    """Метод показывающий все элементы очереди"""
    def show_queue(self):
        if not self.isEmpty():
            temp_head = self.head
            while temp_head:
                print(temp_head.data)
                temp_head = temp_head.next_node
            return "Очередь показана"
        return "Очередь пуста"