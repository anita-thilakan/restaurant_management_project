import secrets
import string
from .models import Coupons

def generate_coupon_code(length=10):
    code = ""
    characters = string.ascii_uppercase + string.digits  # A-Z and 0-9
    for i in range(length):
        code +=secrets.choice(characters)
    
    #check in db 
    if not Coupons.objects.filter(code = code).exists():


        return code

# print(generate_coupon_code())