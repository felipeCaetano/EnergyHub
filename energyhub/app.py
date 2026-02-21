from http import HTTPStatus

from fastapi import FastAPI, HTTPException

from energyhub.schemas import (
    ContaDB,
    ContaPublic,
    ContaSchema,
    ContasList,
    Message,
    UserDB,
    UserList,
    UserPublic,
    UserSchema,
)

app = FastAPI()
database = []
database_contas = []


@app.post(
    '/contas/', status_code=HTTPStatus.CREATED, response_model=ContaPublic
)
def create_conta(conta: ContaSchema):
    conta_with_id = ContaDB(**conta.model_dump(), id=len(database_contas) + 1)
    database_contas.append(conta_with_id)
    return conta_with_id


@app.get('/contas/', response_model=ContasList)
def read_contas():
    return {'contas': database_contas}


@app.put('/contas/{conta_id}', response_model=ContaPublic)
def update_conta(conta_id: int, conta: ContaSchema):
    if conta_id > len(database_contas) or conta_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Conta not found'
        )
    conta_with_id = ContaDB(**conta.model_dump(), id=conta_id)
    database_contas[conta_id - 1] = conta_with_id
    return conta_with_id


@app.delete('/contas/{conta_id}', response_model=Message)
def delete_conta(conta_id: int):
    if conta_id > len(database_contas) or conta_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Conta not found'
        )

    del database_contas[conta_id - 1]

    return {'message': 'Conta deleted'}


@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    user_with_id = UserDB(**user.model_dump(), id=len(database) + 1)
    database.append(user_with_id)
    return user_with_id


@app.get('/users/', response_model=UserList)
def read_users():
    return {'users': database}


@app.put('/users/{user_id}', response_model=UserPublic)
def update_user(user_id: int, user: UserSchema):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )
    user_with_id = UserDB(**user.model_dump(), id=user_id)
    database[user_id - 1] = user_with_id
    return user_with_id


@app.delete('/users/{user_id}', response_model=Message)
def delete_user(user_id: int):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )

    del database[user_id - 1]

    return {'message': 'User deleted'}
