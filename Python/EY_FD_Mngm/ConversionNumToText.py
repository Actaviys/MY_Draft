

dictionary_conversion_numbers_to_text = {
    0: "нуль",
    1: "один",
    2: "два",
    3: "три",
    4: "чотири",
    5: "п'ять",
    6: "шість",
    7: "сім",
    8: "вісім",
    9: "дев'ять",
    10: "десять",
    11: "одинадцять",
    12: "дванадцять",
    13: "тринадцять",
    14: "чотирнадцять",
    15: "п'ятнадцять",
    16: "шістнадцять",
    17: "сімнадцять",
    18: "вісімнадцять",
    19: "дев'ятнадцять",
    20: "двадцять",
    21: "двадцять один",
    22: "двадцять два",
    23: "двадцять три",
    24: "двадцять чотири",
    25: "двадцять п'ять",
    26: "двадцять шість",
    27: "двадцять сім",
    28: "двадцять вісім",
    29: "двадцять дев'ять",
    30: "тридцять",
    31: "тридцять один",
    32: "тридцять два",
    33: "тридцять три",
    34: "тридцять чотири",
    35: "тридцять п'ять",
    36: "тридцять шість",
    37: "тридцять сім",
    38: "тридцять вісім",
    39: "тридцять дев'ять",
    40: "сорок",
    41: "сорок один",
    42: "сорок два",
    43: "сорок три",
    44: "сорок чотири",
    45: "сорок п'ять",
    46: "сорок шість",
    47: "сорок сім",
    48: "сорок вісім",
    49: "сорок дев'ять",
    50: "п'ятдесят",
    51: "п'ятдесят один",
    52: "п'ятдесят два",
    53: "п'ятдесят три",
    54: "п'ятдесят чотири",
    55: "п'ятдесят п'ять",
    56: "п'ятдесят шість",
    57: "п'ятдесят сім",
    58: "п'ятдесят вісім",
    59: "п'ятдесят дев'ять",
}

def convert_numbers_to_text(inp_nuber):
    for dtcv in dictionary_conversion_numbers_to_text:
        if inp_nuber == dtcv:
            return dictionary_conversion_numbers_to_text[dtcv]
            

# print(convert_numbers_to_text(55))

