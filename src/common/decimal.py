from decimal import Decimal, getcontext

getcontext().prec = 10

def D(val) -> Decimal:
    return Decimal(str(val))
