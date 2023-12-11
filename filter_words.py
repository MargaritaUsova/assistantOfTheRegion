import string

BAN_WORDS = set(line.strip() for line in open('resource/ban_words.txt'))

def check_message(message):
    contains_ban_word = False

    if message:
        message_words = set(message.translate(str.maketrans('', '', string.punctuation)).split())
        for word in message_words:
            if word.lower() in BAN_WORDS:
                contains_ban_word = True

    return contains_ban_word