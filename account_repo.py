import logging
import random

import psycopg

import customer_repo
import db_config
from faker import Faker


class AccountRepo():

    def save(self,customer_id,balance,acc_type):
        global log
        query = """
        INSERT into core.account (customer_id,balance,acc_type,create_ts)
        values
        (%s,%s,%s,current_timestamp) 
        """
        query_param=(customer_id,balance,acc_type)
        try:
            with psycopg.connect(** db_config.load_db_config()) as conn:
                with conn.cursor() as cursor:
                    cursor.execute(query=query,params=query_param)
        except (psycopg.DatabaseError , Exception) as ex:
            log.exception("Database Error",ex)




if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    log=logging.getLogger(__name__)
    fake = Faker()
    # Fetch all customers and generate accounts for them
    custRepo = customer_repo.CustomerRepo()
    for customer in custRepo.find_all():
        #Generate account for each customer
        log.debug(f" Customer info : {customer}")
        accRepo = AccountRepo()
        accRepo.save(customer[0],random.uniform(100,10000),random.choice(["Savings","Current","Loan"]))