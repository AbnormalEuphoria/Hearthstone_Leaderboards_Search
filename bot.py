import json
import logging

import aiogram.utils.markdown
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = ''

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler()
async def echo(message: types.Message):

    name_to_search = message.text
    found_name = 'NaN'

    for i in range(1, 5):
        with open(f'player_data/page_{i}.json', 'r', encoding='utf-8') as file:
            page = json.load(file)

        for item in page:
            if item['Account'].lower() == name_to_search.lower():
                found_name = item['Account']
                found_rank = item['Rank']
                found_rating = item['Rating']

    if found_name == 'NaN':
        await message.answer(f'Could not find rankings for user {name_to_search}')
    else:
        await message.answer(f'Account: {found_name}\nRank: {found_rank}\nAverage Score: {found_rating}')



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)