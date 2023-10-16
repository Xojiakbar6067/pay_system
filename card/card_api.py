from fastapi import APIRouter
from datetime import datetime

from card import CardAddModel, EditDicaginCard
from database.cardservice import add_card_db, delete_exact_card_db, edit_card_design_db, get_exact_user_cards_db, get_exact_cards_db, check_card_info_db

card_router = APIRouter(prefix='/card', tags=['rabota s kartami'])

#zapros na dobavit kartu
@card_router.post('/add')
async def add_new_card(data: CardAddModel):
    #perevodim paydentik na obichniy slovar
    card_data = data.dict()

    #proverka karti na nalichii v baze
    checker = check_card_info_db(data.card_number)

    #esli est karta v babze
    if checker:
        return {'status': 1, 'message': 'karta s takim nomerom est v baze'}
    else:
        result = add_card_db(**card_data)

        return {'status': 1, 'message': result}

#zapros na udalit kartu
@card_router.delete('/delete')
async def delete_exact_card(card_id):
    resuld = delete_exact_card_db(card_id=card_id)

    return {'status': 1, 'message': resuld}

#zapros na izmeneniya dizayna karti
@card_router.put('/edit-card-design')
async def edit_card_design(data:EditDicaginCard):
    card_data = data.model_dump()

    checker = check_card_info_db(data.card_id)

    if checker:
        return {'status': 1, 'message': 'karta ne nayden'}
    else:
        result = edit_card_design_db(**card_data)
        return {'status': 1, 'message': result}

#zapros na vivwsti vse karti ob opredelennom polzovatele
@card_router.get('/get_info')
async def get_all_user_cards(user_id: int):
    resuld = get_exact_user_cards_db(user_id=user_id)

    return {'status': 1, 'message': resuld}

#zapros na vivesti opredelennuyu kartu opredelennogo polzovatelya
@card_router.get('/exact_card_info')
async def get_card_info(card_id: int, user_id: int):
    result = get_exact_cards_db(card_id=card_id, user_id=user_id)

    if result:
        return {'status': 1, 'message': result}

    else:
        return {'status': 0, 'message': 'carta ne natden'}