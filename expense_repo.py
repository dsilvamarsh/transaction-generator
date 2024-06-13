import psycopg

import db_config


class ExpenseRepo:
    def find(self):
        pass

    def find_all(self):
        query ="""
        select * from core.expense
        """
        try:
            with psycopg.connect(** db_config.load_db_config()) as conn:
                with conn.cursor() as cursor:
                    cursor.execute(query=query)
                    return cursor.fetchall()
        except (psycopg.DatabaseError(),Exception) as ex:
            print(f" Database Exception {ex}")


    def save(self):
        pass





if __name__ == "__main__":
    repo = ExpenseRepo()
    expense_list =repo.find_all()
    print(f"Expense list : {expense_list}")
