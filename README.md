# BCC3004-Padroes-de-Projeto

"Padrões de projeto são soluções típicas para problemas comuns em projeto de software. Eles são como plantas de obra pré fabricadas que você pode customizar para resolver um problema de projeto recorrente em seu código."

## Padrão Criacional 

 Fornecem mecanismos de criação de objetos que aumentam a flexibilidade e a reutilização de código.
 O padrão criacional mais cobrado em concursos publicos é o Singleton, também conhecido como: Carta única
 
## Singleton     
O padrão de projeto SINGLETON garante à exitência de apenas uma instância de uma classe mantendo um ponto global de acesso ao seu objeto.
Este padrão é útil quando uma classe precisa ter exatamente uma instância ativa em todo o sistema para controlar o acesso a um recurso compartilhado ou gerenciar estados globais. Dessa forma então vamos imaginar um problema e uma solução para exemplificar o uso do singleton:

## Problema
Um aplicativo precisa carregar suas configurações de um arquivo JSON apenas uma vez e compartilhar essa configuração entre todos os componentes do sistema. Múltiplas instâncias de configuração podem resultar em inconsistência de dados e comportamento inesperado.

## Solução
Usar o padrão Singleton para garantir que a configuração seja carregada uma única vez e compartilhada globalmente.


## Diagrama UML
![Singleton UML](https://refactoring.guru/images/patterns/diagrams/singleton/structure-en.png) 


## Código
A classe `Config` carrega a configuração de um arquivo JSON na primeira vez que é instanciada. Todas as chamadas subsequentes usam a mesma instância de configuração.

### Arquivo `config_singleton.py`

```python
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
        try:
            with open('config.json', 'r') as f:
                self._config = json.load(f)
        except FileNotFoundError:
            self._config = {
                "database": "MySQL",
                "host": "localhost",
                "port": 3306
            }

    def get_config(self):
        return self._config

    def update_config(self, key, value):
        self._config[key] = value
        with open('config.json', 'w') as f:
            json.dump(self._config, f, indent=4)