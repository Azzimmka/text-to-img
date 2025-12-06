Что-бы стрыть любой токен:
1. Создайте .env и запишите его в таком виде: TOKEN=8535120...
2. Устонавливайте pip install python-dotenv и в index импортируете:
from dotenv import load_dotenv, find_dotenv
и далее фиксируюте дерикторию токена таким оброзом: load_dotenv(find_dotenv())
3. В index.py 1. import os 2. TOKEN=os.getenv('TOKEN')