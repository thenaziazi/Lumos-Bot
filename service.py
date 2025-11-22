```python
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
```