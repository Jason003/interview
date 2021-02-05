import collections
class Connection:
    def __init__(self, graph):
        self.graph = graph
        self.d1 = collections.defaultdict(set)
        self.d2 = collections.defaultdict(set)
        self.d3 = collections.defaultdict(set)

    def is_friend(self, x, y):
        return self.graph[x][y] == 1

    def get_d1(self, user):
        if user in self.d1:
            return self.d1[user]
        for neigh in range(len(self.graph)):
            if self.is_friend(user, neigh):
                self.d1[user].add(neigh)
        return self.d1[user]

    def get_d2(self, user):
        if user in self.d2:
            return self.d2[user]
        for neigh in self.get_d1(user):
            for friend in self.get_d1(neigh):
                if friend not in self.get_d1(user):
                    self.d2[user].add(friend)
        self.d2[user].discard(user)
        return self.d2[user]

    def get_d3(self, user):
        if user in self.d3:
            return self.d3[user]
        for neigh in self.get_d2(user):
            for friend in self.get_d1(neigh):
                if friend not in self.get_d2(user) and friend not in self.get_d1(user):
                    self.d3[user].add(friend)
        self.d3[user].discard(user)
        return self.d3[user]

    def get_degree(self, user1, user2):
        if user1 == user2:
            return 0
        if user1 in self.get_d1(user2):
            return 1
        if len(self.get_d1(user1) & self.get_d1(user2)) > 0:
            return 2
        if len(self.get_d1(user1) & self.get_d2(user2)) > 0:
            return 3
        return 0


        


con = Connection([[0,1,1,0],[1,0,0,0],[1,0,0,1],[0,0,1,0]])
for i in range(4):
    for j in range(4):
        print(i, j, con.get_degree(i,j))