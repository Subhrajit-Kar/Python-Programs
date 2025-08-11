# A basic unit converter which converts between "C (celsius)" , "F (fahrenheit)" and "K (kelvin)"


def c_to_f(c): return (c * (9/5)) + 32
def f_to_c(f): return (f - 32) / (9/5)
def c_to_k(c): return c + 273.15
def k_to_c(k): return k - 273.15
def f_to_k(f): return c_to_k(f_to_c(f))
def k_to_f(k): return c_to_f(k_to_c(k))

unit_of_conversion = {
    ("C","F"): c_to_f,
    ("F","C"): f_to_c,
    ("C","K"): c_to_k,
    ("K","C"): k_to_c,
    ("F","K"): f_to_k,
    ("K","F"): k_to_f
}

def convert(value, from_unit, to_unit):
    match (from_unit, to_unit):
        case (a,b) if a == b:
                return value
        case (a, b) if (a, b) in unit_of_conversion:
                return unit_of_conversion[a, b](value)
        case _:
            print("...Invalid Conversion Type...")
            return None



print("\t.....🌡️ Temperature Converter......")
while True:
    try:
        value = float(input("Enter the Value for conversion : "))
        from_unit = input(r"Convert From ( C \ F \ K ) : ").upper()
        to_unit = input(r" Convert To ( C \ F \ K ) : ").upper()
        result = convert(value, from_unit, to_unit)
        if result is not None:
            print (f"\t{value:.2f}°{from_unit} = {result:.2f}°{to_unit}")
        else:
             print("...Conversion Failed...")    
        
        wish = input("Do you wish for another conversion (Y/N) : ").strip().upper()
        if wish !="Y" :
            print("...Thanks For Using...")
            break
    except ValueError:
        print("...Please enter valid details...")