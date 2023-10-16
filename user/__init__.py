from pydantic import BaseModel


#klas validatsii dlya registratsii
class UserRegisterModel(BaseModel):
    name: str
    surname: str
    email: str
    phone_number: str
    password: str
    city: str

#klass validatsii dlya izmeneniya dannix polzovatelya
class EditUserModel(BaseModel):
    user_id: int
    edit_type: str
    new_date: str