from .censored_words import CENSORED_WORDS

def filter_comment(comment):
    for word in CENSORED_WORDS:
        if word in comment.content:
            return False  # Неподобающий комментарий
    return True  # Подобающий комментарий