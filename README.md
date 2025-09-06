# Projeto FarmTech IA

Este repositório contém o código-fonte de um projeto acadêmico para a disciplina de Inteligência Artificial, desenvolvido para a startup fictícia "FarmTech Solutions". O objetivo é criar uma solução baseada em Python e R para auxiliar fazendas na transição para a Agricultura Digital, otimizando o planejamento e o manejo de culturas.

## Funcionalidades

A solução é composta por uma aplicação principal em Python para gerenciamento de dados e scripts em R para análise.

### Aplicação Principal (`main.py` - Python)

- **Menu Interativo:** Uma interface de linha de comando que permite ao usuário navegar por todas as funcionalidades do sistema.
- **Gerenciamento de Áreas (CRUD):**
    - **Cadastrar:** Permite registrar novas áreas de plantio (Cana de Açúcar ou Milho) com suas dimensões.
    - **Listar:** Exibe um relatório detalhado e formatado de todas as áreas cadastradas, com um "laudo" explicando os cálculos.
    - **Atualizar:** Permite modificar as dimensões de uma área já existente, recalculando automaticamente todos os dados dependentes.
    - **Deletar:** Remove uma área cadastrada da memória.
- **Cálculos Inteligentes e Automáticos:**
    - **Cana de Açúcar:**
        - Calcula automaticamente o número de ruas de plantio com base na largura da área e em um espaçamento padrão de 1.5m.
        - Calcula a necessidade de fertilizante (NPK) com base no comprimento e no número de ruas.
    - **Milho:**
        - Converte a área de m² para hectares.
        - Calcula a necessidade de herbicida com base em uma dose padrão por hectare.
- **Exportação de Dados:** Salva todos os dados cadastrados em um arquivo `dados_fazenda.csv`, pronto para ser consumido por outras ferramentas de análise.

### Scripts de Análise (`analise.R` e `clima.R` - R)

- **Análise Estatística (`analise.R`):**
    - Lê o arquivo `dados_fazenda.csv` gerado pelo Python.
    - Gera um relatório estatístico completo, incluindo:
        - Análise geral de todas as áreas (total, média, mediana, desvio padrão, mínimo, máximo).
        - Análise detalhada por tipo de cultura, usando a biblioteca `dplyr`.
- **API de Clima (`clima.R`):**
    - Conecta-se à API do OpenWeatherMap para buscar dados meteorológicos em tempo real.
    - Exibe um relatório com as condições atuais de tempo para uma localidade pré-definida (Piracicaba, BR).

## Tecnologias Utilizadas

- **Python 3:** Para a aplicação principal de manipulação de dados.
- **R:** Para a análise estatística e conexão com a API.
    - `dplyr`: Manipulação e sumarização de dados.
    - `httr`: Para realizar requisições web.
    - `jsonlite`: Para processar a resposta da API (JSON).
- **Git & GitHub:** Para controle de versão e gerenciamento do projeto.

## Como Executar

#### Pré-requisitos
- Ter o **Python** e o **R** instalados na máquina.
- Ter o **Git** instalado para controle de versão.

#### Configuração
1. Clone o repositório para sua máquina local:
   ```bash
   git clone [https://github.com/murilosalla-blip/fiap-ia-projeto-farmtech.git](https://github.com/murilosalla-blip/fiap-ia-projeto-farmtech.git)


#### Instale as bibliotecas necessárias para o R, executando os seguintes comandos no console do R:
install.packages("dplyr")
install.packages("httr")
install.packages("jsonlite")
install.packages("Hmisc")

#### Para o script clima.R, é necessário obter uma chave de API gratuita no site OpenWeatherMap e inseri-la no arquivo.

   