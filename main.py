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

# Обробка відповіді
async def handle_response(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    answer = update.message.text.strip().lower()

    word = current_word.get(user_id, "")
    correct_answers = words.get(word, [])

    if not word or not correct_answers:
        await update.message.reply_text("⚠️ Я не знаю, яке слово ти перекладаєш. Напиши /start, щоб почати заново.")
        return

    if answer in correct_answers:
        responses = [
            "✅ Правильно",
            "🎉 Молодець! Все вірно!",
            "🧠 Красава! Точно в ціль!",
            "🔥 Та ти розумник!",
            "😎 Молодчинка",
            "💪 Так тримати",
            "🤙 Вау та ти крутий",
        ]
        await update.message.reply_text(random.choice(responses))
    else:
        correct_display = ", ".join(correct_answers)
        incorrect_responses = [
            f"❌ Ні, правильно: {correct_display}",
            f"🙃 Мимо! Треба: {correct_display}",
            f"🩻 Бот провів МРТ... Там пусто. Правильно: {correct_display}",
            f"💀 ЩОООО??? Правильно: {correct_display}",
        ]
        await update.message.reply_text(random.choice(incorrect_responses))

    await start(update, context)

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
