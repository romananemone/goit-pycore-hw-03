import re

COUNTRY_CODE_PREFIX = "38"

def normalize_phone(phone_number: str) -> str:
    if not isinstance(phone_number, str):
        raise ValueError("Phone number must be a string")
    
    clear_number = re.sub(r"\D", "", phone_number)
    
    if clear_number.startswith(COUNTRY_CODE_PREFIX):
        return f"+{clear_number}"

    return f"+{COUNTRY_CODE_PREFIX}{clear_number}"

if __name__ == "__main__":
    raw_numbers = [
        "067\t123 4567",
        "(095) 234-5678\n",
        "+380 44 123 4567",
        "380501234567",
        "    +38(050)123-32-34",
        "     0503451234",
        "(050)8889900",
        "38050-111-22-22",
        "38050 111 22 11   ",
    ]

    sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
    print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
    print("equal", sanitized_numbers == ['+380671234567', '+380952345678', '+380441234567', '+380501234567', '+380501233234', '+380503451234', '+380508889900', '+380501112222', '+380501112211'])