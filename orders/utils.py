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
