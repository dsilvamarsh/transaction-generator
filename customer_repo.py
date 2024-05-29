import logging
import random

import psycopg

import db_config
from faker import Faker

class CustomerRepo:
    def save(self ,name,tax_id,email,contact,type):
        """Function to save customer"""
        query="""
        INSERT INTO core.customer (name,tax_id,email,contact,create_ts,type)
        values
        (%s,%s,%s,%s,current_timestamp,%s)
        """
        query_params=(name,tax_id,email,contact,type)
        try:
            with psycopg.connect(**db_config.load_db_config()) as conn:
                with conn.cursor() as cursor:
                    cursor.execute(query=query,params=query_params)
        except (psycopg.DatabaseError,Exception) as ex :
            print("Database Error ",ex)
    def find_all(self):
        #global log
        """Function to fetch all customers"""
        query ="""
        select * from core.customer
        """
        try:
            with psycopg.connect(** db_config.load_db_config()) as conn:
                with conn.cursor() as cursor:
                    cursor.execute(query=query)
                    #log.debug("Query Executed succesfully")
                    return cursor.fetchall()
        except (psycopg.DatabaseError , Exception) as ex:
            print("Database Error ",ex)


    def find(self,customer_id):
        query ="""
        select * from core.customer where id= %s;
        """
        try:
            with psycopg.connect(** db_config.load_db_config()) as conn:
                with conn.cursor() as cursor:
                    cursor.execute(query=query,params=(customer_id,))
                    #log.debug("Query Executed succesfully")
                    print(f"Cursor row size {cursor.rowcount}")
                    return cursor.fetchone()
        except (psycopg.DatabaseError , Exception) as ex:
            print("Database Error ",ex)


    def create_dummy_customers(self):
        fake = Faker()
        for run in range(100):
            CustomerRepo().save(
                fake.name(),
                fake.ssn(),
                fake.email(),
                fake.random_number(10),
                random.choice(["Business","Saleried","Government Employee","Self Employee"])
            )
if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    log=logging.getLogger(__name__)
    cust_repo = CustomerRepo()
    #print(cust_repo.find(2))
    cust_repo.create_dummy_customers()