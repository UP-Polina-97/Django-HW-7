from random import randrange
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from Vk_information import get_users_for_date, age_preferences, get_photos_vk_data

token = input('Token for groupchat in vk: ')
# token = ''

vk = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk)

user_id_fromWR = []


def bot_write_msg(user_id, message):
    """THis is a bot that can help you to find love give messages"""
    vk.method('messages.send', {
        'user_id': user_id,
        'message': message,
        'random_id': randrange(10 ** 7), })


def bot_send_photo(user_id, message, url):
    """THis is a bot that can help you to find love give photos"""
    vk.method('messages.send', {
        'user_id': user_id,
        'message': message,
        'attachment': url,
        'random_id': randrange(10 ** 7)})


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:

        if event.to_me:
            request = event.text

            if request == "привет":
                bot_write_msg(event.user_id,
                              f"Привет я бот для try try me. Я могу помочь вам найти пару. Вам помочь? :D")
                user_id_fromWR.append(event.text)
            elif request == "да":
                bot_write_msg(event.user_id, "Какой вай возвратной диапазон? \n 1. 18-24 лет"
                                             "\n2. 25-34 лет"
                                             "\n3. 35-44 лет"
                                             "\n4. 45-54 лет"
                                             "\n5. 55-64 лет"
                                             "\n6. 65-74 лет"
                                             "\n7. 75 лет и старше "

                                             "\nПожалуйста выберите любой из этих категорий и напишите номер в чат. :-)")
            elif request == '1':
                name, id_of_person, photos = get_users_for_date(event.user_id, 1)
                for name, id, photo in zip(name, id_of_person, photos):
                    bot_write_msg(event.user_id, f"{name}\n https://vk.com/id{id} {photo}")
                    # BotSendPhoto(event.user_id, f"{photo}", photo)

            elif request in age_preferences.keys():
                photo, name, id_of_person = get_users_for_date(event.user_id, age_preferences[request])
                for name, id, photo in zip(name, id_of_person, photo):
                    bot_send_photo(event.user_id, f"{name} https://vk.com/id{id} \n", photo)



            elif request == "пока":
                bot_write_msg(event.user_id, "Пока((")
            else:
                bot_write_msg(event.user_id, "Не поняла вашего ответа...")



