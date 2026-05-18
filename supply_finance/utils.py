from .models import *

MODEL_MAP = {
    'feed_types': FeedTypes,
    'feed_suppliers': FeedSuppliers,
    'feed_purchases': FeedPurchases,
    'customers': Customers,
    'sales': Sales,
    'expense_categories': ExpenseCategories,
    'farm_expenses': FarmExpenses,
}

def get_model_by_name(name):
    return MODEL_MAP.get(name)