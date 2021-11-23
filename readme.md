```python
tars = TarsZeroShotNER()

utts = ["The Humboldt University of Berlin is situated near the Spree in Berlin, Germany",
        "The president of Portugal is Marcelo Rebelo de Sousa"]

_, context = tars.transform(utts)

# context is a dict of "zeroshot_ner": [prediction(utt) for utt in utterances]
print(context)
# {'zeroshot_ner': [[{'entity': 'Organization',
#                     'source_text': 'The Humboldt University of Berlin is '
#                                    'situated near the Spree in Berlin, Germany',
#                     'span': (4, 33),
#                     'value': 'Humboldt University of Berlin'},
#                    {'entity': 'Location',
#                     'source_text': 'The Humboldt University of Berlin is '
#                                    'situated near the Spree in Berlin, Germany',
#                     'span': (55, 60),
#                     'value': 'Spree'},
#                    {'entity': 'City',
#                     'source_text': 'The Humboldt University of Berlin is '
#                                    'situated near the Spree in Berlin, Germany',
#                     'span': (64, 70),
#                     'value': 'Berlin'},
#                    {'entity': 'Country',
#                     'source_text': 'The Humboldt University of Berlin is '
#                                    'situated near the Spree in Berlin, Germany',
#                     'span': (72, 79),
#                     'value': 'Germany'}],
#                   [{'entity': 'Location',
#                     'source_text': 'The president of Portugal is Marcelo '
#                                    'Rebelo de Sousa',
#                     'span': (17, 25),
#                     'value': 'Portugal'},
#                    {'entity': 'Person',
#                     'source_text': 'The president of Portugal is Marcelo '
#                                    'Rebelo de Sousa',
#                     'span': (29, 52),
#                     'value': 'Marcelo Rebelo de Sousa'}]]}

```