from random import sample

def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    if (
        min < 1 or 
        max > 1000 or 
        min > max or
        quantity < 0 or
        quantity > (max - min + 1)
    ):
        return []
    
    return sorted(sample(range(min, max + 1), quantity))

if __name__ == '__main__':
    print(get_numbers_ticket(15, 21, 0))   # []
    print(get_numbers_ticket(15, 20, 6))   # [15, 16, 17, 18, 19, 20]
    print(get_numbers_ticket(20, 15, 5))   # []
    print(get_numbers_ticket(15, 20, -5))  # []
