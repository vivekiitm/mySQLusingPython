from DataBase import DataBase
from content import content

class main:
    db = DataBase()
    while True: 
        content.queries()
        query = int(input())
        content.runQuery(query, db)


if __name__ == "__main__":
    main()
