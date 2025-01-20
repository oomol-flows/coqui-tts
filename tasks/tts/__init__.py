import os

from oocana import Context
from TTS.api import TTS
from typing import cast

def main(params: dict, context: Context):
  text: str = params["text"]
  tts: TTS = params["model"]
  speaker_path: str = params["speaker"]
  language: str | None = params["language"]
  output_path: str | None = params["output_path"]

  if output_path is None:
    output_path = os.path.join(
      context.session_dir, 
      f"{context.job_id}.wav",
    )
  tts.tts_to_file(
    text=text, 
    speaker_wav=speaker_path, 
    language=cast(str, language), 
    file_path=output_path,
  )
  return { "output_path": output_path }
