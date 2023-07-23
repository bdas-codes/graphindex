from unittest import TestCase
from guru import Guru


class TestGuru(TestCase):

    def test_ask(self):
        guru: Guru = Guru()
        # Note: These values may change over time due to the nature of external data sources.
        self.assertEqual('70', guru.ask('how old is Tony Blair'))
        self.assertEqual('77', guru.ask('how old is Donald Trump'))
        self.assertEqual('8908081', guru.ask('what is the population of London'))
        self.assertEqual('8804190', guru.ask('what is the population of New York City'))
