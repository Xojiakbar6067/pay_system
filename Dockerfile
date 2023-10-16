#ukazivaem yazik programirovaniya
FROM python:3.8

#
WORKDIR /pay_system

#kopirovat vse papki/fayli b doker
COPY . /pay-systeam

#ustanovka neobhodimoh komponentov
RUN pip install -r requirements.txt

#komanda dlya zapuska
CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=8080"]