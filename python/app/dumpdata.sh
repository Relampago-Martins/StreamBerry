#!/bin/bash

python manage.py dumpdata streamberry.Streaming --indent 4 > fixtures/Streaming.json
python manage.py dumpdata streamberry.Avaliacao --indent 4 > fixtures/Avaliacao.json
python manage.py dumpdata streamberry.Filme --indent 4 > fixtures/Filme.json