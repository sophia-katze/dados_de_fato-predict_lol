# Previsão de uma partida de League of Legends

Este projeto, de autoria de  Mário Vasconcelos e Sophia Helena de Paula, faz parte do desafio da comunidade Dados de Fato, cujo tema é: "Jogos Digitais".

 Consiste de  uma aplicação Streamlit que permite ao usuário fazer previsões usando um modelo de aprendizado de máquina. O usuário pode selecionar posições, escolher personagens para banir e escolher um personagem para jogar. A aplicação então faz uma solicitação para uma API que retorna a previsão do modelo.

## Como usar

1. Execute a aplicação Streamlit (main.py).
2. No menu dropdown "Escolha 5 roles:", selecione as posições desejadas.
3. No menu "Escolha 3 bans:", selecione os personagens que você deseja banir.
4. No menu "Escolha 1 pick:", selecione o personagem que você deseja jogar.
5. Clique no botão "Fazer Previsão" para obter a previsão do modelo.

## Detalhes da Implementação

A aplicação lê um arquivo CSV que contém informações sobre os personagens do jogo. Ela mapeia os nomes dos personagens para seus respectivos IDs e cria um payload com essas informações, juntamente com as posições selecionadas e os personagens banidos. Este payload é então enviado para a API, que retorna a previsão do modelo.

## Dependências

- pandas
- scikit-learn
- flask
- seaborn
- gunicorn
- tensorflow v2.15.0
- keras v2.15.0
- streamlit
