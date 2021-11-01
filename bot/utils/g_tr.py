from googletrans import Translator


def google_tr(text: str, dest: str = 'en') -> str:
    """
    return the tranlated text
    """
    translator = Translator()
    tranlated = translator.translate(text=text, dest=dest).text
    return tranlated


