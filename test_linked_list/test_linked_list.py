import unittest

from LinkedListClass import LinkedList

class TestLinkedListClass(unittest.TestCase):
    linked_list = LinkedList()

    def test_1_init(self):
         self.assertEqual(self.linked_list.__init__(),None)

    def test_2_insert_at_head(self):
        self.assertEqual(self.linked_list.insert_at_head('top_data'), "Узел с данными top_data добавлен в начало списка")

    def test_3_insert_at_end(self):
        self.assertEqual(self.linked_list.insert_at_end('bottom_data'), "Узел с данными bottom_data добавлен в конец списка")

    def test_4_remove_node_position(self):
        self.linked_list.insert_at_head('top_data')
        self.assertEqual(self.linked_list.remove_node_position(1), "Удален узел с данными top_data позиции 1")
        self.assertEqual(self.linked_list.remove_node_position(0), "Удален узел с данными bottom_data позиции 0")
        self.assertEqual(self.linked_list.remove_node_position(0), "Ничего не удалено")

    def test_5_insert_at_position(self):
        self.assertEqual(self.linked_list.insert_at_position('top_data',0), "Узел с данными top_data добавлен на позицию 0")

    def test_6_print_ll(self):
        self.assertEqual(self.linked_list.print_ll(),'Данные списка выведены')

    def test_7_get(self):
        self.assertEqual(self.linked_list.get('top_data'),(True, 'top_data'))

    def test_8_change_data(self):
        self.assertEqual(self.linked_list.change_data('top_data','change_data'), "Заменены данные в узле № 1")