from translations.translationsSelector import getTranslations

translationNotFound = "Translation not defined"

class Translator:
  def __init__(self, langKey):
    self.translations = getTranslations(langKey)

  def getTranslation(self, translationKey):
    return self.translations.get(translationKey, translationNotFound)
