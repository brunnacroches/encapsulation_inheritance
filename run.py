class DatabaseConn:
    def __init__(self) -> None:
        self.__database = 'Postgress' 
        self._conn = '//connection_string' # protect
        self.user = 'Brunna'
    
    def get_database(self) -> None:
        print(self.__database)
    
    def _testing_connection(self) -> None:
        print('Connection OK!')

class Repository(DatabaseConn):
    
    def __init__(self) -> None:
        super().__init__()
        # print(self.user)
        # print(self.__database) ERROR
        # print(self._conn)
    
    def select(self) -> None:
        self._testing_connection()
        print('connectiong to {}'.format(self._conn))
        print('SELECT * FROM table')
        print(self.user)

repo = Repository()
repo.select()

# db = DatabaseConn()
# print(db.user)
# # print(db.__database) -> Erro!
# print(db._conn)
