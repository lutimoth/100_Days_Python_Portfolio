class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
     
        
    
                
user = User("001", "test_user")

print(user.id, user.username)