import random
from util import Queue

class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments
        Creates that number of users and a randomly distributed friendships
        between those users.
        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME
        social_graph = SocialGraph()
        print("social_graph", social_graph)

        # Add users
        for user in range(num_users):
            print(f'User: {user}')
            self.add_user(user)
            print(f'add_user(user): {user}')

        # Create friendships

        # 1. Create a list with all possible friendships
        friend_list = []
        # Loop through and create possibilities
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                # friend_list.append(data)
                friend_list.append((user_id, friend_id))
        # Print friend_list
        print(f'Friend List: {friend_list}')

        # 2. Shuffle the friendships list
        random.shuffle(friend_list)
        # Print shuffled list
        print(f'Shuffled Friend List: {friend_list}')

        for i in range(num_users * avg_friendships // 2):
            friendship = friend_list[i]
            self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id):
        """
        1. Takes a user's user_id as an argument
        2. Returns a dictionary containing every user in that user's
           extended network with the shortest friendship path between them.
        3. The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME

        # Hint 1: What kind of graph search guarantees you a shortest path? BFS (Queue)
        # Hint 2: Instead of using a set to mark users as visited, you could use a dictionary.
        #   Similar to sets, checking if something is in a dictionary runs in O(1) time.
        #   If the visited user is the key, what would the value be? Value = path

        # BFS (Queue)
        q = Queue()
        q.enqueue(([user_id]))
        while q.size() > 0:
            path = q.dequeue()
            last_vertex = path[-1]
            if last_vertex not in visited:
                if last_vertex != user_id:
                    visited[last_vertex] = path
                for friends in self.friendships[last_vertex]:
                    path_copy = path.copy()
                    path_copy.append(friends)
                    q.enqueue(path_copy)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
