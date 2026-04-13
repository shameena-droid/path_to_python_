raw_transactions = [
    {"txn_id": "T101", "user_id": "U1", "amount": 500, "location": "NY", "history": ["NY", "NY"]},
    {"txn_id": "T102", "user_id": "U2", "amount": 12000, "location": "NY", "history": ["NY"]},
    {"txn_id": "T103", "user_id": "U1", "amount": 100, "location": "London", "history": ["NY", "NY"]},
]
config={"flag_the_user":10000}

"""flag the user if the trsnsaction amt is > 10000 """
def flag_the_user(data:list[dict],config:dict=None)->list[dict]:
    for tsn in data:
        amount = tsn.get("amount")
        if amount > config.get("flag_the_user"):
            tsn["status"] = "flagged"
            return tsn["status"]

response=flag_the_user(raw_transactions,config)
print(response)

"""find the location from the transacn ,if the location is not in the history, 
 set status to review required"""
def review_required(data:list[dict])->list[dict]:
    for txn in data:
        location = txn.get("location")
        history=txn.get("history")
        if location not in history:
            txn["status"]="review required"
            return txn["status"]

review = review_required(raw_transactions)
print(review)

"""if trancn amt is >10000 and location is not int the history, status to blocked"""
def block_the_user(data:list[dict],config):
    for txn in data:
        if review_required(data) == "review required" and flag_the_user(data,config) == "flagged":
            txn["status"] = "blocked"
            txn.update({"fraud_metrices":{"status":"review_required","flags":["flagged","unusual location"]}})
    return data
block = block_the_user(raw_transactions,config)   
print(block)

