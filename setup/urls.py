"""setup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from headcount import views as headcount_views
from turnover import views as turnover_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('headcount/line_chart/', headcount_views.line_chart_headcount, name='headcount_line_chart'),
    path('headcount/category_charts/', headcount_views.category_chart_headcount, name='headcount_category_charts'),
    path('turnover/line_chart/', turnover_views.line_chart_turnover, name='line_chart_turnover'),
    path('turnover/category_charts/', turnover_views.category_chart_turnover, name='category_chart_turnover'),
]

