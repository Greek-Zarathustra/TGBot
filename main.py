from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, CallbackQueryHandler, ContextTypes, filters
import random
import asyncio
import os
from dotenv import load_dotenv

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

def get_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("Пропустити 🔁", callback_data="skip")]
    ])

async def send_new_word(update, context):
    word = random.choice(list(words.keys()))
    context.user_data["current_word"] = word
    await update.message.reply_text(
        f"Переклади слово: {word}",
        reply_markup=get_keyboard()
    )

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_new_word(update, context)

async def handle_response(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_answer = update.message.text.strip().lower()
    word = context.user_data.get("current_word")

    if not word:
        await send_new_word(update, context)
        return

    correct = [w.lower() for w in words.get(word, [])]

    if user_answer in correct:
        await update.message.reply_text("✅ Правильно!")
    else:
        await update.message.reply_text(f"❌ Неправильно. Правильна відповідь: {', '.join(words[word])}")

    await asyncio.sleep(1)
    await send_new_word(update, context)

async def skip_word(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    word = context.user_data.get("current_word")
    if word:
        await query.message.reply_text(f"Правильна відповідь: {', '.join(words[word])}")

    await asyncio.sleep(1)
    new_word = random.choice(list(words.keys()))
    context.user_data["current_word"] = new_word
    await query.message.reply_text(f"Переклади слово: {new_word}", reply_markup=get_keyboard())

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_response))
    app.add_handler(CallbackQueryHandler(skip_word, pattern="^skip$"))

    print("✅ Бот запущено!")
    app.run_polling()

if __name__ == "__main__":
    main()
