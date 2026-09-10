from io import BytesIO
from urllib.request import urlopen
import librosa
from transformers import Qwen2AudioForConitonalGenertaion, AutoProcessor 

Processor = AutoProcessor.from_pretrained("Qwen/Qwen2-Audio-7B-Instruct")
model = Qwen2AudioForConditionalGeneration.from_pretrained('Qwen/Qwen2-Audio-7-Instruct", device_map="auto")

conversation = [
      {'role': 'system', 'comtent': 'You are a helpful assistant.'}, 
      
