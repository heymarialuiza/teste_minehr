
# Teste técnico para Backend - 2024

Como uma startup de people analytics nosso produto é voltado para expor os dados em forma de informações valiosas para nossos clientes. Fazemos isso atrávez de cards e gráficos com um storytelling focado na resolução dos problemas.




## Problema

Seu papel será implementar endpoints para dois dos problemas que resolvemos dentro da nossa plataforma

## Headcount:

Headcount, em uma empresa, refere-se ao número total de funcionários em um determinado período de tempo. Representa a contagem total de pessoas empregadas pela organização, independentemente de serem trabalhadores em tempo integral, parcial, temporário ou contratados por projeto. O headcount é uma métrica essencial para o dimensionamento da força de trabalho e é frequentemente utilizado por líderes e departamentos de recursos humanos para entender a dimensão da equipe.


### Endpoints propostos para Headcount

### Retorna o gráfico de linhas

### Cálculo:    
    contagem de ativos no período
    contagem de id_matricula onde fg_status = 1 dentro do periodo init_date e end_date
### url:    
```http
  GET /headcount/line_chart/
```
### Parâmetros
| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `init_date` | `string` | **Obrigatório**. Campo do formato yyyy-MM-dd |
| `end_date` | `string` | **Obrigatório**. Campo do formato yyyy-MM-dd |
### Resposta esperada
```http
  {
    "xAxis": {
        "type": "category",
        "data": [
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "Maio",
            "Jun",
            "Jul",
            "Aug",
            "Set",
            "Oct",
            "Nov",
            "Dec"
        ]
    },
    "yAxis": {
        "type": "value"
    },
    "series": {
        "type": "stacked_line",
        "series": [
            {
                "name": "2021",
                "type": "line",
                "data": [
                    3.4,
                    4.8,
                    5.6,
                    4.9,
                    6.7,
                    5,
                    5.8,
                    5.8,
                    5.4,
                    5.7,
                    6,
                    7.1
                ]
            },
            {
                "name": "2022",
                "type": "line",
                "data": [
                    21.2,
                    8.6,
                    8.2
                ]
            }
        ]
    },
    "title": "Headcount por Ano",
    "grid": 6,
    "color": [
        "#D4DDE2",
        "#A3B6C2"
    ]
}
```
Os itens que serão sobrescritos serão:
- response['xAxis']['data']
- response['series']['series']
   
Os demais itens devem ficar iguais

### Retorna o gráfico categórico

### Cálculo:    
    contagem de ativos no último mês selecionado
    contagem de id_matricula onde fg_status = 1 dentro do mês passado por end_date
### url:    
```http
  GET /headcount/category_charts/
```
### Parâmetros

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `init_date` | `string` | **Obrigatório**. Campo do formato yyyy-MM-dd |
| `end_date` | `string` | **Obrigatório**. Campo do formato yyyy-MM-dd |
| `category` | `string` | **Obrigatório**. Qualquer campos de category da base |
### Resposta esperada
```http
{
    "xAxis": {
        "type": "value",
        "show": true,
        "max": {}
    },
    "yAxis": {
        "type": "category",
        "data": [
            "Empresa 4",
            "Empresa 3",
            "Empresa 1",
            "Empresa 2"
        ]
    },
    "series": {
        "type": "horizontal_stacked",
        "series": [
            {
                "name": "Colaboradores",
                "data": [
                    97,
                    92.9,
                    91.3,
                    89.8
                ],
                "type": "bar"
            }
        ]
    },
    "title": "Empresa",
    "grid": 6,
    "color": [
        "#2896DC"
    ],
    "is%": false
}
```
Os itens que serão sobrescritos serão:
- response['YAxis']['data']
- response['series']['series']
Os demais itens devem ficar iguais   


## Turnover:

Turnover, por outro lado, é uma métrica que expressa a taxa de rotatividade de funcionários em uma empresa durante um determinado período. Também é conhecido como taxa de attrition ou rotatividade de pessoal. O turnover é calculado dividindo o número de funcionários que deixaram a empresa durante um período específico pelo número médio total de funcionários durante o mesmo período, multiplicado por 100 para obter a porcentagem.

### Endpoints propostos para Turnvoer

### Retorna o gráfico de linhas

### Cálculo
    soma de demitidos no perído / média de ativos do período
    (soma de fg_demitido_no_mes) / ((contagem de id_matricula onde fg_status = 1) / (quantidade de meses do período selecionado))    
    período é a quantidade de meses entre init_date e end_date
### url
```http
  GET /turnover/line_chart/
```
### Parâmetros
| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `init_date` | `string` | **Obrigatório**. Campo do formato yyyy-MM-dd |
| `end_date` | `string` | **Obrigatório**. Campo do formato yyyy-MM-dd |

### Resposta esperada
```http
  {
    "xAxis": {
        "type": "category",
        "data": [
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "Maio",
            "Jun",
            "Jul",
            "Aug",
            "Set",
            "Oct",
            "Nov",
            "Dec"
        ]
    },
    "yAxis": {
        "type": "value"
    },
    "series": {
        "type": "stacked_line",
        "series": [
            {
                "name": "2021",
                "type": "line",
                "data": [
                    3.4,
                    4.8,
                    5.6,
                    4.9,
                    6.7,
                    5,
                    5.8,
                    5.8,
                    5.4,
                    5.7,
                    6,
                    7.1
                ]
            },
            {
                "name": "2022",
                "type": "line",
                "data": [
                    21.2,
                    8.6,
                    8.2
                ]
            }
        ]
    },
    "title": "Taxa de Turnover por Ano (%)",
    "grid": 6,
    "color": [
        "#D4DDE2",
        "#A3B6C2"
    ]
}
```
Os itens que serão sobrescritos serão:
- response['xAxis']['data']
- response['series']['series']    

Os demais itens devem ficar iguais   

### Retorna o gráfico categórico

```http
  GET /turnover/category_charts/
```

### Parâmetros
| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `init_date` | `string` | **Obrigatório**. Campo do formato yyyy-MM-dd |
| `end_date` | `string` | **Obrigatório**. Campo do formato yyyy-MM-dd |
| `category` | `string` | **Obrigatório**. Qualquer campos de category da base |

### Resposta esperada
```http
{
    "xAxis": {
        "type": "value",
        "show": true,
        "max": {}
    },
    "yAxis": {
        "type": "category",
        "data": [
            "Empresa 4",
            "Empresa 3",
            "Empresa 1",
            "Empresa 2"
        ]
    },
    "series": {
        "type": "horizontal_stacked",
        "series": [
            {
                "name": "Colaboradores",
                "data": [
                    97,
                    92.9,
                    91.3,
                    89.8
                ],
                "type": "bar"
            }
        ]
    },
    "title": "Empresa",
    "grid": 6,
    "color": [
        "#2896DC"
    ],
    "is%": false
}
```
Os itens que serão sobrescritos serão:
- response['YAxis']['data']
- response['series']['series']
Os demais itens devem ficar iguais   

## Instalação

Instale o projeto com:

```bash
  cd setup
  pip install -r requirements.txt
```
## Rodando o projeto

Instale o projeto com:

```bash
  python manage.py migrate    
  python manage.py populate
  python manage.py runserver    
```
 
## Entregáveis:

- Compartilhe o repositório com os usuários felipeKosloski e lucasrbzrra no github
- Collections do postman para recriarmos as chamadas

## Sinta-se a vontade para sugerir melhorias ou tirar dúvidas

- https://www.linkedin.com/in/felipekosloski/
- https://www.linkedin.com/in/lucas-ribeiro-4179011b6/
