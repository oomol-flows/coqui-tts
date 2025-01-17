import os
import torch

from TTS.api import TTS
from oocana import Context

def main(params: dict, context: Context):
  speaker: str = params["speaker"]
  target: str = params["target"]
  cache_dir: str = params["cache_dir"]

  os.environ["TTS_HOME"] = cache_dir
  os.environ["COQUI_TOS_AGREED"] = "1"

  device = "cuda" if torch.cuda.is_available() else "cpu"
  tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)
  # wav = tts.tts(
  #   text="大家好，我是渣渣辉。欢迎大家一起来玩贪玩蓝月！", 
  #   speaker_wav=speaker, 
  #   language="zh",
  # )
  # wav.pop()
  tts.tts_to_file(
    text="大家好，我是渣渣辉。欢迎大家一起来玩贪玩蓝月！", 
    speaker_wav=speaker, 
    language="zh", 
    file_path=target,
  )
