langs = {'cy': 'Валлійська', 'tl': 'Тагальська', 'sk': 'Словацька',
         'bg': 'Болгарська', 'ml': 'Малаялам', 'sr': 'Сербська', 'jv': 'Яванська',
         'ar': 'Арабська', 'mt': 'Мальтійська', 'tr': 'Турецька', 'tg': 'Таджицька',
         'lo': 'Лаоська', 'id': 'Індонезійська', 'pl': 'Польська',
         'az': 'Азербайджанська', 'el': 'Грецька', 'ca': 'Каталанська',
         'fa': 'Перська', 'cs': 'Чеська', 'kn': 'Каннада', 'en': 'Англійська',
         'mg': 'Малагасійська', 'gl': 'Галісійська', 'my': 'Бірманська',
         'la': 'Латина', 'uk': 'Українська', 'ka': 'Грузинська', 'ru': 'Російська',
         'no': 'Норвезька', 'si': 'Сингальська', 'pap': "Пап'яменто",
         'lv': 'Латиська', 'gu': 'Гуджараті', 'bs': 'Боснійська',
         'mrj': 'Гірськомарійська', 'ta': 'Тамільська', 'ur': 'Урду',
         'su': 'Сунданська', 'mk': 'Македонська', 'ky': 'Киргизька',
         'pa': 'Пенджабська', 'sv': 'Шведська', 'hu': 'Угорська', 'ko': 'Корейська',
         'zh': 'Китайська', 'sw': 'Суахілі', 'eu': 'Баскська',
         'nl': 'Нідерландська', 'he': 'Іврит', 'udm': 'Удмуртська',
         'ga': 'Ірландська', 'hy': 'Вірменська', 'th': 'Тайська', 'xh': 'Коса',
         'kk': 'Казахська', 'lt': 'Литовська', 'af': 'Африкаанс',
         'tt': 'Татарська', 'ja': 'Японська', 'ro': 'Румунська', 'de': 'Німецька',
         'uz': 'Узбецька', 'sq': 'Албанська', 'it': 'Італійська', 'fi': 'Фінська',
         'bn': 'Бенгальська', 'hr': 'Хорватська', 'is': 'Ісландська',
         'mn': 'Монгольська', 'te': 'Телугу', 'mr': 'Маратхі', 'ht': 'Гаїтянська',
         'fr': 'Французька', 'eo': 'Есперанто', 'be': 'Білоруська', 'et': 'Естонська',
         'pt': 'Португальська', 'mi': 'Маорі', 'es': 'Іспанська', 'da': 'Данська',
         'ceb': 'Себуанська', 'am': 'Амхарська', 'ne': 'Непальська', 'ms': 'Малайська',
         'ba': 'Башкирська', 'sl': 'Словенська', 'km': 'Кхмерська', 'mhr': 'Марійська',
         'hi': 'Хінді', 'yi': 'Ідиш', 'lb': 'Люксембурзька', 'vi': "В'єтнамська",
         'gd': 'Шотландська (гельська)'}


top_langs = {'en': 'Англійська', 'it': 'Італійська', 'de': 'Німецька',
             'fr': 'Французька', 'pl': 'Польська', 'es': 'Іспанська',
             'uk': 'Українська', 'ru': 'Російська'}

users_data = {}

def user_exist(chat_id):
    if str(chat_id) in users_data:
        return True
    else:
        return False

def add_user(chat_id, usr_lang):
    users_data[str(chat_id)] = \
        str(list(langs.keys())[list(langs.values()).index(str(usr_lang))])

def change_langs(chat_id, usr_lang):
    users_data[str(chat_id)] = \
        str(list(langs.keys())[list(langs.values()).index(str(usr_lang))])

def change_top_langs(chat_id, usr_lang):
    users_data[str(chat_id)] = \
        str(list(top_langs.keys())[list(top_langs.values()).index(str(usr_lang))])