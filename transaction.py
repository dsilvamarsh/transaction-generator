import random

import psycopg

import account_repo
import customer_repo
import db_config


class TransactionRepo():
    def save(self,src_acc,tgt_acc,transfer_amount,exchange_rate,currency_code):
        query = """
        INSERT INTO core.transaction (src_acc,tgt_acc,transfer_amount,exchange_rate,currency_code)
        values
        (%s,%s,%s,%s,%s) 
        """
        query_params=(src_acc,tgt_acc,transfer_amount,exchange_rate,currency_code)
        try:
            with psycopg.connect(** db_config.load_db_config()) as conn:
                with conn.cursor() as cursor :
                    cursor.execute(query=query,params=query_params)
        except (psycopg.DatabaseError,Exception) as ex:
            print("Database Exception ",ex)



if __name__ == "__main__":
    txn_repo = TransactionRepo()
    cust_repo = customer_repo.CustomerRepo()
    acc_repo = account_repo.AccountRepo()
    # find all customers
    for customer in cust_repo.find_all():
        print(f"Generating txn for customer {customer}")
        # loop over cusomers and find accounts
        src_account_list = acc_repo.find(customer[0])
        tgt_account_list = acc_repo.find_excluding(customer[0])
        # loop over accounts to generate transactions
        for src_account in src_account_list:
            for run in range(10):
                txn_repo.save(
                    src_account,
                    tgt_account_list.index(random.choice()),
                    random.uniform(100,1000),
                    random.choice([1,1.2]),
                    random.choice(["INR"])

                )
    #find



