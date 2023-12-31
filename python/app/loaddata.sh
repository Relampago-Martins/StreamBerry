#!/bin/bash

python manage.py loaddata fixtures/Avaliacao.json --app streamberry.Avaliacao
python manage.py loaddata fixtures/Streaming.json --app streamberry.Streaming
python manage.py loaddata fixtures/Filme.json --app streamberry.Filme