```python
tars = TarsZeroShotNER()

# this usually comes from mycroft.conf and is set by transformers service
# labels can be anything, no training needed (zero shot learning)
# the labels in this example are the default values if not set
tars.config = { "labels": ["Organization", "Vehicle", "Location", "City", "Country", "Person"]}

utts = ["The Humboldt University of Berlin is situated near the Spree in Berlin, Germany",
        "The president of Portugal is Marcelo Rebelo de Sousa"]

_, context = tars.transform(utts)

print(context)
# {'zeroshot_ner': {'City': [{'entity': 'City',
#                             'source_text': 'The Humboldt University of Berlin '
#                                            'is situated near the Spree in '
#                                            'Berlin, Germany',
#                             'span': (64, 70),
#                             'value': 'Berlin'}],
#                   'Country': [{'entity': 'Country',
#                                'source_text': 'The Humboldt University of '
#                                               'Berlin is situated near the '
#                                               'Spree in Berlin, Germany',
#                                'span': (72, 79),
#                                'value': 'Germany'}],
#                   'Location': [{'entity': 'Location',
#                                 'source_text': 'The Humboldt University of '
#                                                'Berlin is situated near the '
#                                                'Spree in Berlin, Germany',
#                                 'span': (55, 60),
#                                 'value': 'Spree'},
#                                {'entity': 'Location',
#                                 'source_text': 'The president of Portugal is '
#                                                'Marcelo Rebelo de Sousa',
#                                 'span': (17, 25),
#                                 'value': 'Portugal'}],
#                   'Organization': [{'entity': 'Organization',
#                                     'source_text': 'The Humboldt University of '
#                                                    'Berlin is situated near '
#                                                    'the Spree in Berlin, '
#                                                    'Germany',
#                                     'span': (4, 33),
#                                     'value': 'Humboldt University of Berlin'}],
#                   'Person': [{'entity': 'Person',
#                               'source_text': 'The president of Portugal is '
#                                              'Marcelo Rebelo de Sousa',
#                               'span': (29, 52),
#                               'value': 'Marcelo Rebelo de Sousa'}]}}

```