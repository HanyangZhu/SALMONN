import whisper

whisper_path = 'C:/Users/38644/PycharmProjects'  # Replace with your actual path

model = whisper.load_model("large-v2", download_root=whisper_path)