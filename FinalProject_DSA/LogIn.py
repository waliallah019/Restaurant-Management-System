


class UserInfo:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

class HashTable:
    def __init__(self, size=1000):
        self.size = size
        self.table = [None] * size

    def _hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash_function(key)
        if self.table[index] is None:
            self.table[index] = [(key, value)]
        else:
            self.table[index].append((key, value))
           

    def find(self, key):
        index = self._hash_function(key)
        if self.table[index] is not None:
            for stored_key, value in self.table[index]:
                if stored_key == key:
                    return value
        return None

    def save_to_file(self, filename):
        with open(filename, 'a') as file:
            for entry in self.table:
                if entry is not None:
                    for key, value in entry:
                        file.write(f"{key},{value.username},{value.password},{value.role}\n")

    def load_from_file(self, filename):
        self.table = [None] * self.size
        with open(filename, 'r') as file:
            lines = file.readlines()

        # Skip the first line (headers) and process the rest
        for line in lines[0:]:
            parts = line.split(',')
            key = parts[0]
            username = parts[1]
            password = parts[2]
            role = parts[3]
            user_info = UserInfo(username, password, role)
            self.insert(key, user_info)

def is_valid_username(username):
    # Check if the username is at least 4 characters long
    if len(username) < 4:
        return False

    # Check if the username contains only alphanumeric characters or underscores
    if not username.isalnum() and "_" not in username:
        return False

    return True

def is_valid_password(password):
    # Check if the password is at least 6 characters long
    if len(password) < 6:
        return False

    # Check if the password contains at least 1 character and 1 digit
    has_character = any(char.isalpha() for char in password)
    has_digit = any(char.isdigit() for char in password)

    return has_character and has_digit


def is_valid_role(role):
    if role.lower() == 'customer':
        return True
    else:
        return False
def isexist(self,username):
     existing_user = self.hash_table.find(username)
     if existing_user is not None:
         return False
     else:
        return True    


def register( self,username, password, role):
       
        user_info = UserInfo(username, password, role)
        self.hash_table.insert(username, user_info)

        # Save the updated user data to a file
        self.hash_table.save_to_file("user_data.txt")


def login(self,name,password):
    
    self.hash_table.load_from_file("user_data.txt")
    user_info = self.hash_table.find(name)
    
    if user_info is not None and user_info.username == name and user_info.password == password :
       return True
    else:
        
        return False



# if __name__ == "__main__":
#     hash_table = HashTable()

#     while True:
#         print("1. Sign Up")
#         print("2. Sign In")
#         print("3. Exit")

#         choice = input("Enter your choice: ")

#         if choice == "1":
#             register()
#             # Save the hash table to a file after registering a new user
#         elif choice == "2":
#             # Load user data from the file before attempting to log in
#             hash_table.load_from_file("user_data.txt")
#             login()
#         elif choice == "3":
#             print("Turn off system")
#             break
#         else:
#             print("Invalid choice!")
