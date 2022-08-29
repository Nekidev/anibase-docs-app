import json

def get_translated_string(language: str, page: str, key: str, default_language: str = "English"):
    """Returns the translated string if it exists, otherwise the original string."""
    translations = json.load(open(f"translations\{page}.json", "r", encoding="utf-8"))
    return translations[language][key] if language in translations and key in translations[language] else translations[default_language][key]