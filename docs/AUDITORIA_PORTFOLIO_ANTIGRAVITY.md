# Auditoria de Portfólio Técnico - Comex Tech MVP

Este documento apresenta uma análise detalhada do projeto **comex-tech-mvp** sob a perspectiva de portfólio técnico para um estudante de Comércio Exterior que busca demonstrar competência em tecnologia aplicada ao setor.

---

## 1. Estrutura do Projeto

A estrutura física atual do projeto é organizada da seguinte forma:

```text
comex-tech-mvp/
├── .env.example
├── .gitignore
├── app.py
├── requirements.txt
├── README.md
├── data/
│   ├── mock/
│   │   └── processos_mock.csv
│   ├── private/
│   ├── raw/
│   └── temp/
├── docs/
│   ├── ESCOPO_ACADEMICO.md
│   └── AUDITORIA_PORTFOLIO_ANTIGRAVITY.md (este documento)
├── src/  [Vazio]
└── tests/ [Vazio]
```

### Análise de Componentes:
- **`app.py`**: Ponto de entrada do aplicativo. Contém toda a lógica de leitura do CSV via Pandas, cálculo do CIF estimado, formatação de moedas e renderização da interface Streamlit.
- **`data/mock/processos_mock.csv`**: Base de dados em formato CSV contendo 10 registros de importações fictícias com destino ao Porto de Santos.
- **`docs/ESCOPO_ACADEMICO.md`**: Excelente declaração de limitações ("Disclaimer"), blindando o projeto contra interpretações de que seria um sistema de produção ou oficial.
- **`requirements.txt`**: Define as dependências (`streamlit` e `pandas`).
- **`src/` e `tests/`**: Pastas estruturais criadas, porém atualmente vazias (sem código-fonte modularizado ou testes automatizados).

---

## 2. O que o Projeto Faz Hoje

O aplicativo é um **dashboard interativo local** construído em Streamlit que:
1. **Carrega e Processa Dados Fictícios**: Lê uma tabela de processos de importação marítima (`data/mock/processos_mock.csv`), convertendo campos de data e calculando dinamicamente o valor CIF (FOB + Frete + Seguro) para cada processo.
2. **Filtra Dados em Tempo Real**: Permite ao usuário filtrar os processos por **Status Acadêmico**, **País de Origem** e **Risco Acadêmico** por meio de um menu lateral (sidebar).
3. **Exibe Métricas Consolidadas**: Apresenta quatro cartões de métricas dinâmicas: número de processos filtrados, total de contêineres, CIF total estimado (USD) e custo de armazenagem estimado (BRL).
4. **Visualiza Gráficos de Apoio**: Exibe dois gráficos de barra simples gerados a partir do agrupamento dos dados (processos por status e por risco).
5. **Apresenta uma Tabela Exploratória**: Mostra uma visão detalhada dos processos filtrados, ocultando índices desnecessários e formatando os campos de datas e valores de maneira amigável.

---

## 3. Classificação do Projeto

O projeto é classificado como um **Protótipo de Simulação Acadêmica** (ou **Protótipo Funcional Didático**).

* **Por que não é um MVP Validável?** Um MVP (Minimum Viable Product) precisa resolver um problema real de um usuário real e permitir a validação de hipóteses de negócio. O projeto atual opera sobre dados 100% estáticos de um CSV e não possui canal de gravação de novos dados ou integração com fluxos de trabalho reais.
* **Por que não é uma POC?** Uma Prova de Conceito (Proof of Concept) visa validar a viabilidade técnica de uma tecnologia específica (ex: testar se é possível consumir a API do Siscomex). Este projeto usa tecnologias maduras e bem estabelecidas para uma interface padrão de visualização de dados.
* **Classificação Adequada**: É um excelente protótipo para apresentações de sala de aula e demonstração de ideias visuais para acompanhamento de fluxos aduaneiros/logísticos.

---

## 4. Avaliação como Portfólio Técnico

**Nota de Potencial: Alta | Nota de Maturidade Atual: Média-Baixa**

