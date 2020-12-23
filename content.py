
class content:

    def queries():
        print("Enter 1 to insert data")
        print("Enter 2 to fetch data")
        print("Enter 3 to update data")
        print("Enter 4 to delete data\n")

    def runQuery(query, db):

        try:
            if(query == 1):
                userId = input("UserID: ")
                username = input("Name: ") 
                phone = input("Phone: ")
                db.insert(userId, username, phone)

            elif(query == 2):
                db.fetch()
            
            elif(query == 3):
                userId = input("UserID: ")
                username = input("New Name: ") 
                phone = input("New Phone: ")
                db.update(userId, username, phone)

            elif(query == 4):
                userId = input("UserID: ")
                db.delete(userId)
            
            else:
                print("Invalid Command! Try Again")

        except Exception as e:
            print(e)
        
        print()