from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    message: str


class ContaSchema(BaseModel):
    mes: str
    ano: str
    valor: float
    bandeira: str
    consumo: int
    vencimento: str
    status: str


class ContaPublic(BaseModel):
    id: int
    mes: str
    ano: str
    consumo: int


class ContaDB(ContaSchema):
    id: int


class ContasList(BaseModel):
    contas: list[ContaPublic]


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserPublic(BaseModel):
    id: int
    username: str
    email: EmailStr


class UserDB(UserSchema):
    id: int


class UserList(BaseModel):
    users: list[UserPublic]
