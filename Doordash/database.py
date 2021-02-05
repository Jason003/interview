'''
begin就是database开始commands，然后可以接受好几个commands，例如set，unset等等
rollback是取消这些commands，然后commit是永久更新database
'''
class Database:
    def __init__(self):
        self.transactions = []
        self.database = {}
        self.start = False

    def begin(self):
        self.start = True

    def set(self, k, v):
        if self.start:
            self.transactions.append(('set', k, v))

    def unset(self, k):
        if self.start:
            self.transactions.append(('unset', k))

    def commit(self):

        for t in self.transactions:
            if t[0] == 'set':
                self.database[t[1]] = t[2]
            elif t[0] == 'unset':
                self.database[t[1]] = None
        self.transactions.clear()

    def rollback(self):
        self.transactions.clear()

    def get(self, k):
        return self.database.get(k, None)

db = Database()
db.set(1,2)
db.rollback()
db.commit()
print(db.get(1))