import subprocess
# subprocess.call(['./Startup_VR.sh']) # ['./calc_Bush.sh']  /home/a1/Desktop/EY_FlashDrive/calc_Bush.sh
subprocess.Popen(['./FilesPRG/calc_Bush.sh']) # calc_Bush



# import open_voise_command

# def parse_input_level_0(user_input): #Функція для парсингу команд
#     cmd, *args = user_input.split() #Розбиваю команду
#     cmd = cmd.strip().lower() #Записую команду в окрему змінну
#     return cmd, *args #Повертаю команду і аргументи

# def join_list_to_str(cmd_input_prs_list): # Функція для злиття списку в рядок
#     res = ""
#     for prscmd in cmd_input_prs_list:
#         res += prscmd
#         res += " "
#     return res
    



# def voise_model_analyze(): # Функція для аналізу голосу
#     print("Привіт :)")
#     while True:
#         name_verification, *args_cmd_inp_list = parse_input_level_0(input("Send command => ")) # Розбиваю на змінні після парсингу
        
#         if name_verification == "ф" or name_verification == "a": # Імпровізована власна назва `EY`
            
#             comandStr = join_list_to_str(args_cmd_inp_list)
#             try:
#                 cmdVc, *argsVc = parse_input_level_0(comandStr)
#                 match cmdVc:
#                     case "привіт":
#                         # vss.text_converter_to_voice("Здарова")
#                         print("Здорова, Як справи?")
                    
#                     case "відкрий":
#                         open_voise_command.funk_analysis_cmd_opening(argsVc) # 
#                         # subprocess.Popen(['./calc_Bush.sh'])
                    
                    
                    
                    
#                     case "вихід":
#                         print("\n Пака :) \n")
#                         break
                    
                    
#                     case _: print("EY_FD-> ", cmdVc, argsVc) # Рівень 3
                         
#             except: print("."*6) # Рівень 2
        
#         else: print("-", name_verification, args_cmd_inp_list) # Рівень 1
                          
        
# voise_model_analyze()
# #








# ################################################################
# import json, pyaudio
# from vosk import Model, KaldiRecognizer
# import time


# # model = Model("VoiseModels/vosk-model-uk-v3-lgraph")
# model = Model("VoiseModels/vosk-model-small-uk-v3-small")
# rec = KaldiRecognizer(model, 16000)
# p = pyaudio.PyAudio()
# stream = p.open(format=pyaudio.paInt16, channels=1, rate= 16000, input=True, frames_per_buffer=8000)
# stream.start_stream()


# def listen(): # Функція для прослуховування
#     while True:
#         data = stream.read(310, exception_on_overflow=False) 
#         # data = stream.read(4000, exception_on_overflow=False) 
#         if (rec.AcceptWaveform(data)) and (len(data) > 0): # 
#             answer = json.loads(rec.Result())
#             if answer["text"]:
#                 yield answer["text"]



# import voice_synthes_ua as vss

# def parse_input(user_input): #Функція для парсингу команд
#     cmd, *args = user_input.split() #Розбиваю команду
#     cmd = cmd.strip().lower() #Записую команду в окрему змінну
#     return cmd, *args #Повертаю команду і аргументи

# def voise_model_analyze(): # Функція для аналізу голосу
#     print("Привіт :)")
    
#     for text in listen():
#         comandVc, *argsVc = parse_input(text) # Розбиваю на змінні після парсингу
#         match comandVc:
#             case "привіт":
#                 vss.text_converter_to_voice("Привіт Діма. Як справи?")
#                 print(comandVc, argsVc)
#                 print("Здорова \nЯк справи?")
                
            
            
#             case "вихід":
#                 print("\n Пака :) \n")
#                 time.sleep(2)
#                 quit()
#             case _:
#                 print(f"->> {comandVc}--{argsVc}")
                          
#         print("--->>>")
        
# voise_model_analyze()