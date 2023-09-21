import yaml

class PhraseManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(PhraseManager, cls).__new__(cls)
        return cls._instance

    def __init__(self, config_path="config/phrases.yaml"):
        if not hasattr(self, "phrases"):
            with open(config_path, 'r', encoding='utf-8') as file:
                self.phrases = yaml.safe_load(file)

    def _get_nested(self, data, keys):
        """Получает вложенное значение из словаря по списку ключей."""
        if keys and data:
            key = keys[0]
            if key in data:
                return self._get_nested(data[key], keys[1:])
        return data

    def t(self, key_string, *args, **kwargs):
        keys = key_string.split(".")
        phrase = self._get_nested(self.phrases, keys)
        if isinstance(phrase, str):
            return phrase.format(*args, **kwargs)
        return None
