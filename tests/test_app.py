from http import HTTPStatus


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'alice',
            'email': 'alice@example.com',
            'password': 'secret',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'alice',
        'email': 'alice@example.com',
        'id': 1,
    }


def test_create_conta(client):
    response = client.post(
        '/contas/',
        json={
            'mes': 'janeiro',
            'ano': '2026',
            'valor': 114.9,
            'bandeira': 'amarela',
            'consumo': 61,
            'vencimento': '24/01/2026',
            'status': 'paga',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'mes': 'janeiro',
        'ano': '2026',
        'consumo': 61,
    }


def test_read_users(client):
    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'alice',
                'email': 'alice@example.com',
                'id': 1,
            }
        ]
    }


def test_read_contas(client):
    response = client.get('/contas/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'contas': [
            {
                'id': 1,
                'mes': 'janeiro',
                'ano': '2026',
                'consumo': 61,
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'mynewpassword',
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'bob',
        'email': 'bob@example.com',
        'id': 1,
    }


def test_update_conta(client):
    response = client.put(
        '/contas/1',
        json={
            'mes': 'janeiro',
            'ano': '2026',
            'valor': 114.9,
            'bandeira': 'amarela',
            'consumo': 61,
            'vencimento': '24/01/2026',
            'status': 'em aberto',
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'mes': 'janeiro',
        'ano': '2026',
        'consumo': 61,
    }


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}


def test_delete_conta(client):
    response = client.delete('/contas/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Conta deleted'}
