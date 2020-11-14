from aiogram.dispatcher.filters.state import State, StatesGroup

class Student(StatesGroup):
    zero_status = State()
    StudentName = State()
    FinishSummary = State()

class Worker(StatesGroup):
    Worker = State()