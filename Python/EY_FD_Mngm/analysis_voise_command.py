import webbrowser as wb
import subprocess as sbp
from datetime import datetime, timedelta


def funk_opening_cmd(inp_text:list):
    for aText in inp_text:
        print(aText)
        
        match aText:
            case "відео":
                wb.open("https://www.youtube.com/")
            case "музику":
                wb.open("https://www.youtube.com/watch?v=Ia6ZBd4ehmU&list=PL6yK8n0u0pOcGgnm-8kYnD3UNmFAr2ZQT&pp=iAQB8AUB")
            case "калькулятор":
                sbp.Popen(['./FilesPRG/calc_Bush.sh'])
                



import ConversionNumToText
def funk_exact_current_time():
    res = ""
    curr_time = str(datetime.now().time())[:5:]
    strip_time = str(curr_time).split(":")
    
    for stt in strip_time:
        concT = ConversionNumToText.convert_numbers_to_text(int(stt))
        res += concT
        res += " ; "
    
    return res

# print(funk_exact_current_time())