from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import random
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.environ["BOT_TOKEN"]

# Встав сюди свій словник:
# words = {"keep": ["зберігати"], ...}
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
    "say": ["казати"],
    "see": ["бачити"],
    "seek": ["шукати"],
    "sell": ["продавати"],
    "send": ["посилати"],
    "shoot": ["стріляти"],
    "show": ["показувати"],
    "shut": ["закривати"],
    "sing": ["співати"],
    "sleep": ["спати"],
    "speak": ["говорити"],
    "spend": ["витрачати"],
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

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # надсилаємо перше слово
    word = random.choice(list(words.keys()))
    context.user_data["current_word"] = word
    await update.message.reply_text(f"Переклади слово: {word}")

async def handle_response(update: Update, context: ContextTypes.DEFAULT_TYPE):
    answer = update.message.text.strip().lower()
    word = context.user_data.get("current_word")

    if not word:
        # якщо раптом нема поточного слова — стартуємо заново
        return await start(update, context)

    correct = [t.lower().strip() for t in words[word]]
    if answer in correct:
        await update.message.reply_text("✅ Правильно!")
    else:
        await update.message.reply_text(f"❌ Неправильно. Правильна відповідь: {', '.join(words[word])}")

    # чекаємо 1 секунду і надсилаємо нове слово
    await asyncio.sleep(1)
    new_word = random.choice(list(words.keys()))
    context.user_data["current_word"] = new_word
    await update.message.reply_text(f"Переклади слово: {new_word}")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_response))

    print("✅ Бот запущено!")
    app.run_polling()

if __name__ == "__main__":
    main()
