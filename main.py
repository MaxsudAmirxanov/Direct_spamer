from pyrogram import Client
from pyrogram.types import User
import random
import asyncio
import datetime

#Наш копирайт
# text = {1: "тест1", 2: "test2", 3: "test3"}
text = {
    1: """Приветствую, увидел вас в чате предпринимателей. Я руководитель проектов веб-студии,
создаём продающие сайты на заказ. На счету уже более 20 реализованных проектов, делаем сайты 'под ключ'- 
то есть разработка сайта и маркетинговый этап на нас. Может вам или вашим знакомым понадобится помощь 
специалистов? """,

    2: """Здравствуйте, нашёл вас в чате предпринимателей, меня зовут Роман, моя команда знает, как привлечь
тёплые заявки в бизнес и как вывести его на новый уровень. Скажите, у вас есть свой бизнес? """,

    3: """Доброго времени суток, увидел вас в чате предпринимателей Воронежа. Хочу предложить вам свою услугу) Активно занимаемся
созданием продающих сайтов и упаковкой бизнеса уже полгода. На счету более 20 реализованных проектов, делаем сайты 'под ключ'-то есть
разработка сайта и маркетинговый этап на нас. Вам интересна наша услуга? """,

    4: """Добрый день, нашёл вас в одном из чате предпринимателей. Мы с командой занимаемся разработкой и продвижением сайтов.
Уже реализовали более 20 успешных проектов, создаём сайты 'под ключ', а именно вся разработка, написание текстов и продвижение 
берём на себя. 
Вот наше портфолио: https://www.behance.net/kratosmood
Если вам актуальна наша услуга, созвонюсь с вами на 10 минут и проконсультирую по всем интересующим вопросам.
Что думаете?"""}

#14460056
api_id=11751291
api_hash="facfd37f442048af5bb8aa4107a5b2b9"


app = Client("me", api_id, api_hash )

async def main(v, choice_2, file_name):
    'Рассылка, по базе'
    async with app:

        number_r = random.randint(1,4)
        new_v = v.split('\n')

        index = 0
        for i in new_v:
            if i == '':
                continue
            print(i)
            index += 1
            if index == 1:
                if choice_2 == '3':
                    'Рассылка тестом'
                    first_name = (await app.get_users(i)).first_name
                    await app.send_message(i, f"{first_name} {text[number_r]}")
                    break

                elif choice_2 == '2':
                    'Рассылка с кружочками'
                    await app.send_video_note(i, f"data\{file_name}.mp4")
                    break

                elif choice_2 == '1':
                    'Рассылка с гс'
                    await app.send_audio(i, f"data\{file_name}.ogg")
                    break


async def compiler_chat(chat, file_name):
    "Компилятор чатов"
    await app.start()
    async for user in app.iter_chat_members((await app.get_chat(chat)).id):
        
        timestamp = user.user.last_online_date

        try:
            value = datetime.datetime.fromtimestamp(timestamp)
        except TypeError:
            with open(f'data_for_user/{file_name}.txt', 'a', encoding='utf-8') as file:
                file.write(f"{user.user.username}\n")
                continue



        with open(f'data_for_user/{file_name}.txt', 'a', encoding='utf-8') as file:
            if value.strftime('%Y-%m-%d') == f'2022-03-07' or value.strftime('%Y-%m-%d') == f'2022-03-08' or value.strftime('%Y-%m-%d') == f'2022-03-09' or value.strftime('%Y-%m-%d') == f'2022-03-10' or value.strftime('%Y-%m-%d') == f'2022-03-11' or value.strftime('%Y-%m-%d') == f'2022-03-12' or value.strftime('%Y-%m-%d') == f'2022-03-13':
                file.write(f"{user.user.username}\n")

            else:
                print(f"Последний раз, когда пользовател заходил - {value.strftime('%Y-%m-%d %H:%M:%S')} - {user.user.username}")
            


def spam(data_base):
    number = 0
    choice_1 = int(input("Скольким пользователям хотите отправить сообщение? "))
    choice_2 = input('''
        1) Рассылка с гс
        2) Рассылка с кружочками
        3) Рассылка тестом
        ''')
    if choice_2 == '2':
        file_name = input('Ведите название файла, находящийся в папке data (.mp4 указывать не надо): \n')

    elif choice_2 == '1':
        file_name = input('Ведите название файла, находящийся в папке data (.ogg указывать не надо): \n')
    elif choice_2 == '3':
        file_name = 'Пусто'

    for v in open(f"data_for_user/{data_base}.txt", "r"):
        number += 1

        app.run(main(v, choice_2, file_name))
        if choice_1 == number:
            
    
            #Удаление строк ID, которым сообщение отправилось
            with open(f"data_for_user/{data_base}.txt", 'r') as f:
                lines = f.readlines()

            with open(f"data_for_user/{data_base}.txt", 'w') as f:
                f.writelines(lines[choice_1:])
            break



print('''
1) Запустить рассылку по базе 
2) Скомпилировать пользователей чата
''')
choice = input("Что хотите сделать? ")

if choice == '1':
    data_base = input('Ведите название файла (.txt указываеь не надо): \n')
    

    spam(data_base)

elif choice == '2':
    chat = input('Введите @ чата, который хотите скомпилировать: \n')
    file_name = input('Ведите название нового чата: \n')
    asyncio.run(compiler_chat(chat, file_name))