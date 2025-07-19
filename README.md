# Exploratory Data Analysis of Stroke Risk Factors

This project investigates clinical and demographic variables associated with stroke using exploratory data analysis (EDA) techniques. The analysis includes statistical summaries, correlation evaluation, outlier detection, and patient segmentation using clustering algorithms.

## Project Structure

- `analise_avc/` — Python package containing all analysis modules
- `main.py` — script that runs the full analysis pipeline
- `imagens/` — folder where plots and visualizations are saved
- `requirements.txt` — dependencies required to run the project
- `setup.py` — package metadata and installation settings
- `README.md` — documentation and usage instructions

## Technologies and Libraries

Language: Python 3.9+

Libraries used:
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- scipy

## Analysis Workflow

1. Data loading and initial statistics
2. Preprocessing: handling missing values, encoding categorical variables, creating derived features
3. Descriptive statistics grouped by stroke occurrence
4. Visualization of age, glucose level, and BMI distributions
5. Correlation matrix construction and heatmap generation
6. Outlier detection using Z-score for glucose and BMI
7. Clustering analysis with KMeans and Elbow Method
8. Focused exploration of young patients without comorbidities

## How to Run

1. Clone the repository:

1. Clone the repository: https://github.com/GabriGuerra/analise_avc.git
2. Install dependencies: pip install -r requirements.txt
3. Download the dataset manually from Kaggle:
- Visit: https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset
- Download the file `stroke-data.csv`
- Save it in the root directory of this project
4. Run the analysis:


## Data Source

This project uses the publicly available "Stroke Prediction Dataset" from Kaggle:

https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset

The dataset remains under the authors' original license. Usage here is educational and demonstrative only.

## Author

Gabriel Guerra Samorano Pires

## License

External datasets retain their original licensing and attribution.

# Análise Exploratória de Fatores Associados ao Risco de AVC

Este projeto realiza uma análise exploratória de dados clínicos e demográficos relacionados à ocorrência de Acidente Vascular Cerebral (AVC), utilizando técnicas de estatística, correlação, detecção de outliers e agrupamento de pacientes por perfis clínicos.

## Estrutura do Projeto

- `analise_avc/` — pacote Python com todos os módulos de análise
- `main.py` — script que executa a pipeline completa
- `imagens/` — pasta onde os gráficos e visualizações são salvos
- `requirements.txt` — dependências necessárias para execução
- `setup.py` — metadados e configuração do pacote
- `README.md` — documentação do projeto e instruções de uso

## Tecnologias e Bibliotecas

Linguagem: Python 3.9 ou superior

Bibliotecas utilizadas:
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- scipy

## Etapas da Análise

1. Carregamento de dados e estatísticas iniciais
2. Pré-processamento: tratamento de valores nulos, codificação de variáveis categóricas e criação de atributos derivados
3. Estatísticas descritivas agrupadas por ocorrência de AVC
4. Visualização das distribuições de idade, glicemia e IMC
5. Construção da matriz de correlação e geração de heatmap
6. Detecção de outliers usando Z-score para glicemia e IMC
7. Análise de agrupamento com KMeans e método do cotovelo (Elbow Method)
8. Investigação específica de pacientes jovens sem comorbidades

## Como Executar

1. Clone o repositório:

1. Clone o repositório: https://github.com/GabriGuerra/analise_avc.git
2. Instale as dependências: pip install -r requirements.txt
3. Faça o download manual do dataset:
- Acesse: https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset
- Baixe o arquivo `stroke-data.csv`
- Coloque-o na pasta raiz deste projeto
4. Execute a análise: python main.py


## Fonte dos Dados

Este projeto utiliza a base pública "Stroke Prediction Dataset" disponível no Kaggle:

https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset

Os dados permanecem sob a licença original dos autores. O uso neste projeto é exclusivamente educacional e demonstrativo. O arquivo CSV **não está incluído** neste repositório.

## Autor

Gabriel Guerra Samorano Pires  

## Licença

As bases de dados externas mantêm sua licença original e atribuições.