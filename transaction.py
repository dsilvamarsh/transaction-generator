import psycopg

import db_config


class TransactionRepo():
    def save(self):
        query = """"""
        query_params=""

        with psycopg.connect(** db_config.load_db_config()) as conn:
            with conn.cursor() as cursor :
                cursor.execute(query=query,params=query_params)