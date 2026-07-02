# 🚢 Comex Tech MVP - Dashboard de Controle de Importação Marítima

Este é um protótipo de dashboard de dados analíticos para acompanhamento e controle simulado de processos de importação marítima com destino ao Porto de Santos/SP. O projeto une conceitos teóricos de **Comércio Exterior** com **Engenharia de Software** e **Visualização de Dados**.

---

## ⚠️ AVISO DE ESCOPO EXCLUSIVAMENTE ACADÊMICO
> [!IMPORTANT]
> **Este projeto é um protótipo didático local.**
> - **Sem Integrações Reais**: Não possui qualquer conexão com sistemas oficiais (Siscomex, Receita Federal, MDIC, Portal Único Siscomex, armadores ou terminais portuários).
> - **Dados Fictícios**: Todos os processos, empresas importadoras, navios, valores financeiros e observações contidos na base de dados são 100% inventados para fins de simulação.
> - **Cálculos Didáticos**: As estimativas financeiras (incluindo cálculo de CIF e armazenagem) são aproximações matemáticas simples para demonstração e não representam fórmulas tributárias ou aduaneiras oficiais brasileiras.
> - **Finalidade**: Destinado exclusivamente a portfólio acadêmico e demonstração de competências técnicas em Python e análise de dados de comércio exterior.

---

## 🎯 Objetivo
Demonstrar a viabilidade de um painel de monitoramento integrado para processos aduaneiros e logísticos. O dashboard consolida métricas financeiras e operacionais estimadas, facilitando a tomada de decisão acadêmica sobre prioridades de desembaraço e riscos operacionais simulados.

---

## 💻 O que o Aplicativo Faz
- **Consolidação de Métricas**: Calcula em tempo real o total de processos filtrados, volume total de contêineres, valor CIF estimado (somando FOB + Frete + Seguro) e estimativa de custos de armazenagem (BRL).
- **Filtros Operacionais Dinâmicos**: Permite filtrar a base por Status Acadêmico do processo, País de Origem da mercadoria e Nível de Risco atribuído didaticamente.
- **Gráficos Analíticos**: Apresenta distribuições de processos por status e por risco.
- **Tabela Exploratória Detalhada**: Lista os processos fictícios ordenados por data prevista de chegada (ETA Santos), com formatação brasileira para datas e moedas estrangeiras.

---

## 🛠️ Tecnologias Utilizadas
- **Python 3.12+**: Linguagem base do projeto.
- **Streamlit**: Framework de interface rica para prototipagem rápida e dashboards interativos.
- **Pandas**: Biblioteca para manipulação, limpeza e análise estruturada de dados.
- **Unittest**: Biblioteca padrão do Python para desenvolvimento de testes automatizados.

---

## 🖼️ Demonstração Visual

> Placeholder: inserir futuramente print ou GIF do dashboard rodando localmente.

---

## 🚀 Como Rodar o Projeto Localmente (Windows)

No terminal do Windows (PowerShell ou Prompt de Comando), siga os passos abaixo:

1. **Clone o repositório ou navegue até a pasta do projeto**:
   ```powershell
   cd comex-tech-mvp
   ```

2. **Crie e ative o ambiente virtual (venv)**:
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. **Atualize o gerenciador de pacotes (pip) e instale as dependências**:
   ```powershell
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Execute o dashboard**:
   ```powershell
   streamlit run app.py
   ```

5. **Acesse no seu navegador**:
   O aplicativo estará disponível no endereço local informado no terminal, normalmente [http://localhost:8501](http://localhost:8501).

---

## 🧪 Como Rodar os Testes Automatizados
O projeto conta com testes unitários para validar a lógica de formatação e os cálculos estruturais. Para executá-los dentro do ambiente virtual ativado:
```powershell
.venv\Scripts\python -m unittest discover tests
```

---

## 📂 Estrutura do Projeto

```text
comex-tech-mvp/
├── app.py                # Arquivo principal do Streamlit (UI)
├── requirements.txt      # Dependências necessárias (Streamlit e Pandas)
├── README.md             # Documentação principal
├── .env.example          # Modelo de variáveis de ambiente
├── .gitignore            # Arquivos ignorados pelo Git
├── data/
│   └── mock/
│       └── processos_mock.csv  # Base de dados em formato tabular
├── docs/
│   ├── ESCOPO_ACADEMICO.md     # Detalhes das premissas e escopo
│   └── AUDITORIA_PORTFOLIO_ANTIGRAVITY.md
├── src/                  # Código-fonte modularizado
│   ├── __init__.py
│   ├── calculations.py   # Lógica matemática e processamento de dataframes
│   └── utils.py          # Funções utilitárias de formatação
└── tests/                # Testes unitários do sistema
    ├── __init__.py
    ├── test_calculations.py
    └── test_utils.py
```

---

## 📊 Estrutura do Dataset (processos_mock.csv)
A base de dados simula informações reais coletadas em fluxos de importação:
- `processo_id`: Identificador único do processo de importação.
- `importador_ficticio` / `fornecedor_ficticio`: Nomes de empresas simuladas.
- `pais_origem` / `porto_origem`: Rota de origem da mercadoria.
- `navio_ficticio`: Nome do navio de transporte marítimo.
- `eta_santos`: Data prevista de chegada do navio no Porto de Santos.
- `data_prevista_desembaraco`: Previsão didática de liberação aduaneira da carga.
- `status_academico`: Situação do fluxo (Ex: *Em trânsito*, *Triagem documental*, etc.).
- `risco_academico`: Nível de risco de conformidade didático (Baixo, Médio, Alto).
- `quantidade_containers`: Total de contêineres do processo.
- `valor_fob_usd_estimado` / `frete_usd_estimado` / `seguro_usd_estimado`: Valores que compõem o CIF.
- `armazenagem_brl_estimada`: Custo de armazenamento simulado no terminal.
- `observacoes_academicas`: Notas didáticas sobre o andamento do processo.

---

## 🛑 Limitações do Protótipo
1. **Dados Estáticos**: Não há gravação ou atualização dinâmica da base de dados (salva em arquivo CSV estático).
2. **Cálculos Simplificados**: Não há cálculo real de impostos (II, IPI, PIS, COFINS, ICMS) ou tarifas portuárias oficiais, tabelas vigentes ou cobranças reais de operadores/terminais.
3. **Ausência de Backend**: Sem persistência em banco de dados relacional ou controle de acesso de usuários (login).

---

## 🗺️ Roadmap de Evolução (Próximos Passos)
- [x] **Modularização**: Separação de funções utilitárias e de cálculos em pacotes independentes (Fase 1).
- [x] **Testes Unitários**: Testagem das fórmulas e formatações com `unittest` (Fase 1).
- [ ] **Persistência de Dados**: Migração do CSV para um banco relacional como o SQLite.
- [ ] **Formulário de Entrada**: Criação de formulário interativo no Streamlit para inclusão e edição de novos processos no dashboard.
- [ ] **Exportação de Relatórios**: Botão para download direto das consultas filtradas em Excel ou CSV.
