class ManagerInfo:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

class HashTable:
    def __init__(self):
        self.manager_info = None

    def load_from_file(self, filename):
        with open(filename, 'r') as file:
            lines = file.readlines()

        for line in lines[0:]:
            parts = line.split(',')
            username = parts[0]
            password = parts[1]
            role = parts[2].strip()
            self.manager_info = ManagerInfo(username, password, role)
            break 

def loginM(self,name,password,role):
    hash_table = HashTable()
    hash_table.load_from_file("Admin.txt")

    if hash_table.manager_info is not None:
       

        if name == hash_table.manager_info.username and password == hash_table.manager_info.password and role==hash_table.manager_info.role:
        
            return True
        else:
            return False
    else:
        raise ValueError("Manager information not found.")

if __name__ == "__main__":
    login()
