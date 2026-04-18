# Sample E-commerce Inventory Database
inventory = {
    "SKU_101": {"name": "Wireless Mouse", "price": 25.00, "stock_count": 50, "category": "Electronics"},
    "SKU_102": {"name": "Gaming Keyboard", "price": 80.00, "stock_count": 0, "category": "Electronics"},
    "SKU_103": {"name": "Yoga Mat", "price": 30.00, "stock_count": 15, "category": "Fitness"},
    "SKU_104": {"name": "Bluetooth Speaker", "price": 120.00, "stock_count": 5, "category": "Electronics"},
    "SKU_105": {"name": "Protein Shaker", "price": 15.00, "stock_count": 0, "category": "Fitness"},
}

"""15% discount for electronics category"""
for key,data in inventory.items():
    if data["category"] == "Electronics":
        data["price"] = data["price"] - (data["price"] * (15/100))

"""add new key and value """
for key,data in inventory.items():
    if data["stock_count"] == 0:
        data["re_Stock_Urgent"] = True

"""check for a key and add if it doesnt exist using setDefault()"""
for data in inventory.values():
    if "last_solid" not in data:
        data.setdefault("last_solid", "Never")

print(inventory)



