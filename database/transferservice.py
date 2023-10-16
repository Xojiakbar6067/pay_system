from datetime import datetime

from database.models import Transfer, UserCard
from database import get_db

#proverka karti
def _validate_card(card_number, db):

    exact_card = db.query(UserCard).filter_by(card_number=card_number).first()

    return exact_card

#sozdat perevod
def create_transaction_db(card_from, card_to, amound):
    db = next(get_db())

    #proverka na nalichii v baze obeix kard
    check_card_from = _validate_card(card_from, db)
    check_card_to = _validate_card(card_to, db)

    #esli oba karti sushestvuet v baze
    if check_card_from and check_card_to:
        #proverka balansa togo kto vrovodit dengi
        if check_card_from.balance>=amound:
            check_card_from.balance-=amound
            check_card_to.balance+=amound

            new_transaction = Transfer(card_from_id=check_card_from.card_id, card_to_id=check_card_to.card_id, amount=amound, transaction_date=datetime.now())

            db.add(new_transaction)
            db.commit()

            return 'perevod uspeshno vipolnen'
        else:
            return 'nedostatochna sredst v balanse'

    return 'odno iz kart ne sushectvuet'


#poluchit vse perevodi po karte (card_id)
def get_all_user_tarnsfers_db(card_from_id):
    db = next(get_db())

    card_transaction = db.query(Transfer).filter_by(card_from_id=card_from_id).all()

    return card_transaction

#otmenit perevod
def cancel_transfer_db(card_from, card_to, amound, transfer_id):
    db = next(get_db())

    check_card_from = _validate_card(card_from, db)
    check_card_to = _validate_card(card_to, db)

    if check_card_from and check_card_to:
        #proverka balansa togo kto vrovodit dengi
        if check_card_to.balance >= amound:
            check_card_from.balance += amound
            check_card_to.balance -= amound

            exact_transaction = db.query(Transfer).filter_by(transfer_id=transfer_id).first()
            exact_transaction.status = False

            db.commit()

            return 'perevod uspeshno atmenen'
        return 'karta ne nayden'