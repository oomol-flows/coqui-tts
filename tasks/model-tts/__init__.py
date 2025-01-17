import os
import torch

from TTS.api import TTS
from typing import Literal

def main(params: dict):
  model: str = params["model"]
  model_path: str = params["model_path"]
  device: Literal["cpu", "cuda"] = params["device"]

  os.environ["TTS_HOME"] = model_path
  os.environ["COQUI_TOS_AGREED"] = "1" # ignore EOF error (break by stdin)

  if device == "cuda" and not torch.cuda.is_available():
    print("CUDA is not available, using CPU instead.")
    device = "cpu"

  return { "model": TTS(model).to(device) }
