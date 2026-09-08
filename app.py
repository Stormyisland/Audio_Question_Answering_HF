from io import BytesIO
from urllib.request import urlopen
import librosa
from transformers import Qwen2AudioForConitonalGenertaion, AutoProcessor 

Processor = AutoProcessor.from_pretrained("Qwen/Qwen2-Audio-7B-Instruct")
