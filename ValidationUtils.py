import validators
import phonenumbers
from datetime import datetime

def validate_email(email):
       return  validators.email(email)
def validate_gender(gender):
    return gender.lower() in ["male", "female"]

def getTime():
    return datetime.now()
def validate_phone_number(phone_number, country_code):
    try:
        parsed_number = phonenumbers.parse(phone_number, country_code)
        if phonenumbers.is_valid_number(parsed_number):
            return True
        else:
            return False
    except phonenumbers.NumberParseException:
        return False



# בדיקת אימות