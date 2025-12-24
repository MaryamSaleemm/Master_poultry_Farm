from .models import *

MODEL_MAP = {
    # Feed Management
    'feed_types': FeedTypes,
    'feed_suppliers': FeedSuppliers,
    'feed_purchases': FeedPurchases,
    
    # Sales & Customers
    'customers': Customers,
    'sales': Sales,

    # Expenses
    'expense_categories': ExpenseCategories,
    'farm_expenses': FarmExpenses,
}

def get_model_by_name(name):
    return MODEL_MAP.get(name)