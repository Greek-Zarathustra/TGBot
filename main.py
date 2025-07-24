from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import random
import os
from dotenv import load_dotenv

# Завантажити змінні середовища
load_dotenv()
TOKEN = os.environ["BOT_TOKEN"]

# Глобальні словники
words = {}
current_word = {}

# Зчитати слова з файлу words.txt
def load_words(filename="words.txt"):
    result = {}
    try:
        with open(filename, encoding="utf-8") as f:
            for line in f:
                if ":" in line:
                    eng, ukr = line.strip().split(":", 1)
                    translations = [word.strip().lower() for word in ukr.split(",")]
                    result[eng.strip().lower()] = translations
    except Exception as e:
        print(f"Помилка при завантаженні слів: {e}")
    return result

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global words
    user_id = update.effective_user.id
    word = random.choice(list(words.keys()))
    current_word[user_id] = word
    await update.message.reply_text(f"Переклади слово: {word}")

async def handle_response(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    answer = update.message.text.strip().lower()

    word = current_word.get(user_id)
    correct_answers = words.get(word, [])

    if not word or not correct_answers:
        # Просто обираємо нове слово, як ні в чому не бувало
        new_word = random.choice(list(words.keys()))
        current_word[user_id] = new_word
        await update.message.reply_text(f"👉 Слово для перекладу: {new_word}")
        return

    normalized_correct_answers = [ans.strip().lower() for ans in correct_answers]

    if answer in normalized_correct_answers:
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

    # Обираємо нове слово
    new_word = random.choice(list(words.keys()))
    current_word[user_id] = new_word
    await update.message.reply_text(f"\n👉 Наступне слово: {new_word}")

# Основна функція запуску бота
def main():
    global words
    words = load_words("words.txt")

    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_response))

    print("✅ Бот запущено!")
    app.run_polling()

if __name__ == "__main__":
    main()
