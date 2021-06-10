class SocialNetwork:
    class User:
        def __init__(self, uname):
            self.username = uname
            self.friends = []

    def __init__(self):
        self.users = []

    def size(self):
        return len(self.users)

    def get_friends(self, user):
        return user.friends
    
    def create_user(self, username):
        new_user = self.User(username)
        self.users.append(new_user)
        return new_user

    def create_friendship(self, user_a, user_b):
        user_a.friends.append(user_b)
        user_b.friends.append(user_a)

    def DFS(self, u):
        '''traverses the graph using DFS starting at user u, in preorder'''
        marked_list = []
        dfs_order = []
        return self.dfs_rec(u, marked_list, dfs_order)

    def dfs_rec(self, u, marked_list, dfs_order):
        dfs_order.append(u) # the "visit"
        marked_list.append(u)
        for w in self.get_friends(u):
            if w not in marked_list:
                self.dfs_rec(w, marked_list, dfs_order)
        return dfs_order

    def count_circles(self):
        marked_list = []
        counter = 0
        for user in self.users:
            user_group = self.DFS(user)
            if user.username not in marked_list:
                for u in user_group:
                    marked_list.append(u.username)
                counter += 1   
        return counter