from database.models import User
from database import get_db

#registratsiya polzovatelya (name, surname, phone_number, reg_date, password, city)
def add_new_user_db( name, surname, phone_number, city, password, reg_date, email):
    db = next(get_db())

    checker = db.query(User).filter_by(phone_number=phone_number).first()

    if checker:
        return 'takoy polzovatel uje sushestvuet'
    else:
        new_user = User( name=name,email=email, surname=surname, phone_number=phone_number, city=city, password=password, reg_date=reg_date)

        db.add(new_user)
        db.commit()

        return 'polzovatel uspeshno dobavlen'

#poluchit informatsiyu o polzovatele (user_id)
def get_exact_user_db(user_id):
    db = next(get_db())

    exact_user = db.query(User).filter_by(user_id=user_id).first()

    return exact_user

#proverka dannix (email)
def check_email_db(email):
    db = next(get_db())

    email = db.query(User).filter_by(email=email).first()

    if email:
        return email
    else:
        return False

#izmenit dannie (user_id, edit_type, new_data)
def change_user_info_db(user_id, edit_type, new_data):
    db = next(get_db())

    exact_user = db.query(User).filter_by(user_id=user_id).first()

    if exact_user:
        if edit_type == 'city':
            exact_user.city = new_data

        elif edit_type == 'email':
            exact_user.email = new_data

        elif edit_type == 'password':
            exact_user.password = new_data

        db.commit()
        return 'dannie uspeshno izmeneni'
    return 'polzovatel ne nayden'

#udalit polzovatelya (user_id)
def delete_exact_user_db(user_id):
    db = next(get_db())

    exact_user = db.query(User).filter_by(user_id=user_id).first()

    if exact_user:
        db.delete(exact_user)
        db.commit()

        return 'polzovatel uspeshno udalen'
    else:
        return 'polzovatel ne nayden'