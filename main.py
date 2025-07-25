from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import random
import os
from dotenv import load_dotenv

# Завантажуємо змінні середовища з .env
load_dotenv()
TOKEN = os.environ["BOT_TOKEN"]

# Словник слів
words = {
    "keep": ["зберігати", "продовжувати"],
    "hurt": ["пошкодити"],
    "become": ["ставати"],
    "begin": ["починати"],
    "bring": ["приносити"],
    "buy": ["купляти"],
    "catch": ["зловити"],
    "choose": ["вибирати"],
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
    "seem": ["здається"],
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
    "carry": ["нести"],
    "talk": ["розмовляти", "говорити"],
    "appear": ["з'являтися"],
    "offer": ["пропонувати"],
    "expect": ["очікувати"],
    "suggest": ["пропонувати"],
    "continue": ["продовжувати"],
    "add": ["додавати"]
}

# Команда /start або /next
async def next_word(update: Update, context: ContextTypes.DEFAULT_TYPE):
    word = random.choice(list(words.keys()))
    context.user_data["current_word"] = word
    await update.message.reply_text(f"Переклади слово: {word}")

# Обробка відповіді користувача
async def handle_response(update: Update, context: ContextTypes.DEFAULT_TYPE):
    answer = update.message.text.strip().lower()
    word = context.user_data.get("current_word")

    if not word:
        await update.message.reply_text("Натисни /start або /next, щоб отримати слово.")
        return

    correct_answers = words.get(word, [])
    normalized = [ans.lower().strip() for ans in correct_answers]

    if answer in normalized:
        await update.message.reply_text("✅ Правильно!")
    else:
        correct_display = ", ".join(correct_answers)
        await update.message.reply_text(f"❌ Неправильно. Правильна відповідь: {correct_display}")

    # Очікуємо, поки користувач викличе /next
    context.user_data["current_word"] = None

# Запуск бота
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", next_word))
    app.add_handler(CommandHandler("next", next_word))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_response))

    print("✅ Бот запущено!")
    app.run_polling()

if __name__ == "__main__":
    main()
