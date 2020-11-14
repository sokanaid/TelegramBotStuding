from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
# Кнопки выбора типа собеседника: Студент/Работодатель.
btnUserTypeStudent = KeyboardButton("Студент")
btnUserTypeWorker = KeyboardButton("Работодатель")
choose_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
choose_kb.add(btnUserTypeStudent)
choose_kb.add(btnUserTypeWorker)

# Кнопки заполения резюме студента.
btnUserSendRSummary = KeyboardButton("Заполнить резюме")
btnBack = KeyboardButton("Отмена")
SendRSummary = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
SendRSummary.add(btnUserSendRSummary)
SendRSummary.add(btnBack)

BackOnly = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(btnBack)