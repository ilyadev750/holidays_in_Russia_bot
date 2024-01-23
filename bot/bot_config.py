from aiogram import Bot, Dispatcher
from .bot_token import BOT_TOKEN
from aiogram.contrib.fsm_storage.memory import MemoryStorage


START_MESSAGE_RU = ('Добро пожаловать в бот, который может дать информацию о праздниках в России. Пожалуйста, введите '
                    'название праздника или команду /holidays_ru, чтобы получить полный список праздников.')
START_MESSAGE_EN = ("Welcome to the bot, which could give information about holidays in the Russian Federation. Please,"
                    "input the name of a holiday or the command '/holidays_en' to get the list of all holidays.")

HOLIDAYS_RU = ('<b><em>Новый год\n\nРождество Христово\n\nСтарый Новый год\n\nКрещение\n\nТатьянин день - день студента\n\n'
            'Масленица\n\nВербное воскресенье\n\nПасха\n\nТроица\n\nДень Защиты детей\n\nДень Защитника Отечества - '
            '23 февраля\n\nМеждународный женский день - 8 марта\n\nПраздник весны и труда - 1 мая\n\n'
            'День Победы - 9 мая\n\nДень защиты детей\n\nДень России\n\nДень Знаний - 1 сентября\n\nДень учителя\n\nДень Народного единства'
            '\n\nДень Конституции</em></b>')

HOLIDAYS_EN = ("<b><em>New Year\n\nChristmas\n\nOld New Year\n\nLord's Baptism\n\nTatyana's day - student's day\n\n"
            "Maslenitsa\n\nPalm Sunday\n\nEaster\n\nTrinity\n\nChildren's day\n\nDefender of the Fatherland Day - "
            "23rd February\n\nInternational Women's Day - 8 March\n\nLabor Day - 1 May\n\n"
            "Victory Day - 9 May\n\nChildren's Day\n\nRussia Day\n\n1st September - Knowledge Day\n\nTeacher's day\n\nNational Unity Day"
            "\n\nConstitution Day</em></b>")

HOLIDAYS_NUMBERS = ['1', '23', '8', '9']


bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())