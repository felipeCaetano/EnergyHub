from dataclasses import asdict

from sqlalchemy import select

from energyhub.models import Conta, User


def test_create_user(session, mock_db_time):
    with mock_db_time(model=User) as time:
        new_user = User(
            username='alice', password='secret', email='teste@test'
        )
        session.add(new_user)
        session.commit()

    user = session.scalar(select(User).where(User.username == 'alice'))

    assert asdict(user) == {
        'id': 1,
        'username': 'alice',
        'password': 'secret',
        'email': 'teste@test',
        'created_at': time,
    }


def test_create_conta(session, mock_db_time):
    with mock_db_time(model=Conta) as time:
        new_conta = Conta(
            mes='janeiro',
            ano='2026',
            bandeira='amarela',
            vencimento='26/01/2026',
            valor=114.9,
            consumo=61,

        )
        session.add(new_conta)
        session.commit()

    conta = session.scalar(select(Conta).where(Conta.mes == 'janeiro'))

    assert asdict(conta) == {
        'id': 1,
        "mes": 'janeiro',
        'ano': '2026',
        'bandeira': 'amarela',
        'vencimento': '26/01/2026',
        'valor': 114.9,
        'consumo': 61,
        'created_at': time,
    }
