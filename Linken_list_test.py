from unittest import TestCase, main
# from lislLink.LInkList import LinkedList


class TestLinkedList(TestCase):

    def setUp(self):
        self.list = LinkedList()

    def test_insert_at_head(self):
        self.list.insert_at_head(10)
        self.assertEqual(self.list.head.data, 10)
        self.list.insert_at_head(20)
        self.assertEqual(self.list.head.data, 20)

    def test_insert_at_end(self):
        self.list.insert_at_end(10)
        self.assertEqual(self.list.head.data, 10)
        self.list.insert_at_end(20)
        self.assertNotEqual(self.list.head.data, 20)
        self.assertEqual(self.list.head.next_node.data, 20)

    def test_remove_node_position(self):
        self.list.insert_at_head(10)
        self.list.insert_at_head(20)
        self.list.remove_node_position(1)
        self.assertEqual(self.list.head.data, 10)

    def test_insert_at_position(self):
        self.list.insert_at_position(10, 1)
        self.list.insert_at_position(20, 1)
        self.assertEqual(self.list.head.data, 20)

    def test_print_ll(self):
        self.list.insert_at_head(10)
        self.list.insert_at_head(20)
        self.assertEqual(self.list.print_ll(), "Данные списка выведены")

    def test_get(self):
        self.list.insert_at_head(10)
        self.list.insert_at_head(20)
        found, _ = self.list.get(10)
        self.assertTrue(found)

    def test_change_data(self):
        self.list.insert_at_head(10)
        self.list.change_data(10, 20)
        self.assertEqual(self.list.head.data, 20)


if __name__ == '__main__':
    main()
