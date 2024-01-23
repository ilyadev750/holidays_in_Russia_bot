from aiogram import executor
from bot.bot_config import dp
from bot import dialog_with_user
from bot.middlewaries import ThrottlingMiddleware, MaxLengthMiddleware


if __name__ == '__main__':
    dp.middleware.setup(ThrottlingMiddleware())
    dp.middleware.setup(MaxLengthMiddleware())
    executor.start_polling(dp, skip_updates=True)