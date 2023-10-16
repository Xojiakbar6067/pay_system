from pydantic import BaseModel

#klass validatsii carti
class CreateTransactionModel(BaseModel):
    card_from: int
    card_to: int
    amound: float

#klass validatsii tranzaksii
class CancelTransactionModel(BaseModel):
    card_from: int
    card_to: int
    amound: float
    transfer_id: int