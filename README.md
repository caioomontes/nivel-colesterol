# 💉 Previsão de Colesterol com Regressão Linear

Doenças cardiovasculares continuam sendo uma das principais causas de morte no mundo, frequentemente associadas a fatores como obesidade e altos níveis de colesterol. No entanto, a realização de exames laboratoriais frequentes em larga escala é limitada por custo e logística, o que dificulta o monitoramento precoce da saúde populacional.

Este projeto foi desenvolvido no contexto do **Módulo 1 do Bootcamp "Arquiteto(a) de Big Data"** e propõe uma solução baseada em ciência de dados: prever o nível de colesterol de pacientes com base em variáveis simples e amplamente disponíveis, como **peso corporal e gênero**.

### 🧠 Questão-Problema

> **É possível prever o colesterol de um paciente apenas com base no seu peso?**

A partir dessa pergunta, construímos um modelo de **regressão linear**, que identifica a relação entre peso e colesterol utilizando dados clínicos reais fornecidos por uma empresa da área da saúde.

Além de aplicar conceitos fundamentais de análise e tratamento de dados, visualização e aprendizado de máquina, este projeto tem um propósito claro: **antecipar riscos cardiovasculares e apoiar decisões clínicas com base em dados acessíveis**.

---

Estrutura do projeto
- 📊 Análise exploratória dos dados
- 🧹 Tratamento de dados ausentes (média e moda)
- 🔎 Visualizações gráficas da relação entre variáveis
- 📈 Modelo preditivo de regressão linear com avaliação de desempenho
- 📁 Organização modular para reuso e expansão futura

---

🔬 Tecnologias Utilizadas
- Python 3.9+
- pandas 1.5.2
- matplotlib 3.6.2
- seaborn 0.12.1
- scikit-learn 1.2.0

📊 Metodologia
- Variáveis numéricas: média arredondada para 2 casas decimais
- Variáveis categóricas: moda
- Análise exploratória com gráficos de dispersão
- Divisão por gênero para avaliar diferenças no padrão preditivo
- Regressão Linear com avaliação de métricas (R², MAE)

Resultados do Modelo
> - A cada 1 kg a mais no peso do paciente, espera-se um aumento de aproximadamente 1,26 unidades no nível de colesterol. 
> - Valor de colesterol estimado para um paciente com peso igual a 0 (interpretado apenas como base matemática da equação da reta). 
> - O modelo explica 97% da variação dos níveis de colesterol com base no peso. Um excelente nível de ajuste. 
> - Em média, o modelo erra cerca de 5 unidades na previsão dos valores reais de colesterol. 

🧾 Conclusão
O modelo de regressão linear construído mostrou-se altamente eficaz para prever os níveis de colesterol com base apenas no peso corporal dos pacientes. Com um R² de 0.97, é possível afirmar que existe uma forte correlação entre as duas variáveis, tornando viável o uso desse tipo de abordagem para triagens e ações preventivas na área da saúde.

Feito por Caio Montes — Cientista de Dados & Analista de Dados
