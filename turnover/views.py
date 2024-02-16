from django.shortcuts import render
from django.db.models import Sum
from django.http import JsonResponse
from .models import Turnover
from .models import Headcount
from datetime import datetime

def line_chart_turnover(request):
    # Obtem os parâmetros da requisição
    init_date = request.GET.get('init_date')
    end_date = request.GET.get('end_date')

    # Consulta o banco de dados para recuperar os dados relevantes
    turnover_data = Turnover.objects.filter(dt_reference_month__range=[init_date, end_date])

    # Calcula a soma de demitidos no período
    total_demitidos = turnover_data.aggregate(total_demitidos=Sum('fg_demitido_no_mes'))['total_demitidos']

    # Calcula a média de ativos durante o período
    total_ativos = Headcount.objects.filter(dt_reference_month__range=[init_date, end_date], fg_status=1).count()
    quantidade_meses = (datetime.strptime(end_date, '%Y-%m-%d') - datetime.strptime(init_date, '%Y-%m-%d')).days / 30
    media_ativos = total_ativos / quantidade_meses if quantidade_meses > 0 else 0

    # Calcula o turnover
    turnover = (total_demitidos / media_ativos) * 100

    # Organiza os dados no formato JSON para o gráfico de linhas
    response_data = {
        "xAxis": {"type": "category", "data": [ "Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]},
        "yAxis": {"type": "value"},
        "series": {
            "type": "stacked_line",
            "series": [
                {"name": "Turnover (%)", "type": "line", "data": [turnover] * 12} 
            ]
        },
        "title": "Taxa de Turnover por Ano (%)",
        "grid": 6,
        "color": ["#D4DDE2", "#A3B6C2"]
    }

    return JsonResponse(response_data)

def category_chart_turnover(request):
    # Obtenha os parâmetros da requisição
    init_date = request.GET.get('init_date')
    end_date = request.GET.get('end_date')
    category = request.GET.get('category')

    # Consulte o banco de dados para recuperar os dados relevantes
    turnover_data = Turnover.objects.filter(dt_reference_month__range=[init_date, end_date], ds_category=category)

    # Calcula a contagem de demitidos para cada categoria
    demitidos_por_categoria = turnover_data.aggregate(total_demitidos=Sum('fg_demitido_no_mes'))['total_demitidos'] or 0

    # Organiza os dados no formato JSON para o gráfico categórico
    response_data = {
        "xAxis": {"type": "value", "show": True, "max": {}},
        "yAxis": {"type": "category", "data": [category]},
        "series": {
            "type": "horizontal_stacked",
            "series": [
                {"name": "Demitidos", "data": [demitidos_por_categoria], "type": "bar"}
            ]
        },
        "title": "Categoria",
        "grid": 6,
        "color": ["#2896DC"],
        "is%": False
    }

    return JsonResponse(response_data)
