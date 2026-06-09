# MVP Academico de Controle de Importacao Maritima

Protótipo acadêmico em Streamlit para simular, com dados 100% fictícios, o acompanhamento de processos de importação marítima com destino ao Porto de Santos.

## Aviso Importante

Este projeto é exclusivamente acadêmico e demonstrativo.

- Não possui integração com Siscomex, Receita Federal, MDIC, Portal Único, armadores, terminais portuários ou qualquer sistema real.
- Não utiliza credenciais, tokens, certificados digitais ou dados sensíveis.
- Não define NCM, alíquota, LI, LPCO, tratamento administrativo ou regra oficial.
- Não deve ser usado para decisão operacional, fiscal, aduaneira, financeira ou jurídica.
- Todos os dados de processos, empresas, valores, prazos e observações são fictícios.

## Tema do MVP

Controle fictício de importação marítima via Porto de Santos, com foco em:

- visão geral dos processos mockados;
- filtros por status, país de origem e risco acadêmico;
- indicadores simples de valores estimados e contêineres;
- tabela exploratória para apoio a apresentação acadêmica.

## Estrutura

```text
.
├── app.py
├── data/
│   └── mock/
│       └── processos_mock.csv
├── docs/
│   └── ESCOPO_ACADEMICO.md
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Como Rodar no Windows

No PowerShell, dentro da pasta do projeto:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
streamlit run app.py
```

Depois, acesse o endereço local exibido pelo Streamlit, normalmente:

```text
http://localhost:8501
```

## Configuracao

O arquivo `.env.example` existe apenas como referência acadêmica. O MVP atual não exige variáveis de ambiente.

## Proximo Patch Recomendado

Adicionar testes simples para validação do dataset mockado e criar uma camada de funções em `src/` para separar leitura, filtros e cálculo de indicadores da interface Streamlit.
