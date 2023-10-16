from fastapi import APIRouter
from datetime import datetime

from transfer import CreateTransactionModel, CancelTransactionModel
from database.transferservice import create_transaction_db, get_all_user_tarnsfers_db, cancel_transfer_db

transfer_router = APIRouter(prefix='/transfers', tags=['rabota s platejami'])

#zapros na sozdaniya tranzaksii
@transfer_router.post('/create')
async def add_new_transaction(data: CreateTransactionModel):
    transfer_data = data.model_dump()

    resuld = create_transaction_db(**transfer_data)

    return {'status': 1, 'message': resuld}

#zapros na atmeneniya tranzaksi
@transfer_router.post('/cancel')
async def cancel_transfer(data: CancelTransactionModel):
    cancel_data = data.model_dump()

    result = cancel_transfer_db(**cancel_data)

    return {'status': 1, 'message': result}

#zapros na vivod vse tranzaksii ob opredelennoy karte
@transfer_router.get('/monitoring')
async def get_card_transaction(card_id: int):
    resuld = get_all_user_tarnsfers_db(card_from_id=card_id)

    return {'status': 1, 'message': resuld}