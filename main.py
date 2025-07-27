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
    "adverse": ["Несприятливий", "шкідливий"],
"absence": ["Відсутність"],
"accumulate": ["Наростити", "накопичувати"],
"arrange": ["Влаштувати", "організувати"],
"astray": ["Збитися з дороги"],
"accomplish": ["Виконати"],
"assault": ["Нападати", "Напад"],
"ambush": ["Атакувати"],
"agitate": ["Збуджувати", "хвилювати"],
"attempt": ["Спроба"],
"abundance": ["Достаток", "багатство"],
"admonish": ["Наставляти"],
"anticipate": ["Передбачити"],
"abandon": ["Відмовитися"],
"appealing": ["Привабливий"],
"animosity": ["Злоба"],
"atonement": ["Спокута"],
"absolution": ["Прощення гріхів", "виправдання"],
"audacity": ["Зухвалість"],
"assemble": ["Зібрати"],
"avail": ["Користь"],
"auspicious": ["Сприятливий"],
"awe": ["Вселяти страх"],
"attend": ["Відвідувати", "супроводжувати"],
"appalled": ["Приголомшений"],
"ardent": ["Палкий"],
"allure": ["Привабливість"],
"attest": ["Свідчити"],
"aggrieve": ["Ображати"],
"affection": ["Прихильність"],
"abyss": ["Безодня"],
"accede": ["Приєднатися"],
"burden": ["Ярмо", "тягар"],
"by-product": ["Побічний продукт"],
"bamboozled": ["Обдурений"],
"beholder": ["Спостерігач"],
"baseless": ["Безпідставний"],
"bummer": ["Облом"],
"benign": ["Доброякісний"],
"compelled": ["Змушений"],
"corroborate": ["Підтвердити"],
"caution": ["Попереджати"],
"consequence": ["Наслідок (рідко Мати значення)"],
"culprit": ["Винуватець"],
"confine": ["Ув’язнити", "обмежувати"],
"consume": ["Поглинати"],
"covet": ["Прагнути", "жадати"],
"contemplate": ["Споглядати", "міркувати"],
"contribution": ["Внесок"],
"complacent": ["Самовдоволений"],
"curveball": ["Несподівана проблема"],
"conquests": ["Завоювання"],
"conduct": ["Проводити"],
"conducive": ["Сприяти", "сприятливий"],
"cease": ["Припинити"],
"comrade": ["Товариш"],
"congregate": ["Збиратися", "сходитися"],
"cater": ["Обслуговувати (рідко Вгоджати)"],
"conjecture": ["Припущення"],
"crucial": ["Вирішальне значення"],
"collide": ["Зіткнутися"],
"cling": ["Чіплятися"],
"cherish": ["Плекати"],
"consent": ["Дозвіл"],
"clash": ["Зіткнутися"],
"convey": ["Передати"],
"coax": ["Вмовляти", "підлещуватись"],
"conspicuous": ["Помітний"],
"commotion": ["Метушня"],
"circumvent": ["Обійти"],
"complicit": ["Співучасний"],
"comprehension": ["Розуміння"],
"custody": ["Опіка"],
"cast": ["Відкинути", "кинути"],
"contradiction": ["Протиріччя"],
"conceited": ["Зарозумілий"],
"compression": ["Стиснення", "тиск"],
"compound": ["З’єднувати", "сполучати"],
"consumption": ["Споживання"],
"courtesy": ["Ввічливість"],
"coherent": ["Зв’язаний"],
"crave": ["Жадати"],
"compassionate": ["Жалісливий"],
"compulsion": ["Примус"],
"contempt": ["Неприязнь"],
"conundrum": ["Загадка"],
"condone": ["Потурати"],
"contingency": ["Непередбачувані обставини"],
"catch-up": ["Надолужити"],
"concur": ["Погоджуватись"],
"doomed": ["Приречений"],
"dispose": ["Утилізувати", "здихатися"],
"docket": ["Порядок денний"],
"discrepancy": ["Невідповідність"],
"deplorable": ["Плачевний"],
"descend": ["Знизитися", "опуститися"],
"discern": ["Розрізняти"],
"deify": ["Боготворити"],
"deceive": ["Обманювати"],
"deliberate": ["Навмисний", "радитися"],
"diligent": ["Старанний"],
"diminish": ["Применшувати"],
"dispute": ["Суперечка"],
"distort": ["Спотворювати"],
"distinguish": ["Відрізнити"],
"dicey": ["Ризикований"],
"decompose": ["Розкладатися"],
"defective": ["Несправний"],
"devote": ["Присвятити"],
"deception": ["Обман"],
"detain": ["Затримати"],
"divulge": ["Розголошувати"],
"divine": ["Божественний"],
"deride": ["Висміювати"],
"disillusion": ["Розчарування"],
"defy": ["Кинути виклик"],
"depth": ["Глибина"],
"discretion": ["Розсуд", "секретність"],
"devise": ["Придумати"],
"demean": ["Принижувати"],
"decipher": ["Розшифрувати"],
"drastic": ["Різкий"],
"duplicitous": ["Дволикий"],
"detention": ["Покарання", "затримання"],
"devastated": ["Спустошений"],
"disposition": ["Вдача", "природа"],
"dawdle": ["Марнувати час", "ледарювати"],
"depravity": ["Розбещеність"],
"dissent": ["Інакомислення"],
"deity": ["Божество"],
"demeanor": ["Манера поведінки"],
"deem": ["Вважати"],
"defiance": ["Непокора"],
"dismissive": ["Зневажливий"],
"envoy": ["Посланець"],
"exile": ["Вигнання"],
"endeavor": ["Намагання", "прагнути"],
"erode": ["Роз’їдати"],
"erase": ["Стерти"],
"eventual": ["Остаточний", "можливий"],
"expenditure": ["Витрати"],
"examine": ["Оглянути"],
"excel": ["Відзначатися"],
"errand": ["Доручення"],
"expose": ["Викрити"],
"eradication": ["Викорінення"],
"extend": ["Продовжити", "розширити"],
"escort": ["Супроводжувати"],
"entice": ["Заманювати", "спокушати"],
"endure": ["Терпіти"],
"emerge": ["Виникати"],
"ensnare": ["Ловити в пастку"],
"exaggeration": ["Перебільшення"],
"edict": ["Наказ"],
"eviction": ["Виселення"],
"expense": ["Витрати"],
"excessive": ["Зайвий", "занадто"],
"encounter": ["Зустріч"],
"essence": ["Сутність"],
"flatter": ["Лестити"],
"fawn over": ["Підлещуватись"],
"filth": ["Бруд"],
"figment": ["Вигадка"],
"forsake": ["Покинути"],
"frequently": ["Часто"],
"facilitate": ["Сприяти", "впроваджувати"],
"frown upon": ["Хмуритися", "не схвалювати"],
"festivity": ["Святкування", "урочистість"],
"fragile": ["Крихкий"],
"falter": ["Вагатися", "втрачати впевненість"],
"foment": ["Розпалювати", "підбурювати"],
"foreboding": ["Передчуття"],
"futile": ["Марний"],
"grandeur": ["Велич"],
"grudge": ["Образа"],
"gradually": ["Поступово"],
"grasp": ["Захопити", "осягнути"],
"generalization": ["Узагальнення"],
"gory": ["Кривавий"],
"grueling": ["Виснажливий"]

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
