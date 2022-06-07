from math import erf, sqrt

def normal_cdf(x: float, mu: float = 0, sigma: float = 1) -> float:
    return (1 + erf((x - mu) / sqrt(2) / sigma)) / 2

def inverse_normal_cdf(p: float, mu: float = 0, sigma: float = 1, tolerance: float = 0.00001) -> float:
    if mu != 0 or sigma != 1:
        return mu + sigma * inverse_normal_cdf(p, tolerance=tolerance)

    low_z = -10
    hi_z = 10
    mid_z = (hi_z + low_z) / 2

    while hi_z - low_z > tolerance:
        mid_z = (hi_z + low_z) / 2
        mid_p = normal_cdf(mid_z)
        if mid_p < p:
            low_z = mid_z
        else:
            hi_z = mid_z

    return mid_z

p = float(input('Enter p: '))
res = inverse_normal_cdf(p=p)
print(res)
