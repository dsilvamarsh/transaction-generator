import threading
import time

import account_repo
import transaction_repo


class TransactionGeneratorBot:

    daily_expense_types = ["Tea","Cofee","Breakfast","Smoke","Lunch","Dinner","Drinks"]

    def live_your_life(self,customer_name,customer_id):
        """This function will be invoked to generate transactions as a human being """
        # This function should live infinite till the main process is terminated

        while True:
        # Identify the account associated with the customer
            for account in account_repo.AccountRepo().find(customer_id):
                #Sleep for a moment
                time.sleep(5)
                transaction_repo.TransactionRepo().generate_transaction(
                    account[0],


                )
