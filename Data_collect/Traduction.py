from textblob import TextBlob


def traduction(text, language):
    '''Prend en argument un texte et la langue dans laquelle on veut traduire le texte et le traduit.

    PARAMETRE:

    text = str, language = str de la forme "en", "fr", soit en ISO 639-1

    '''
    blob = TextBlob(text)
    if blob.detect_language() != language:
        return blob.translate(to=language)
    else:
        return text
