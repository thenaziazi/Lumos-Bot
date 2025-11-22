import asyncio
import os
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext

from aiogram.types import Message

from database import save_users, get_users, init_db
from states import Questionnarie

from dotenv import load_dotenv
load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

bot = Bot(token=BOT_TOKEN)

dp = Dispatcher()


@dp.message(CommandStart())
async def start_command(message: Message):
    await  message.answer('Привет я твой первый бот. Ты крутышка. lumos club')

@dp.message(Command(commands=['info']))
async def state_command(message: Message, state: FSMContext):
    await state.set_state(Questionnarie.full_name)
    await message.answer('Ваше ФИО')

@dp.message(Questionnarie.full_name)
async def name_command(message: Message, state: FSMContext):
    await state.update_data(full_name=message.text)
    await state.set_state(Questionnarie.age)
    await message.answer('Введите пароль:')

@dp.message(Questionnarie.age)
async def age_command(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await state.set_state(Questionnarie.gender)
    await message.answer('Ваш пол')



@dp.message(Questionnarie.gender)
async def gender_command(message: Message, state: FSMContext):
    await state.update_data(gender=message.text)
    await state.set_state(Questionnarie.profession)
    await message.answer('Кем вы работаете?')


@dp.message(Questionnarie.profession)
async def profession_command(message: Message, state: FSMContext):
    data = await state.get_data()
    await message.answer(f'ФИО: {data.get("full_name")}\n'
                         f'Юзер {message.from_user.username}\n'
                         f'Возраст: {data.get("age")}\n'
                        f"Пол: {data.get('gender')}\n"
                         f"Работа: {message.text}")
    username = data.get("full_name")
    password = data.get("age")
    save_users(username, password)

    await state.clear()


@dp.message(Command('get_users'))
async def get_users_command(message: Message):
    users = get_users()
    await message.answer(users)





@dp.message(Command("help"))
async def help_command(message: Message):
    help_text = (
        "/start — старт команда\n"
        "/photo — обработчик фоток\n"
        "/text — обработчик текста"
    )
    await message.reply(help_text)


@dp.message(F.photo)
async def photo_command(message: Message):
    await message.reply('Классная фотка')


@dp.message(F.text)
async def text_command(message: Message):
    await message.answer(f'Ты написал {message.text}')



async def main():
    await dp.start_polling(bot)


init_db()


if __name__=='__main__':
    asyncio.run(main())




