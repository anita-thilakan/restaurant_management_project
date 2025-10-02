<<<<<<< HEAD
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
=======
import secrets
import string

from .models import Coupons
def generate_coupon_code(len=10):
    code = ""
    characters = string.ascii_uppercase + string.digits
    for i in range(len):
        code += secrets.choice(characters)
    
    # check code in db before alloting
    if not Coupons.objects.filter(code=code).exists():
        return code
>>>>>>> bac5e779490cd9da5091f129f83c3043fd071cc9
