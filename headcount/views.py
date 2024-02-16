from django.shortcuts import render
from django.http import JsonResponse
from .models import Headcount
from datetime import datetime, timedelta

def line_chart_headcount(request):
    # Obtem os parâmetros da requisição
    init_date = request.GET.get('init_date')
    end_date = request.GET.get('end_date')

    # Consulta o banco de dados para recuperar os dados relevantes
    headcount_data = Headcount.objects.filter(dt_reference_month__range=[init_date, end_date])

    # Calcula o headcount para cada mês
    headcount_by_month = {}
    for data_point in headcount_data:
        reference_month = data_point.dt_reference_month.strftime('%b %Y')
        if reference_month not in headcount_by_month:
            headcount_by_month[reference_month] = 0
        headcount_by_month[reference_month] += 1  # Incrementa o headcount para o mês

    # Organiza os dados no formato JSON conforme especificado na resposta esperada
    xAxis_categories = list(headcount_by_month.keys())
    series_data = [{'name': 'Headcount', 'data': list(headcount_by_month.values())}]

    response_data = {
        'xAxis': {'type': 'category', 'data': xAxis_categories},
        'yAxis': {'type': 'value'},
        'series': {'type': 'line', 'series': series_data},
        'title': 'Headcount por Mês',
        'grid': 6,
        'color': ['#D4DDE2']
    }

    return JsonResponse(response_data)

def category_chart_headcount(request):
    # Obtem os parâmetros da requisição
    init_date = request.GET.get('init_date')
    end_date = request.GET.get('end_date')
    category = request.GET.get('category')

    # Converte as datas de string para objetos de data
    end_date_obj = datetime.strptime(end_date, '%Y-%m-%d')

    # Calcula o último mês selecionado
    last_month_end_date = end_date_obj - timedelta(days=end_date_obj.day)
    last_month_start_date = last_month_end_date.replace(day=1)

    # Consulta o banco de dados para recuperar os dados relevantes
    headcount_data = Headcount.objects.filter(
        dt_reference_month__range=[last_month_start_date, last_month_end_date]
    )

    # Calcula a contagem de ativos no último mês selecionado onde fg_status é igual a 1
    active_count = headcount_data.filter(fg_status=1).count()

    # Organiza os dados no formato JSON conforme especificado na resposta esperada
    response_data = {
        "xAxis": {"type": "value", "show": True, "max": {}},
        "yAxis": {"type": "category", "data": [category]},  # Utiliza a categoria fornecida na requisição
        "series": {
            "type": "horizontal_stacked",
            "series": [
                {"name": "Colaboradores", "data": [active_count], "type": "bar"}
            ]
        },
        "title": "Empresa",
        "grid": 6,
        "color": ["#2896DC"],
        "is%": False
    }

    return JsonResponse(response_data)
