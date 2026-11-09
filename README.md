# UTC to Timezone

API FastAPI para cadastrar, editar e consultar usuários e seus fusos horários.

## Executar localmente

Na raiz do projeto:

```bash
python3 -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
python -m uvicorn main:app --reload
```

## Rotas

- POST /users: cadastra um usuário (201).
- GET /users: lista usuários. (200)
- GET /users/{user_id}: consulta um usuário (200, e 404 se não existir).
- PUT /users: atualiza um usuário pelo campo Id (200 e 404 se não existir).

Exemplo de cadastro:

```json
{
  "Name": "Noah",
  "Email": "noah@example.com",
  "Timezone": "America/Sao_Paulo"
}
```

