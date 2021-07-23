from math import pi, sqrt
def basel(error):
    basel_pi = 0
    x = 0
    term = 0
    while ( pi - sqrt(basel_pi)) > error:
        x += 1
        basel_pi += 6*(1/(x**2))
        term += 1
    basel_pi = sqrt(basel_pi)
    return basel_pi, term

def taylor(error):
    taylor_pi = 0
    x = 0
    term = 0
    while abs(pi - taylor_pi) > error:
        x += 1
        if x % 2 != 0:
            taylor_pi += (1/(2*x-1))*4
            term += 1
        else:
            taylor_pi -= (1/(2*x-1))*4
            term += 1
    return taylor_pi, term

def wallis(error):
    wallis_pi_half = 1
    x = 0
    term = 0
    while abs(pi - wallis_pi_half*2) > error:
        x += 1
        wallis_pi_half *= ((2*x)**2)/((2*x-1)*(2*x+1))
        term += 1
    wallis_pi = wallis_pi_half * 2
    return wallis_pi, term
error = float(input("Enter the error: "))
print(wallis(error))

def spigot(error):
    half_spigot_pi = 1
    x = 0
    term = 0
    while abs(pi - 2*half_spigot_pi) > error:
        x += 1
        half_spigot_pi *= 
        
