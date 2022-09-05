import unittest

from bankaccount import BankAccount


class TestBankAccount(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.adam = BankAccount("Adam", "Luther", 24564437869)

    def test_init_method(self):
        self.assertIsInstance(self.adam.id_number, int)

    def test_deposit(self):
        pass
