from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
   path('', views.index, name='index'),                                            #вывод главной страницы
    path('market/products/', views.products, name='products'),                        #вывод списка всей продукции
    path('market/product/<int:id_product>', views.product, name='product'),           #вывод выбранного пользователем проодукта по id по форме (cтр 17)
    path('market/order/<int:id_order>', views.order, name='order'),                   # вывод заказа по Id (формы ввода id пока нет)
    path('market/clients/', views.clients, name='clients'),                           # вывод всех клиентов
    path('market/orders/', views.orders, name='orders'),                              # вывод всех заказов
    path('market/client_orders/<int:id_client>', views.client_orders, name='client_orders'),      # все заказы по клиенту (формы выбора клиента пока нет)
    path('market/client_products_sorted/<int:id_client>/<int:days>/', views.client_products_sorted, name='client_products_sorted'), # вывыод всех товаров по клиенту за послегие кол дней (форма ввода id клиента и кол дней - стр 16)
    path('market/product_form/<int:id_product>', views.product_form, name='product_form'),        #форма дляизменения выбранного по id продукта (форма для выбора Id продукта  - стр 15)
    path('market/choice_product_id_form/', views.choice_product_by_id, name='choice_product_id_form'),    # #форма для выбора id продукта
    path('market/choice_products_by_client_by_days/', views.choice_products_by_client_by_days, name='choice_products_by_client_by_days'),  # форма для ввода id клиента и кол дней
    path('market/choice_product/', views.choice_product, name='choice_product'),        
]