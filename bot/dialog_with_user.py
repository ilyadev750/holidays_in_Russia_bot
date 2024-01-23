import re
from db.choose_the_holiday import get_the_result
from aiogram import types
from .bot_config import dp, START_MESSAGE_RU, START_MESSAGE_EN, HOLIDAYS_RU, bot, HOLIDAYS_EN, HOLIDAYS_NUMBERS
from .middlewaries import rate_limit
from .keyboards import keyboard_1, ReplyKeyboardRemove
from .logging_settings import *


@dp.message_handler(commands=['start'])
@rate_limit(3)
async def start_bot(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text=START_MESSAGE_RU)
    await bot.send_message(chat_id=message.from_user.id, text=START_MESSAGE_EN, reply_markup=keyboard_1)


@dp.message_handler(commands=['help'])
@rate_limit(limit=3)
async def help_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text="/holidays_ru - получить список праздников")
    await bot.send_message(chat_id=message.from_user.id, text="/holidays_en - to get the list of all holidays",
                           reply_markup=keyboard_1)



@dp.message_handler(commands=['holidays_ru'])
@rate_limit(limit=3)
async def help_command(message: types.Message,):
    await bot.send_message(chat_id=message.from_user.id, text='Список праздников в Российской Федерации:',
                           reply_markup=ReplyKeyboardRemove())
    await bot.send_message(chat_id=message.from_user.id, text=HOLIDAYS_RU, parse_mode='HTML')
    await bot.send_message(chat_id=message.from_user.id, text='Выберите праздник из списка:')


@dp.message_handler(commands=['holidays_en'])
@rate_limit(limit=3)
async def help_command(message: types.Message,):
    await bot.send_message(chat_id=message.from_user.id, text='The list of holidays in the Russian Federation',
                           reply_markup=ReplyKeyboardRemove())
    await bot.send_message(chat_id=message.from_user.id, text=HOLIDAYS_EN, parse_mode='HTML')
    await bot.send_message(chat_id=message.from_user.id, text='Please, choose a holiday from the list:')


# @dp.message_handler()
# @rate_limit(limit=3)
# async def choose_the_holiday(message: types.Message):
#     pattern = message.text.capitalize().split(" ")[0]
#     pattern_2 = message.text.capitalize().split(" ")
#     result = get_the_result(pattern).all()
#     print(pattern_2)
#     print(pattern)
#     if result:
#         description = result[0].description
#         await bot.send_message(chat_id=message.from_user.id, text=f'{description}')
#     else:
#         await bot.send_message(chat_id=message.from_user.id, text='Нет такого праздника. Пожалуйста, введите корректный '
#                                                                   'праздник или команду /help')
#         await bot.send_message(chat_id=message.from_user.id, text='There is no holiday like this. Please, input a '
#                                                                   'correct holiday or /help command')


@dp.message_handler()
@rate_limit(limit=3)
async def choose_the_holiday(message: types.Message):
    search_pattern = get_the_search_pattern(message.text)
    result = get_the_result(search_pattern).all()
    if result:
        description = result[0].description
        await bot.send_message(chat_id=message.from_user.id, text=f'{description}')
    else:
        await bot.send_message(chat_id=message.from_user.id, text='Нет такого праздника. Пожалуйста, введите корректный '
                                                                  'праздник или команду /help')
        await bot.send_message(chat_id=message.from_user.id, text='There is no holiday like this. Please, input a '
                                                                  'correct holiday or /help command')


@dp.errors_handler()
async def errors_handler(update: types.Update, exception: Exception):
    logging.error(f'Ошибка при обработке запроса {update}: {exception}')


def get_the_search_pattern(text):
    patterns = re.sub(" +", " ", text)
    patterns = patterns.lstrip().split(" ")
    if len(patterns) > 1:
        if patterns[0].capitalize() in 'День':
            search_pattern = patterns[1].capitalize()
        elif patterns[0] in HOLIDAYS_NUMBERS:
            search_pattern = f'{patterns[0]} {patterns[1].capitalize()}'
        else:
            search_pattern = patterns[0].capitalize()
    else:
        search_pattern = patterns[0].capitalize()
    return search_pattern