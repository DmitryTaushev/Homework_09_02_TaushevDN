import unittest

from QueueClass import Queue

class TestLinkedListClass(unittest.TestCase):
    queue = Queue()

    def test_isEmpty(self):
        self.assertEqual(self.queue.isEmpty(),'Очередь пуста')
        self.queue.enqueue('head_data')
        self.assertEqual(self.queue.isEmpty(), 'Очередь не пуста')



    def test_isFull(self):
        self.assertEqual(self.queue.isFull(),'Очередь не полна')
        self.queue.enqueue('head_data_1')
        self.queue.enqueue('head_data_2')
        self.queue.enqueue('head_data_3')
        self.queue.enqueue('head_data_4')
        self.assertEqual(self.queue.isFull(), 'Очередь полна')

