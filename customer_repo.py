import logging

import psycopg

import db_config
from faker import Faker

class CustomerRepo:
    def save(self ,name,tax_id,email,contact):
        """Function to save customer"""
        query="""
        INSERT INTO core.customer (name,tax_id,email,contact,create_ts)
        values
        (%s,%s,%s,%s,current_timestamp)
        """
        query_params=(name,tax_id,email,contact)
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
if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    log=logging.getLogger(__name__)
    repo = CustomerRepo()
    #repo.save('Sara','dww3334','sara@gmail.com','33445555')
    fake= Faker()
    for run in range(1000):
        repo.save(fake.name(),fake.ssn(),fake.email(),fake.random_number(10))
    #log.debug(f"Customers : {repo.find_all()}")