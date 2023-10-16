from fastapi import FastAPI
#dlya html
from starlette.templating import Jinja2Templates

from card.card_api import card_router

from user.user_api import user_router
from transfer.transfer_api import transfer_router
from currensy.currensy_api import currensy_router

#sozdat bazu dannix
from database import Base, engine
Base.metadata.create_all(bind=engine)

app = FastAPI(docs_url='/')

##esli xotim vivodit html stranichku
template = Jinja2Templates(directory='templates')
from html_example.html_show import html_router
app.include_router(html_router)

app.include_router(user_router)
app.include_router(card_router)
app.include_router(transfer_router)
app.include_router(currensy_router)