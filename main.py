from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import random
import os


# Словник для тренування — тепер значення це список правильних варіантів
words = {
"keep": ["зберігати", "продовжувати"],
"hurt": ["пошкодити, шкодити"],
"become": ["ставати"],
"begin": ["починати"],
"bring": ["приносити"],
"buy": ["купляти"],
"catch": ["зловити"],
"choose": ["вибирати", "вибрати"],
"come": ["приходити"],
"cry": ["плакати"],
"dream": ["мріяти"],
"draw": ["малювати"],
"drink": ["пити"],
"eat": ["їсти"],
"fall": ["падати"],
"feel": ["відчувати"],
"fight": ["битися"],
"find": ["знаходити"],
"fly": ["літати"],
"forget": ["забувати"],
"forgive": ["пробачати"],
"feed": ["годувати"],
"get": ["отримати"],
"give": ["давати"],
"hide": ["ховати"],
"hear": ["чути"],
"hit": ["вдаряти"],
"hold": ["тримати"],
"know": ["знати"],
"lay": ["класти"],
"learn": ["дізнаватися"],
"leave": ["залишати"],
"let": ["дозволяти"],
"lie": ["брехати"],
"lose": ["програвати"],
"make": ["робити"],
"lend": ["позичати"],
"mean": ["мати на увазі"],
"meet": ["зустрічати"],
"pay": ["платити"],
"put": ["класти"],
"read": ["читати"],
"rid": ["позбуватися"],
"say": ["казати"],
"see": ["бачити"],
"seek": ["шукати"],
"sell": ["продавати"],
"send": ["посилати"],
"shoot": ["стріляти"],
"show": ["показувати"],
"shut": ["закривати"],
"sing": ["співати"],
"sit": ["сидіти"],
"sleep": ["спати"],
"speak": ["говорити"],
"spend": ["витрачати"],
"stand": ["стояти"],
"steal": ["красти"],
"swim": ["плавати"],
"take": ["брати"],
"teach": ["навчати"],
"tell": ["розповідати"],
"think": ["думати"],
"understand": ["розуміти"],
"throw": ["кидати"],
"wear": ["носити одяг"],
"win": ["вигравати"],
"write": ["писати"],
"look": ["глянути"],
"use": ["використовувати"],
"want": ["хотіти"],
"work": ["працювати"],
"call": ["дзвонити"],
"try": ["спробувати"],
"ask": ["запитати"],
"need": ["потребувати"],
"seem": ["здається, здаватися"],
"turn": ["повертати"],
"follow": ["слідувати"],
"help": ["допомагати"],
"start": ["починати"],
"run": ["бігати"],
"move": ["рухатися"],
"believe": ["вірити"],
"set": ["встановлювати"],
"allow": ["дозволяти"],
"live": ["жити"],
"happen": ["траплятися"],

    # додай інші слова за потребою
}

# Пам'ятаємо, яке слово ми задали користувачу
current_word = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    word = random.choice(list(words.keys()))
    current_word[user_id] = word
    await update.message.reply_text(f"Переклади слово: {word}")

async def handle_response(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    answer = update.message.text.strip().lower()

    word = current_word.get(user_id, "")
    correct_answers = words.get(word, [])

    if answer in correct_answers:
        correct_responses = [
            "✅ Правильно",
            "🎉 Молодець! Все вірно!",
            "🧠 Красава! Точно в ціль!",
            "🔥 Та ти розумник! В яблучко!",
            "😎 Молодчинка",
            "💪 Так тримати",
            "🤙 Вау та ти крутий",
            "🤌 Перфекто!",
            "🤓 Ти що відмінник? Дивовижно!!!",
            "👌 ОК",
            "🍾 Відкрию пляшку за тебе",
            "🍷 П'ю за твоє здоров'я",
            "🌝 Файно",
            "🌚 Ніфіга собі, грамотно!",
            "💙💛 Україна гордитиметься тобою",
        ]
        await update.message.reply_text(random.choice(correct_responses))
    else:
        correct_display = ", ".join(correct_answers)
        incorrect_responses = [
            f"❌ ТАДЕЙ! думай трохи🤡, Правильна відповідь: {correct_display}",
            f"🙃 Мимо! Було треба: {correct_display}",
            f"🚫 Не вгадано. Правильно буде: {correct_display}",
            f"⚠️ Ти серйозно зараз? Правильно: {correct_display}",
            f"🤬 Фу аж гидко Правильно: {correct_display}",
            f"🥴 Очі болять від такого... Правильно: {correct_display}",
            f"⛔ Мені за тебе соромно. Правильно: {correct_display}",
            f"💀 ЩОООО??? Правильно: {correct_display}",
            f"💩💩💩💩💩 Правильно: {correct_display}",
            f"🫵🫵🫵 Ось невдаха, ХА ХА Правильно: {correct_display}",
            f"🩻 Бот провів МРТ... Там пусто. Правильно: {correct_display}",
            f"⚰️ Твої знання померли. RIP. Правильно: {correct_display}",
            f"🗿🗿🗿 Нема слів. Правильно: {correct_display}",
            f"🚫 Тадей не позорся, вчись трохи. Правильно: {correct_display}",
            f"🧬 ДНК аналіз показав: ген англійської відсутній. Правильно: {correct_display}",
        ]
        await update.message.reply_text(random.choice(incorrect_responses))

    # Нова спроба
    await start(update, context)

def main():
    print("Environment variables keys:", list(os.environ.keys()))
    TOKEN = os.environ["BOT_TOKEN"]
    print("TOKEN is found")
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_response))

    print("Бот запущено!")
    app.run_polling()

if __name__ == "__main__":
    main()
print("Environment variables:", os.environ)