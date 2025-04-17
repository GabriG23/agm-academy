import utils


def main():

    base = 10
    altezza = 20
    gradi = 45
    text = 'Ciao Mondo'
    strings = ['ape', 'cane', 'elefante', 'bue', 'gatto', 'lucertola', 'bue']
    numbers = [-1, 2, 6, 3, 1231, 199, 21, -12312]
    numbers_string = ["22", "23", "99", "-1", "-24"]
    num = 23128
    word = '888'

    print(f"L'area del quadrato di lato {base} è {utils.square_area(base)}\n")
    print(f"Conversione da {gradi} gradi Celcius in {utils.conversion_C_F(gradi)} gradi Fahrenheit\n")
    print(f"L'area del rettangolo di base {base} e altezza {altezza} è {utils.rect_area(base, altezza)}\n")
    print(f"Stringa in ordine invertito: {utils.reverse_order(text)}\n")

    print(f"Lista originale di stringhe: {strings}")
    print(f"Lista di stringhe con lunghezza maggiore di 5: {utils.remove_len_5(strings)}\n") 

    print(f"Lista di numeri: {numbers}")
    print(f"Lista ordinata: {sorted(numbers)}")
    print(f"Il numero più grande è : {utils.max_number(numbers)}\n")

    print(f"La prola più grande è: {utils.longest_string(strings)}\n")

    print(f"Numero convertito in stringa: {utils.string_conversion(num)}")
    print(f"Stringa convertita in numer: {utils.int_conversion(word)}\n")

    print(f"Numeri stringa: {numbers_string}")
    print(f"Lista di numeri interi: {utils.numbers_converter(numbers_string)}\n")

    print(f"Lista di numeri interi: {numbers}")
    print(f"Lista di stringhe di numeri interi: {utils.strings_converter(numbers)}\n")

    print(f"Numero: {num}")
    print(f"Lista dei numeri interi presenti nel numero: {utils.number_splitter(num)}\n")


if __name__ == '__main__':
    main()