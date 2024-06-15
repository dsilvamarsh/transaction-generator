import random
import time
import psycopg

import account_repo
import customer_repo
import db_config
import expense_repo


class TransactionRepo():
    def save(self,src_acc,tgt_acc,transfer_amount,exchange_rate,currency_code,status,reference,expense_id):
        query = """
        INSERT INTO core.transaction (src_acc,tgt_acc,transfer_amount,exchange_rate,currency_code,status,reference,expense_id)
        values
        (%s,%s,%s,%s,%s,%s,%s,%s)  
        """
        query_params=(src_acc,tgt_acc,transfer_amount,exchange_rate,currency_code,status,reference,expense_id)
        try:
            with psycopg.connect(** db_config.load_db_config()) as conn:
                with conn.cursor() as cursor :
                    cursor.execute(query=query,params=query_params)
        except (psycopg.DatabaseError,Exception) as ex:
            print("Database Exception ",ex)
    def save_all(self,query_params_list):
        query = """
        INSERT INTO core.transaction (src_acc,tgt_acc,transfer_amount,exchange_rate,currency_code,status,reference,expense_id)
        values
        (%s,%s,%s,%s,%s,%s,%s,%s) 
        """

        try:
            with psycopg.connect(** db_config.load_db_config()) as conn:
                with conn.cursor() as cursor :
                    cursor.executemany(query,query_params_list)
        except (psycopg.DatabaseError,Exception) as ex:
            print("Database Exception ",ex)
    def generate_dummy_transactions_for_customer(self,customer):
        """This function will generate dummy transactions"""
        #cust_repo = customer_repo.CustomerRepo()
        acc_repo = account_repo.AccountRepo()
        exp_repo = expense_repo.ExpenseRepo()
        expense_list=exp_repo.find_all()
        # find all customers

        print(f"Generating txn for customer {customer}")
        # loop over cusomers and find accounts
        src_account_list = acc_repo.find(customer[0])
        tgt_account_list = acc_repo.find_accounts_with_type('Business')
        # loop over accounts to generate transactions
        src_account = random.choice(src_account_list)
        expense=random.choice(expense_list)
        tgt_account=random.choice(tgt_account_list)
        expense=random.choice(expense_list)
        self.save(src_account[0],
                  tgt_account[0],
                  expense[2],
                  random.choice([1]),
                  random.choice(["INR"]),
                  "Pending",
                  expense[1],
                  expense[0])
        time.sleep(expense[5])


    def generate_dummy_transactions(self):
        """This function will generate dummy transactions"""
        cust_repo = customer_repo.CustomerRepo()
        acc_repo = account_repo.AccountRepo()
        exp_repo = expense_repo.ExpenseRepo()
        expense_list=exp_repo.find_all()
        # find all customers
        for customer in cust_repo.find_all():
            print(f"Generating txn for customer {customer}")
            # loop over cusomers and find accounts
            src_account_list = acc_repo.find(customer[0])
            tgt_account_list = acc_repo.find_excluding(customer[0])
            # loop over accounts to generate transactions
            for src_account in src_account_list:
                query_params=[]
                for run in range(100000):
                    expense=random.choice(expense_list)
                    tmp=[]
                    tmp.append(src_account[0])
                    tmp.append(random.choice(tgt_account_list)[0])
                    tmp.append(random.uniform(100, 1000))
                    tmp.append(random.choice([1, 1.2]))
                    tmp.append(random.choice(["INR"]))
                    tmp.append("Pending")
                    tmp.append(expense[1])
                    tmp.append(expense[0])
                    tmp.append(expense[5])
                    query_params.append(tuple(tmp))

                self.save_all(query_params)

if __name__ == "__main__":
    txn_repo = TransactionRepo()
    txn_repo.generate_dummy_transactions()
    #find



