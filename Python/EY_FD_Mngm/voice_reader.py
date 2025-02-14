import json, pyaudio
from vosk import Model, KaldiRecognizer
import time
import threading

# model = Model("VoiseModels/vosk-model-uk-v3-lgraph")
model = Model("VoiseModels/vosk-model-small-uk-v3-small")
rec = KaldiRecognizer(model, 16000)
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate= 16000, input=True, frames_per_buffer=8000)
stream.start_stream()


def listen(): # Функція для прослуховування
    while True: 
        data = stream.read(450, exception_on_overflow=False)  
        if (rec.AcceptWaveform(data)) and (len(data) > 0): # 
            answer = json.loads(rec.Result())
            if answer["text"]:
                yield answer["text"]



def parse_input(user_input): #Функція для парсингу команд
    cmd, *args = user_input.split() #Розбиваю команду
    cmd = cmd.strip() #Записую команду в окрему змінну
    return cmd, *args #Повертаю команду і аргументи

def join_list_to_str(cmd_input_prs_list): # Функція для злиття списку в рядок
    res = ""
    for prscmd in cmd_input_prs_list:
        res += prscmd
        res += " "
    return res
  


import voice_synthes_ua as vss
import analysis_voise_command
import other_analysis_input_voise


def voise_model_analyze(): # Функція для аналізу голосу
    print("Привіт :)")
    for textMicro in listen():
        name_verification, *args_cmd_inp_list = parse_input(textMicro)
        
        if name_verification == "Флешка" or name_verification == "флешка": # Імпровізована власна назва `EY`
            
            comandStr = join_list_to_str(args_cmd_inp_list)
            
            cmdVc, *argsVc = parse_input(comandStr)
            match cmdVc:
                case "Привіт" | "привіт":
                    vss.text_converter_to_voice("Привіт. Як сьогодні твої справи?")
                    # print("Здорова, Як справи?")
                
                case "Відкрий" | "відкрий":
                    analysis_voise_command.funk_opening_cmd(argsVc) # 
                
                case "Скільки" | "скільки":
                    ht = analysis_voise_command.funk_exact_current_time()
                    print(ht)
                    vss.text_converter_to_voice(ht)
                
                
                
                
                
                case "Дякую" | "дякую":
                    vss.text_converter_to_voice("Будь ласка!. Звертайся..")
                
                case "Вихід" | "вихід":
                    vss.text_converter_to_voice("До зустрічі!")    
                    print("\n Пака ;) \n")
                    break
                
                
                case _: # Рівень 2
                    print("-", name_verification, args_cmd_inp_list) 
        
        else: # Рівень 1
            other_analysis_input_voise.analys_voise_text_to_commands(textMicro) 
            
                     


def keyboard_input_cmd(): # Функція для консольних команд
    while True:
        try:
            command, *qrg = parse_input(input())

            match command:
                case "time":
                    print("hh/mm/ss...")
                    print(qrg)
                
                
                case "q":
                    break
                
        
        except: pass





def main():
    threading.Thread(target=voise_model_analyze).start()
    # threading.Thread(target=keyboard_input_cmd).start()
    


if __name__ == "__main__":
    main()