### Pontos Fortes:
- **Alinhamento de Domínio**: Mostra que o estudante entende conceitos de Comex (ETA, Incoterms, Porto de Santos, CIF, FOB, frete, seguro, desembaraço, parametrização/risco).
- **Stack Tecnológica Correta**: A escolha de Python, Pandas e Streamlit é perfeita para profissionais de negócios que querem demonstrar capacidades analíticas e de prototipagem rápida.
- **Transparência**: O arquivo `docs/ESCOPO_ACADEMICO.md` e o aviso de aviso importante no topo do dashboard demonstram maturidade e responsabilidade profissional.

### Pontos de Melhoria para Portfólio:
- **Simplicidade do Código**: Um recrutador técnico que abrir o `app.py` verá que toda a lógica está misturada com o código visual em um único arquivo de menos de 200 linhas. Isso não demonstra boas práticas de engenharia de software (como modularização e separação de conceitos).
- **Falta de Testes**: As pastas `tests/` vazias indicam que a confiabilidade do código não foi validada de forma automatizada.
- **Ausência de Interatividade de Dados**: O usuário só pode visualizar dados que já estão no CSV. Adicionar a possibilidade de inserir novos processos fictícios via tela elevaria o nível técnico do projeto.

---

## 5. O que Falta para Ficar Apresentável no GitHub (Portfólio de Destaque)

Para que um recrutador ou gestor da área de Comex/Tech olhe o repositório e se impressione:

1. **Modularização do Código**:
   - Mover a lógica de carga de dados, cálculos financeiros e formatação para arquivos dentro de `src/` (ex: `src/data_loader.py` e `src/formatters.py`).
   - Importar essas funções no `app.py`, deixando o arquivo principal focado exclusivamente na renderização dos componentes visuais do Streamlit.
2. **Implementação de Testes Unitários**:
   - Criar testes na pasta `tests/` usando `pytest` para validar o cálculo do CIF e as funções de formatação de moedas. Isso mostra capricho técnico e preocupação com qualidade.
3. **Documentação Atraente**:
   - Melhorar o `README.md` adicionando **capturas de tela (screenshots) ou um GIF animado** do dashboard em funcionamento.
   - Escrever uma seção explicando o "Problema de Negócio Simulado" e a "Decisão de Arquitetura".
4. **Hospedar o App**:
   - Fazer deploy gratuito do protótipo no **Streamlit Community Cloud** e colocar o link direto no topo do repositório do GitHub. Um portfólio que pode ser testado com um clique é muito mais visitado.
5. **CI/CD Básico**:
   - Configurar um arquivo de workflow do GitHub Actions (`.github/workflows/tests.yml`) para rodar os testes automaticamente a cada push. Isso demonstra conhecimento de práticas de DevOps.

---

## 6. O que Falta para Virar um MVP Validável (Fase de Validação de Negócio)

Se o objetivo for transformar este protótipo em uma ferramenta que um profissional de Comex real possa testar e validar na prática:

1. **Persistência de Dados**:
   - Substituir o arquivo CSV por um banco de dados leve (ex: SQLite local) ou um serviço gratuito de nuvem (ex: Supabase, PostgreSQL) para salvar os dados criados.
2. **Interface de Entrada de Dados (CRUD)**:
   - Criar uma aba ou formulário no Streamlit para permitir a inclusão, edição e exclusão de processos de importação diretamente pela interface visual, sem precisar editar arquivos CSV.
3. **Importação de Planilhas Reais**:
   - Permitir que o usuário faça upload de um arquivo Excel contendo seus próprios processos para que o dashboard seja gerado dinamicamente com os dados do usuário.
4. **Controle de Acesso Simples**:
   - Um sistema básico de login (autenticação) para separar os processos por usuário ou empresa importadora fictícia.
5. **Cálculos Fiscais Parametrizáveis**:
   - Permitir a configuração de alíquotas estimadas de impostos de importação (II, IPI, PIS, COFINS, ICMS) por produto, aproximando o dashboard do cálculo do custo de nacionalização real.

---

## 7. Riscos Técnicos

1. **Inexistência de Tratamento de Erros na Carga do CSV**:
   - Se o arquivo `processos_mock.csv` estiver corrompido, faltar alguma coluna ou possuir valores nulos em campos de cálculo, o aplicativo irá falhar (crash) com um erro técnico do Pandas exposto na tela do usuário.
