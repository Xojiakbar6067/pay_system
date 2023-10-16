from pydantic import BaseModel

#klass dlya validatsii dobavleniya karti
class CardAddModel(BaseModel):
    user_id: int
    card_number: int
    balance: float
    exp_date: int
    card_name: str
    cvv: int

#klass dlya validatsii izmeneniya dizayn karti
class EditDicaginCard(BaseModel):
    card_id: int
    design_path: str