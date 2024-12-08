import telebot

TOKEN ='7564324863:AAFC6NkmCRXIzPSk3phBCjkLV3OvVhY0L_0'
bot = telebot.TeleBot(TOKEN)

car_marka = {
    '1': "Toyota",
    '2': "BMW",
    '3': "Mercedes"
}

assortment = {
    '1': ("Чорна ручка", 150),
    '2': ("Синя ручка", 180),
    '3': ("Червона ручка", 200)
}

user_choices = {}

@bot.message_handler(commands=['start'])
def welcome(message):
    user_choices[message.chat.id] = {}
    bot.send_message(
        message.chat.id,
        "Привіт! Ось доступні марки автомобілів:\n"
        "1. Toyota\n"
        "2. BMW\n"
        "3. Mercedes\n"
        "Напишіть номер марки, щоб продовжити."
    )

@bot.message_handler(func=lambda message: message.chat.id not in user_choices)
def handle_new_user(message):
    welcome(message)

@bot.message_handler(func=lambda message: message.chat.id in user_choices and 'car_marka' not in user_choices[message.chat.id])
def choose_car_marka(message):
    marka_number = message.text.strip()

    if marka_number in car_marka:
        user_choices[message.chat.id]['car_marka'] = car_marka[marka_number]
        bot.send_message(
            message.chat.id,
            "Ви обрали марку автомобіля: {0}.\n\nОберіть колір ручки:\n"
            "1. Чорна — 150 грн\n"
            "2. Синя — 180 грн\n"
            "3. Червона — 200 грн\n"
            "Напишіть номер кольору ручки.".format(car_marka[marka_number])
        )
    else:
        bot.send_message(message.chat.id, "Невірний номер марки. Виберіть номер з доступних (1, 2 або 3).")

@bot.message_handler(func=lambda message: message.chat.id in user_choices and 'car_marka' in user_choices[message.chat.id] and 'item' not in user_choices[message.chat.id])
def choose_item(message):
    item_number = message.text.strip()

    if item_number in assortment:
        user_choices[message.chat.id]['item'] = assortment[item_number]
        item_name, price = assortment[item_number]
        car_marka = user_choices[message.chat.id]['car_marka']

        bot.send_message(
            message.chat.id,
            f"Ви обрали:\n"
            f"Марка автомобіля: {car_marka}\n"
            f"Ручка: {item_name} — {price} грн\n\n"
            f"Дякуємо за замовлення!"
        )
        user_choices[message.chat.id] = {}
    else:
        bot.send_message(message.chat.id, "Невірний номер ручки. Виберіть номер з асортименту (1, 2 або 3).")

bot.polling(none_stop=True)
