from polls.repository.user import UserRepository
from polls.models import User
from typing import List

class UserService:
    def __init__(self) -> None:
        self.user_repository = UserRepository()

    def getAllUser(self) -> List[User]:
        return self.user_repository.get().values()
    
    def getSpecificUser(self, name) -> User:
        return self.user_repository.getByCondition(name=name)

    def insertUser(self, name) -> User:
        return self.user_repository.save(name=name)
    
    def updateUser(self, name, **kwargs) -> User:
        getUser = self.user_repository.getByCondition(name=name)
        return self.user_repository.update(getUser, **kwargs)
    
    def deleteUser(self, name) -> None:
        getUser = self.user_repository.getByCondition(name=name)
        return self.user_repository.delete(getUser)
