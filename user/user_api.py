from fastapi import APIRouter
from datetime import datetime

from database.userservice import add_new_user_db, get_exact_user_db, check_email_db, change_user_info_db, delete_exact_user_db

from user import UserRegisterModel, EditUserModel

user_router = APIRouter(prefix='/user', tags=['rabota s polzovatelyami'])

#registratsiya polzovatelya
@user_router.post('/register')
async def register_user(data: UserRegisterModel):
    #perevodim paydentik v obichniy slovar
    new_user_data = data.dict()
    #vizov funksii dlya proverki pochti v baze
    checker = check_email_db(data.email)

    if not checker:
        result = add_new_user_db(reg_date=datetime.now(), **new_user_data)

        return {'status': 1, 'message': result}

    return {'status': 0, 'message': 'polzovatel c takoy pochtoy uje sushestvuet'}

@user_router.get('/info')
async def get_user(user_id: int):
    result = get_exact_user_db(user_id)
    return {'status': 1 if result else 0, 'message': result}

@user_router.put('/edit-data')
async def edit_user(data: EditUserModel):
    change_data = data.dict()

    result = change_user_info_db(**change_data)

    return {'status': 1, 'message': result}


@user_router.delete('/delete-user')
async def delete_user(user_id: int):
    result = delete_exact_user_db(user_id)

    return {'status': 1, 'message': result}