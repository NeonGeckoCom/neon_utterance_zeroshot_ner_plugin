# # NEON AI (TM) SOFTWARE, Software Development Kit & Application Development System
# # All trademark and other rights reserved by their respective owners
# # Copyright 2008-2021 Neongecko.com Inc.
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
# 3. Neither the name of the copyright holder nor the names of its
#    contributors may be used to endorse or promote products derived from this
#    software without specific prior written permission.
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
# THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR
# CONTRIBUTORS  BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA,
# OR PROFITS;  OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE,  EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
from flair.data import Sentence
from flair.models import TARSTagger

from neon_transformers import UtteranceTransformer


class TarsZeroShotNER(UtteranceTransformer):
    def __init__(self, name="TarsZeroShotNER", priority=99):
        super().__init__(name, priority)
        # Load pre-trained TARS model for English
        self.tars = TARSTagger.load('tars-ner')
        self.labels = self.config.get("labels") or ["Organization", "Vehicle",
                                                    "Location", "City", "Country",
                                                    "Person"]
        self.tars.add_and_switch_to_new_task('zeroshot ner', self.labels, label_type='ner')

    def transform(self, utterances, context=None):
        preds = []
        for utt in utterances:
            sentence = Sentence(utt)
            self.tars.predict(sentence)

            preds.append([{"entity": span.labels[0].value,
                           "value": span.text,
                           "source_text": utt,
                           "span": (span.start_pos, span.end_pos)}
                          for span in sentence.get_spans()])

        # return unchanged utterances + data
        return utterances, {"zeroshot_ner": preds}


