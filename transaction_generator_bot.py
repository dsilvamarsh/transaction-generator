import logging
import threading
import time

import account_repo
import customer_repo
import transaction_repo



def live_your_life(customer):
    """This function will be invoked to generate transactions as a human being """
    # This function should live infinite till the main process is terminated
    txn_repo = transaction_repo.TransactionRepo()
    log.debug(f" Customer will start living his life {customer}")
    while True:
        txn_repo.generate_dummy_transactions_for_customer(customer)
        log.debug(f'Customer {customer} is ready to work for some time ')
        log.debug(f'Customer {customer} is Hungry ')
        time.sleep(60)

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    log=logging.getLogger(__name__)
    customer_thread_list = []
    #Fetch customers for whom we want to create a human bot
    cust_repp = customer_repo.CustomerRepo()
    log.debug(f"Customer repo fetched {cust_repp}")
    for customer in cust_repp.find_all():
        log.debug(f" Generating a thread for customer {customer}")
        cust_thread = threading.Thread(target=live_your_life,args=(customer,))
        cust_thread.start()
        log.debug(f" Thread started for customer {customer}")
        customer_thread_list.append(cust_thread)
        log.debug(f"Customer added to Join list {customer}")
    for val in customer_thread_list:
        val.join()
    log.debug("After all threads have joined ")

    log.debug("End of the bot generator")