# from listLink.queue import Queue
import unittest


class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue(3)

    def test_is_empty(self):
        self.assertTrue(self.queue.is_empty())

    def test_is_full(self):
        self.queue.enqueue('a')
        self.queue.enqueue('b')
        self.queue.enqueue('c')
        self.queue.enqueue('c')
        self.assertTrue(self.queue.is_full())
