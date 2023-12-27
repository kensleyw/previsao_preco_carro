# ValorAuto App

## Descrição
Este repositório contém o código-fonte de uma aplicação web chamada ValorAuto. Essa aplicação realiza a precificação de veículos com base em um modelo preditivo treinado. O treinamento do modelo está documentado no arquivo `analise_modelo_preditivo.ipynb`.

## Objetivo
O objetivo principal do ValorAuto App é automatizar e otimizar a definição dos preços dos carros que serão vendidos pela empresa. A aplicação utiliza um modelo preditivo construído com base em características dos veículos.

## Conteúdo do Repositório
- `relatorio.html`: Documento de analise exploratória, gerado com ydata_profiling.
- `analise_modelo_preditivo.ipynb`: Notebook Jupyter que contém a análise exploratória de dados, treinamento do modelo preditivo e seleção dos melhores parâmetros.
- `app.py`: Script Streamlit que implementa a interface da aplicação web. Permite ao usuário inserir os dados do veículo e fornece uma estimativa do preço com base no modelo treinado.
- `modelo.joblib`: Arquivo binário que armazena o modelo preditivo treinado para a precificação de veículos.
- `dados/CarPrice.csv`: Conjunto de dados utilizado para treinar o modelo.

## Como Usar
1. Clone o repositório para sua máquina local.
2. Instale as dependências utilizando o seguinte comando:
    ```bash
    pip install -r requirements.txt
    ```
3. Execute a aplicação utilizando o seguinte comando:
    ```bash
    streamlit run app.py
    ```
4. Abra o navegador e acesse a URL fornecida pelo Streamlit.

## Contato
- **Desenvolvedor:** Kensley William
- **Email:** kensleyw@gmail.com

# Como Colaborar
Se você deseja colaborar com o projeto, ficarei felize em receber sua contribuição! Aqui estão algumas maneiras de colaborar:

1. **Identificando e Relatando Problemas:** Caso encontre algum problema ou bug, por favor, abra uma "issue" no GitHub descrevendo o problema detalhadamente.

2. **Sugestões e Melhorias:** Se tiver ideias para melhorar a aplicação, sinta-se à vontade para abrir uma "issue" com suas sugestões.

3. **Envio de Pull Requests:** Se você já corrigiu um bug ou implementou uma melhoria, envie um "pull request" para que possamos analisar e integrar suas mudanças.

4. **Compartilhamento e Feedback:** Compartilhe a aplicação com seus amigos e colegas, e forneça feedback sobre sua experiência de uso.

Sua contribuição é valiosa para a comunidade. Obrigado por considerar colaborar com o ValorAuto App!

