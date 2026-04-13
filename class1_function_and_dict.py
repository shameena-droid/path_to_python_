mock_db = {
    "users": [
        {"id": 1, "name": "Alice", "role": "admin",},
        {"id": 2, "name": "Bob", "role": "user"}
        ],
    "items": [
        {"id": 101, "name": "Laptop","status":"active"},
        {"id": 102, "name": "Mouse","status":"active"},
        {"id": 103, "name": "keyboard","status":"active"},
        
        ]
}
#make an item inactive
def deactivate_item(data,item_id):
    for i in data["items"]:
        if i["id"]==item_id:
            i["status"]="inactive"
            return f"the item {item_id} has been marked as inactive"
    return "invalid item"

#lets call the function
ID = int(input("Enter item ID to deactivate: "))
print(deactivate_item(mock_db,ID))
print(mock_db["items"])
#get active items
def get_active_items(data):
    newmock_db=[]
    for item in data["items"]:
        if item.get("status") == "active":
            newmock_db.append(item)
          
    return newmock_db

yes=input("Do you want to see the active items: yes/no")
if yes=="yes":
    print(get_active_items(mock_db))
else:
    print("invalid query")
#search item by the name
def search_item_by_name(data,name):
    name=name.lower()
    for i in data["items"]:
        i_name=i.get("name").lower()
        if i_name==name:
            print("id: ",i.get("id"))
            print("status:",i.get("status"))
    return "item not found"        
name=input("enter an item name :")
search_item_by_name(mock_db,name)



            