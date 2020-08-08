from django.test import TestCase

from kanban.models import Board, Card, Column


class SampleTestCase(TestCase):
    def test_sample_board(self):
        board = Board.objects.create(name="Sample Board")
        column = Column.objects.create(board=board, title="Sample Column")
        Card.objects.create(column=column, title="Sample Card", slug="sample-card")

        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        boards = response.context["boards"]
        self.assertEqual(len(boards), 1)
        self.assertEqual(boards[0].name, "Sample Board")
        columns = boards[0].columns.all()
        self.assertEqual(len(columns), 1)
        self.assertEqual(columns[0].title, "Sample Column")
        cards = columns[0].cards.all()
        self.assertEqual(len(cards), 1)
        self.assertEqual(cards[0].title, "Sample Card")
