import mysql.connector as connector

class DataBase:
    def __init__(self):
        self.con = connector.connect(host='localhost',
                                    port ='3306',
                                    user='root',
                                    password='410tc1',
                                    database='pythontest')
        query = 'create table if not exists user(userID int primary key, userName varchar(200), phone varchar(12))'
        cur=self.con.cursor()
        cur.execute(query)
    
    def insert(self, userid, username, phone):
        query = "insert into user(userId, userName, phone) values({},'{}','{}')".format(userid,username,phone)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()

    def fetch(self):
        query="select * from user"
        cur=self.con.cursor()
        cur.execute(query)
        for row in cur:
            print(row)
    
    def delete(self, userid):
        query="delete from user where userId = {}".format(userid)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()

    def update(self, userID, newName, newPhone):
        query = "update user set userName='{}',phone='{}' where userId={}".format(newName, newPhone, userID)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()