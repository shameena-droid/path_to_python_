
transactions = {
    "TXN_001": {"amount": 500, "location": "Local", "timestamp": "2023-10-01 10:00", "status": "approved"},
    "TXN_002": {"amount": 12000, "location": "Local", "timestamp": "2023-10-01 10:05", "status": "pending"},
    "TXN_003": {"amount": 450, "location": "International", "timestamp": "2023-10-01 10:10", "status": "pending"},
    "TXN_004": {"amount": 20, "location": "Local", "timestamp": "2023-10-01 10:15", "status": "approved"},
    "TXN_005": {"amount": 15000, "location": "International", "timestamp": "2023-10-01 10:20", "status": "pending"},
}

"""add a new trasaction"""
txn = {
    "TXN_006":{"amount": 75, "location": "International", "timestamp": "2023-10-01 10:20", "status": "pending"}
      }
transactions.update(txn)

"""if the amount >10000 or location is international ,update status to flagged"""
rule = {"mxm_amount":10000}
def flag_the_user(database:dict[str, dict[str, int | str]],rule:dict ):
    flagged_items = []
    for t_n, data in database.items() :
        if data["amount"] > rule.get("mxm_amount") or data["location"] == "International" :
            data["status"] = "flagged"
            flagged_items.append(t_n)
    print("flagged transactions are : ")
    print(flagged_items)
    return database

"""calling the f()"""
flagged= flag_the_user(transactions,rule)

"""create a list to add the items to be deleted..."""
to_be_removed = []
""" ...to remove the txn whose status=approved"""
def delete_approved_items(database:dict[str, dict[str, int | str]],remove)->list[str]:
    for t_n, data in database.items() :
        if data["status"] == "approved":
            remove.append(t_n)   
    for item in remove:
        database.pop(item)
    return remove

"""call the f()"""
popped = delete_approved_items(transactions,to_be_removed)
print(" removed transactions are : ")
print(popped)

"""view the flagged txns"""
print("the final database : ")
print(flagged)
