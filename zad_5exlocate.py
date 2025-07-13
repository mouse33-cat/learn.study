import zad_5exlocate_import

def ask_for_float_value(message):
    input_value = input(message)
    return float(input_value)

początkowa_wartość = ask_for_float_value("Podaj początkową wartość lokaty. : ")
percentage = ask_for_float_value("Podaj oprocentowanie lokaty. : ")
years = ask_for_float_value("Ile lat trwa lokata? : ")
final_value = zad_5exlocate_import.locate(percentage, years, początkowa_wartość)
print(f"Twoja lokata po tylu : {years} latach przyniesie zysk {final_value} ")