from bank import Bank
from customer import Customer
from transaction import Transaction
from account import Account
from datasource import DataSource
import sys

def main() -> int:

    print("**Starting bank**")
    bank_instance=Bank("Swedish Bank")
    return 0


if __name__ == '__main__':
    sys.exit(main())  # next section explains the use of sys.exit
