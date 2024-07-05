# config_singleton.py
import json

class Config:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance._load_config()
        return cls._instance

    def _load_config(self):
        # Carregar a configuração de um arquivo JSON
        try:
            with open('config.json', 'r') as f:
                self._config = json.load(f)
        except FileNotFoundError:
            # Usar uma configuração padrão se o arquivo não for encontrado
            self._config = {
                "database": "MySQL",
                "host": "localhost",
                "port": 3306
            }

    def get_config(self):
        return self._config

    def update_config(self, key, value):
        self._config[key] = value
        # Atualizar o arquivo de configuração
        with open('config.json', 'w') as f:
            json.dump(self._config, f, indent=4)

if __name__ == "__main__":
    config1 = Config()
    config2 = Config()

    print("Config 1:", config1.get_config())
    print("Config 2:", config2.get_config())
    print("São a mesma instância?", config1 is config2)
