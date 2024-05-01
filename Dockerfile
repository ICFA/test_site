FROM python:3.12.3-slim

COPY . ./

RUN python -m pip install -r requires.txt

ENTRYPOINT [ "python", "manage.py" ]

CMD [ "runserver", "0.0.0.0:8001" ]
