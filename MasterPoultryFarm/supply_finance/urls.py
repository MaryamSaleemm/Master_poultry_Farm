from django.urls import include, path
from .views import *
from rest_framework.routers import DefaultRouter
from .api_views import SalesViewSet, ExpensesViewSet

# --- ROUTER ---
router = DefaultRouter()
router.register(r'sales', SalesViewSet)
router.register(r'expenses', ExpensesViewSet)
urlpatterns = [
    # ==========================================
    # 1. FEED MANAGEMENT
    # ==========================================
    path('feed/types/', UniversalListView.as_view(), {'model_name': 'feed_types'}, name='finance_feed_types_list'),
    path('feed/types/add/', UniversalCreateView.as_view(), {'model_name': 'feed_types'}, name='finance_feed_types_create'),
    path('feed/types/<int:pk>/edit/', UniversalUpdateView.as_view(), {'model_name': 'feed_types'}, name='finance_feed_types_update'),
    path('feed/types/<int:pk>/delete/', UniversalDeleteView.as_view(), {'model_name': 'feed_types'}, name='finance_feed_types_delete'),

    path('feed/suppliers/', UniversalListView.as_view(), {'model_name': 'feed_suppliers'}, name='finance_feed_suppliers_list'),
    path('feed/suppliers/add/', UniversalCreateView.as_view(), {'model_name': 'feed_suppliers'}, name='finance_feed_suppliers_create'),
    path('feed/suppliers/<int:pk>/edit/', UniversalUpdateView.as_view(), {'model_name': 'feed_suppliers'}, name='finance_feed_suppliers_update'),
    path('feed/suppliers/<int:pk>/delete/', UniversalDeleteView.as_view(), {'model_name': 'feed_suppliers'}, name='finance_feed_suppliers_delete'),

    path('feed/purchases/', UniversalListView.as_view(), {'model_name': 'feed_purchases'}, name='finance_feed_purchases_list'),
    path('feed/purchases/add/', UniversalCreateView.as_view(), {'model_name': 'feed_purchases'}, name='finance_feed_purchases_create'),
    path('feed/purchases/<int:pk>/edit/', UniversalUpdateView.as_view(), {'model_name': 'feed_purchases'}, name='finance_feed_purchases_update'),
    path('feed/purchases/<int:pk>/delete/', UniversalDeleteView.as_view(), {'model_name': 'feed_purchases'}, name='finance_feed_purchases_delete'),

    # ==========================================
    # 2. CUSTOMERS & SALES
    # ==========================================
    path('sales/customers/', UniversalListView.as_view(), {'model_name': 'customers'}, name='finance_customers_list'),
    path('sales/customers/add/', UniversalCreateView.as_view(), {'model_name': 'customers'}, name='finance_customers_create'),
    path('sales/customers/<int:pk>/edit/', UniversalUpdateView.as_view(), {'model_name': 'customers'}, name='finance_customers_update'),
    path('sales/customers/<int:pk>/delete/', UniversalDeleteView.as_view(), {'model_name': 'customers'}, name='finance_customers_delete'),

    path('sales/records/', UniversalListView.as_view(), {'model_name': 'sales'}, name='finance_sales_list'),
    path('sales/records/add/', UniversalCreateView.as_view(), {'model_name': 'sales'}, name='finance_sales_create'),
    path('sales/records/<int:pk>/edit/', UniversalUpdateView.as_view(), {'model_name': 'sales'}, name='finance_sales_update'),
    path('sales/records/<int:pk>/delete/', UniversalDeleteView.as_view(), {'model_name': 'sales'}, name='finance_sales_delete'),

    # ==========================================
    # 3. EXPENSES
    # ==========================================
    path('expenses/categories/', UniversalListView.as_view(), {'model_name': 'expense_categories'}, name='finance_expense_categories_list'),
    path('expenses/categories/add/', UniversalCreateView.as_view(), {'model_name': 'expense_categories'}, name='finance_expense_categories_create'),
    path('expenses/categories/<int:pk>/edit/', UniversalUpdateView.as_view(), {'model_name': 'expense_categories'}, name='finance_expense_categories_update'),
    path('expenses/categories/<int:pk>/delete/', UniversalDeleteView.as_view(), {'model_name': 'expense_categories'}, name='finance_expense_categories_delete'),

    path('expenses/records/', UniversalListView.as_view(), {'model_name': 'farm_expenses'}, name='finance_farm_expenses_list'),
    path('expenses/records/add/', UniversalCreateView.as_view(), {'model_name': 'farm_expenses'}, name='finance_farm_expenses_create'),
    path('expenses/records/<int:pk>/edit/', UniversalUpdateView.as_view(), {'model_name': 'farm_expenses'}, name='finance_farm_expenses_update'),
    path('expenses/records/<int:pk>/delete/', UniversalDeleteView.as_view(), {'model_name': 'farm_expenses'}, name='finance_farm_expenses_delete'),

    # Fallback
    path('manage/<str:model_name>/', UniversalListView.as_view(), name='finance_universal_list'),
    path('api/', include(router.urls)),
]