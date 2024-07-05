# BCC3004-Padroes-de-Projeto

"Padrões de projeto são soluções típicas para problemas comuns em projeto de software. Eles são como plantas de obra pré fabricadas que você pode customizar para resolver um problema de projeto recorrente em seu código."

## Padrão Criacional 

 Fornecem mecanismos de criação de objetos que aumentam a flexibilidade e a reutilização de código.
 O padrão criacional mais cobrado em concursos publicos é o Singleton, também conhecido como: Carta única
 
## Singleton     
O padrão de projeto SINGLETON garante à exitência de apenas uma instância de uma classe mantendo um ponto global de acesso ao seu objeto.
Este padrão é útil quando uma classe precisa ter exatamente uma instância ativa em todo o sistema para controlar o acesso a um recurso compartilhado ou gerenciar estados globais.

Imagine que você está desenvolvendo um sistema que deve usar apenas uma instância de uma classe para:
- Gerenciar uma configuração global. 

Criar múltiplas instâncias de tais classes pode resultar em comportamento indesejado, desperdício de recursos ou inconsistência de dados.

- Solução

O Singleton resolve isso garantindo que uma classe tenha apenas uma instância, fornecendo um ponto de acesso global a essa instância. Ele pode controlar a criação da instância e garantir que não sejam criadas outras instâncias.