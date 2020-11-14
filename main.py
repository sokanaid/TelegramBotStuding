import logging
import config
import KeyBords
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import States
from aiogram.utils import deep_linking
bot = Bot(config.token)
dp = Dispatcher(bot,storage=MemoryStorage())

@dp.message_handler(commands=['start'], state= '*')
async def send_welcome(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, "Привет, пожалуйста, выбери кем ты являешься.", reply_markup=KeyBords.choose_kb)
    await States.Student.first();

@dp.message_handler(text=['Студент'], state=States.Student.zero_status)
async def choose_student(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, "Привет, заполни, пожалуйста, резюме.", reply_markup=KeyBords.SendRSummary)
    await States.Student.next()

@dp.message_handler(text=['Работодатель'],state=States.Student.zero_status)
async def choose_worker(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, "Привет Работодатель", reply_markup=KeyBords.BackOnly)

@dp.message_handler(text=['Отмена'],state='*')
async def back(message: types.Message, state: FSMContext):

    await States.Student.zero_status.set()
    await send_welcome(message,state)

@dp.message_handler(text=['Заполнить резюме'], state = States.Student.StudentName)
async def send_name(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, "Напиши ФИО.")
    await States.Student.next()

@dp.message_handler( state=States.Student.FinishSummary)
async def finish_summary(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, "Спасибо, "+message.text+", что заполнили анкету.", reply_markup=KeyBords.BackOnly)
    await state.finish()
if __name__ == '__main__':
     executor.start_polling(dp, skip_updates=True)