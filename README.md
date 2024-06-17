# Trainees 1 - Cirrosifier: Análise de Dados da Cirrose

## Sobre o Projeto

Este repositório contém todos os estudos e análises realizados durante a diretoria de Trainees 1 da rotação 2024.1 da @TAIL (Liga de Inteligência Artificial e Tecnologia), na UFPB. No projeto "Cirrosifier", analisamos os dados do dataset [Liver Cirrhosis Stage Classification](https://www.kaggle.com/datasets/aadarshvelu/liver-cirrhosis-stage-classification) com o objetivo de:

* Realizar Análise Exploratória de Dados (EDA) sobre a doença Cirrose Biliar Primaria (CBP);
* Desenvolver algoritmos de Machine Learning para prever o estágio e a situação da doença nos pacientes.

O projeto foi desenvolvido utilizando o ambiente Jupyter Notebook no VS Code, com Python e suas principais bibliotecas de análise de dados e machine learning: pandas, numpy, matplotlib, seaborn, scikit-learn e tensorflow.

Na próxima seção, detalharemos o conteúdo de cada pasta e arquivo do repositório para facilitar a navegação e o aprendizado.

## Pastas e Arquivos

### "data"

A pasta `data` contém todos os dados utilizados no projeto, organizados em subpastas:

* **"dados_brutos":** Armazena os dados brutos extraídos do dataset original, sem pré-processamento.
* **"dados_processados":** Contém os arquivos CSV processados e prontos para serem utilizados nos notebooks. Para mais detalhes sobre cada arquivo, consulte o notebook `pre_processamento.ipynb` na pasta `notebooks`.

### "notebooks"

A pasta `notebooks` concentra o desenvolvimento das análises e modelos de machine learning:

* **Pasta "models":** Armazena os modelos de machine learning desenvolvidos, separados em pastas específicas:
    * `modelos_estagio`: Modelos para prever o estágio da cirrose.
    * `modelos_morte`: Modelos para prever a mortalidade por cirrose.
* **Pasta "scalers":** Guarda os scalers utilizados nos modelos, com a mesma estrutura de pastas dos modelos:
    * `scalers_estagio`: Scalers para os modelos de previsão de estágio.
    * `scalers_morte`: Scalers para os modelos de previsão de mortalidade.
* **Notebook "classificacao_estagio.ipynb":** Desenvolvimento dos modelos de machine learning para prever o estágio da cirrose.
* **Notebook "classificacao_mortes.ipynb":** Desenvolvimento dos modelos de machine learning para prever a situação do paciente.
* **Notebook "eda_completo.ipynb":** Realização da Análise Exploratória de Dados (EDA), com insights sobre os dados e visualizações explicativas das features.
* **Notebook "pre_processamento.ipynb":** Limpeza do dataframe, tratamento de dados ausentes e duplicados, tradução de nomes de colunas e outras etapas de pré-processamento.

## Veja Mais

* **Artigo no Medium:** [Cirrosifier](https://medium.com/@joyribeirogxavier/fff3a577da2f) - Detalhes sobre o projeto, metodologia e resultados.
* **Site do Projeto:** [Aplicação no Streamlit](https://tail-cirrosifier.streamlit.app/) - Aplicação web com o modelo de previsão de estágio e mortalidade por cirrose.
* **Mais Sobre a TAIL:** [Site da TAIL](https://tail-tech.com/) - Outros projetos da nossa Liga Acadêmica.


### Agradecimentos

* Agradecemos à TAIL pela oportunidade de realizar este projeto e esperamos que tenham gostado do projeto. Se você leu até aqui, muito obrigado, e bons estudos!

