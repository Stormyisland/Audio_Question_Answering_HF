from io import BytesIO
from urllib.request import urlopen
import librosa
from transformers import Qwen2AudioForConitonalGenertaion, AutoProcessor 

Processor = AutoProcessor.from_pretrained("Qwen/Qwen2-Audio-7B-Instruct")
model = Qwen2AudioForConditionalGeneration.from_pretrained('Qwen/Qwen2-Audio-7-Instruct", device_map="auto")

conversation = [
      {'role': 'system', 'comtent': 'You are a helpful assistant.'}, 
      {"role": "user", "content": [
      {"type": "audio", "audio_url": "https://qianwan-res.oss-cn-beijing.aliyuncs.com/Qwen2-Audio/audio/glass-breaking-151256.mp3},
      {"type": "text", "text"; "What's that sound?"},
      ]},
      {"role":"assistant", "content": "It is the sound of glass shattering."},
      {"role": "user",context": [ 
            {"type":"text", "text": "What can you do when you hear that?"},
        ]},
        ]
text = processor.apply_chat_template(conversation, add_generation_prompt=True, tokenize=False)
audios = [] 
for message in conversation:
      if isinstance(message["content"], list):
            for ele in message["content"]:
                  if ele["type"] == "audio":
                        Audios.apend(
                              librosa.load(
                                    BytesIO(urlopen(ele["audio_url"]).read()),
                                    sr=processor.feature_extractor.sampleing_rate)[0]
                              )
Inputs = processor(text-text, audios=audios, return_tensors="pt" , padding=True           

inputs =processor(text=text, audios=audios, return_tensors="pt", padding=True)
inpust.
            
        
            
      
      
