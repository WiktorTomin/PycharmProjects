import unittest
from unittest.mock import Mock

from book_service import BookService


class TestBookService(unittest.TestCase):
    def setUp(self) -> None:
        self.service = BookService(Mock())

    def test_find_by_id(self):
        book_id = 3
        self.service.find_by_id(book_id)
        self.service.book_repository.find_by_id.assert_called_with(book_id)

    def test_find_all(self):
        self.service.find_all()
        self.service.book_repository.find_all.assert_called_once()