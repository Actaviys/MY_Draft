import torch
import sounddevice as sd
import time

language = "ua"
model_id = "v4_ua"

speaker = "mykyta" # random
sample_rate = 48000
put_accent = True

device = torch.device("cpu")

texts = "Мир тобі, -ласкаво сказав ангел, сідаючи поруч з котом на товсту гілку і струшуючи з неї сніг. Привіт, -кіт розплющив зелені очі, ліниво оглянув ангела і відвернувся."

model, _ = torch.hub.load(repo_or_dir="snakers4/silero-models",
                          model="silero_tts",
                          language=language,
                          speaker=model_id
                          )
model.to(device)


def text_converter_to_voice(texts):
    # print(texts)
    audio = model.apply_tts(text=texts,
                            speaker=speaker,
                            sample_rate=sample_rate,
                            put_accent=put_accent
                            )
    
    
    sd.play(audio, sample_rate)
    time.sleep(len(audio) / sample_rate)
    sd.stop()

# import ConversionNumToText
# tr = ConversionNumToText.convert_numbers_to_text(15)
# text_converter_to_voice(tr)
# text_converter_to_voice("Привіт. Як справи?")

