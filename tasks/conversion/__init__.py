import os

from oocana import Context
from TTS.api import TTS

def main(params: dict, context: Context):
  tts: TTS = params["model"]
  source_path: str = params["source_speaker"]
  target_path: str = params["target_speaker"]
  output_path: str | None = params["output_path"]

  if output_path is None:
    output_path = os.path.join(
      context.session_dir,
      f"{context.job_id}.wav",
    )

  tts.voice_conversion_to_file(
    source_wav=source_path,
    target_wav=target_path,
    file_path=output_path,
  )
  return { "output_path": output_path }