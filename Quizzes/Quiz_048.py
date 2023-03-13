from Project.library import encrypt_password
from Project.library import check_password
import sqlite3


class database_worker:
    def __init__(self, name):
        self.connection = sqlite3.connect(name)
        self.cursor = self.connection.cursor()


    def search(self, query):
        result = self.cursor.execute(query).fetchall()
        return result


    def run_save(self, query):
        self.cursor.execute(query)
        self.connection.commit()


    def close(self):
        self.connection.close()


x = database_worker('Quiz_048.db')
query = 'SELECT * FROM ledger'
result = x.search(query)
x.close()

# [(1, 560, 371, 37255, '$pbkdf2-sha256$30000$XouR0rrX2jvH.N87pzQGoA$V8D/wxNXriCt/SD/raqk3CiPB3VgQRHRLJk4FzrENok'),
# (2, 488, 561, 1431, '$pbkdf2-sha256$30000$h9Dau9e6t5bS.j8n5Nw7xw$ULW72DF7fhQ2u1JL1T8cvvTzH8jc6UFsNAx8sc.luH4'),
# (3, 254, 920, 26756, '$pbkdf2-sha256$30000$lXJuLQUgpBRiLGWM0TpnrA$EGhB0YJK1vkKCZr1Ws1ivMEHMxQkjy4V9/DByGxL9V4'),
# (4, 438, 920, 15968, '$pbkdf2-sha256$30000$IGTMude6934PYWxt7d2bEw$oMdkl26oYYmhLnVr2sASE8UNOS1i2oLVvCxeruXKM7o'),
# (5, 744, 261, 24371, '$pbkdf2-sha256$30000$BIBwLgUgBMC4NwbAWKuVUg$knesXOgdM.d.95.S93HkhHua6Xvl4pm.UA7J2Y02xJQ')]

for element in result:
    id = element[0]
    sender_id = element[1]
    receiver_id = element[2]
    amount = element[3]
    prev_hash = element[4]

    unhashed_str = f"id {id},sender_id {sender_id},receiver_id {receiver_id},amount {amount}"
    encrypt_password(unhashed_str)
    print(check_password(unhashed_str, prev_hash))