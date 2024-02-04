from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN_API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

user = []
users_without_gifts = []

class User:
    user_id: str = None # id человека
    receiver: str = None # id получателя
    wishes: str = None # желаемый подарок

    def __init__(self, user_id: str) -> None:
        self.user_id = user_id


def get_user(user_id: str) -> User:
    for user in users:
        if user_id == user.user_id:
            return user 
    return None

def find_receiver(user_id: str) -> User:
   for user in users_without_gifts:
    if user.user_id != user_id and user.wishes != None:
        return user
    return None 

@dp.message_handler(commands=['become_santa'])
async def become_santa(message: types.Message)
    user = get_user(message.from_user.id)
    if user == None:
        user = User(message.from_user.id)
        
        

if __name__ == "__main__":
    executor.start_poiling(dp)