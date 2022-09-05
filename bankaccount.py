import random


class BankAccount:
    """
    This is a class about describing the operation of a bank account
    """

    def __init__(self, first_name: str, last_name: str, id_number: int) -> None:
        """
        This method is the constructor of the Bank Account class\n
        :param first_name: The first name of the person creating the bank account
        :param last_name: The last name of the person creating the bank account
        :param id_number: The id number of the person creating the bank account
        :returns: None
        """
        assert isinstance(first_name, str), f"The first name provided is not of the string type"
        assert isinstance(last_name, str), f"The last name provided is not of the string type"
        assert isinstance(id_number, int), f"The id provided is not of the float type"
        for i in self.database["Id Number"]:
            assert i != id_number

        self.first_name = first_name
        self.last_name = last_name
        self.id_number = id_number
        self.balance = 0
        self.database["First Name"].append(self.first_name)
        self.database["Last Name"].append(self.last_name)
        self.database["Id Number"].append(self.id_number)

    database = {
        "First Name": [],
        "Last Name": [],
        "Id Number": []
    };

    def deposit(self, id_number: int, amount: float) -> str:
        if id_number == self.id_number:
            self.balance += amount
            return f"The new balance will be {self.balance} after depositing "

    def withdraw(self, id_number: int, amount: float) -> str:
        if id_number == self.id_number:
            if self.balance > 0:
                self.balance -= amount
                return f"The new balance will be {self.balance} after withdrawing {amount}"
            else:
                return f"The balance can not be withdrawn from because it is at {self.balance}"

    @property
    def get_name(self) -> str:
        """

        :return: The account first name
        """
        return self.first_name

    @get_name.setter
    def get_name(self, first_name) -> None:
        """

        :param first_name:
        :return: None
        """
        self.first_name = first_name
