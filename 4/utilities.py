

def runge_error(prev, res, prec):
    return (prev - res)*1.0 / (2 ** prec - 1)