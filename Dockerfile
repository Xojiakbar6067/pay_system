#ukazivaem yazik programirovaniya
FROM python:3.10

#
WORKDIR /pay_system

#kopirovat vse papki/fayli b doker
COPY . /pay_system

#ustanovka neobhodimoh komponentov
RUN pip install -r requirements.txt

#komanda dlya zapuska
CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=8080"]