2. **Concorrência e Estado no Streamlit**:
   - O Streamlit executa o script do início ao fim a cada clique. Se o app evoluir para escrita de arquivos de forma local concorrente, múltiplos usuários gravando no mesmo arquivo CSV causarão perda e corrupção de dados.
3. **Dependência de Tipagem Dinâmica e Mudanças de Schema**:
   - O uso de referências diretas a strings como `dados["valor_fob_usd_estimado"]` torna o código vulnerável. Se houver uma alteração de grafia no cabeçalho do CSV, múltiplos pontos do código quebrarão silenciosamente até a execução.
4. **Consumo de Memória**:
   - O Pandas carrega todo o dataset na memória RAM. Para 10 linhas isso é insignificante, mas se a base crescer para dezenas de milhares de processos históricos, a performance do aplicativo cairá severamente sem paginação.

---

## 8. Riscos de Comex e Limitação de Escopo

1. **Simplificação Excessiva do Cálculo do CIF**:
   - No comércio exterior brasileiro, o valor aduaneiro (base de cálculo dos tributos) baseia-se no Incoterm e inclui despesas de carga/descarga e capatazia (THC) no porto de destino até a chegada. A fórmula puramente aritmética `FOB + Frete + Seguro` é uma aproximação acadêmica e não serve para fins fiscais reais.
2. **Representação Incompleta de Parametrização**:
   - O app usa o termo "Risco Acadêmico" (Baixo, Médio, Alto). Na Receita Federal do Brasil, os canais de parametrização (Verde, Amarelo, Vermelho, Cinza) representam a análise fiscal real. Um recrutador sênior de Comex pode achar a terminologia infantil se não for explicada a sua equivalência didática.
3. **Redundância de Incoterms no Mock**:
   - Na linha do processo `IMP-ACAD-0002` o Incoterm está marcado como `CIF`, mas há colunas separadas para `frete_usd_estimado` e `seguro_usd_estimado`. Tecnicamente, se a venda é CIF, o valor do frete e seguro já compõem o preço de venda FOB/mercadoria declarado pelo exportador. O app soma novamente estes valores para calcular o CIF estimado, gerando uma dupla contagem teórica de frete/seguro.
4. **Prazos Logísticos Estáticos**:
   - A previsão de desembaraço e a data de ETA são estáticas. Na vida real, a imprevisibilidade de atracação no Porto de Santos (greves, maré, congestionamento de berço) exige cálculos dinâmicos de *Demurrage* de contêineres e janelas de devolução, que não são abordados no modelo atual.

---

## 9. 5 Melhorias Pequenas, Práticas e Seguras
*(Sem alteração imediata de código, prontas para aprovação)*

1. **Modularização de Funções Auxiliares**:
   - Criar `src/utils.py` e mover as funções `formatar_moeda_usd` e `formatar_moeda_brl` para lá, importando-as no `app.py`.
2. **Criação de Testes de Formatação e CIF**:
   - Escrever um arquivo `tests/test_calculations.py` que valide se a soma do CIF e a formatação brasileira de moedas estrangeiras funcionam perfeitamente.
3. **Melhoria Visual nas Métricas e Tabela**:
   - Utilizar emojis/ícones e cores customizadas nos cartões de métricas do Streamlit. Exibir o status de Risco Acadêmico na tabela com formatação condicional simples (ex: células vermelhas para risco alto).
4. **Glossário Acadêmico em Sidebar**:
   - Inserir um expander no menu lateral contendo um mini-glossário com os termos técnicos utilizados (FOB, CIF, ETA, Contêiner, Desembaraço) para demonstrar domínio teórico diretamente na interface.
5. **Exportação de Dados Filtrados**:
   - Adicionar um botão (`st.download_button`) no final da tabela para permitir que o usuário baixe a visualização filtrada atual em formato CSV, simulando uma exportação de relatório operacional didático.

---

### Diagnóstico Concluído
O projeto possui bases sólidas para fins didáticos e com poucas horas de refatoração técnico-estrutural e refinamento visual pode se tornar um portfólio de destaque no GitHub para a interseção de Comex e Tecnologia.

**Recomendação**: Iniciar a aplicação do primeiro bloco de melhorias práticas (modularização, testes e refinamento do README) após aprovação do plano de trabalho.
