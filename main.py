import os
from os.path import join, dirname
from time import sleep
from dotenv import load_dotenv

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import Application, CallbackQueryHandler, CommandHandler

from parser import parse, printVacancie

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

reply_keyboard = [
    ["/parse", "/stop"],
]

#Включаем кнопки
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)

async def start(update, context):
    await update.message.reply_text('Привет! Этот бот поможет в поиске работы.', reply_markup=markup)

async def stop(update, context):
    await update.message.reply_text('stop work')
    
async def parse_vacancies(update, context):
    '''Функция отвечает за парсинг и вывод вакансии'''
    parse()
    data = printVacancie()
    name = data[0]
    city = data[1]
    salary = data[2]
    url =  data[3]
    await update.message.reply_text(f'Вакансия: {name}\n Город: {city}\n Зарплата: {salary}\n Ссылка: {url}', reply_markup=markup)
    sleep(5)

def main():
    #Инцилизируем бота и задаем команды
    application = Application.builder().token(TELEGRAM_TOKEN).build()
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('parse', parse_vacancies))
    application.add_handler(CommandHandler('stop', stop))
    application.run_polling()
    
    
if __name__ == "__main__":
    main()
