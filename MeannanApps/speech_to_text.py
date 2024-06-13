from transformers import Wav2Vec2Processor, Wav2Vec2ForCTC
import torch


class SpeechToText:
    def __init__(self):
        self.processor = Wav2Vec2Processor.from_pretrained(
            "facebook/wav2vec2-base-960h")
        self.model = Wav2Vec2ForCTC.from_pretrained(
            "facebook/wav2vec2-base-960h")

    def transcribe(self, audio):
        input_values = self.processor(
            audio, return_tensors="pt", sampling_rate=16000).input_values
        with torch.no_grad():
            logits = self.model(input_values).logits
        predicted_ids = torch.argmax(logits, dim=-1)
        transcription = self.processor.batch_decode(predicted_ids)[0]
        return transcription


speech_to_text = SpeechToText()
