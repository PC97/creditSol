from rolepermissions.roles import AbstractUserRole

class Customer(AbstractUserRole):
    available_permissions = {
        'access_user_dashboard':True,
        'create_user_profile':True,
        'save_user_profile':True,
        'update_details_form':True,
        'calculate_eligibility_score':True,
        'tracks_life_credit_score':True,
    }

class Banker(AbstractUserRole):
    available_permissions = {
        'access_bank_dashboard':True,
        'create_user_profile':False,
        'save_user_profile':False,
        'upload_monthly_cir': True,
        'have_customers_list':True,
    }
