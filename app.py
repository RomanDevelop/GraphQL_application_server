import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

# Определяем GraphQL тип
@strawberry.type
class Query:
    @strawberry.field
    def hello(self, name: str = "World") -> str:
        return f"Hello, {name}!"

# Создаем схему
schema = strawberry.Schema(query=Query)

# Инициализируем FastAPI
app = FastAPI()

# Подключаем GraphQL к FastAPI через strawberry
graphql_app = GraphQLRouter(schema)

app.include_router(graphql_app, prefix="/graphql")

@app.get("/")
async def root():
    return {"message": "Hello, FastAPI with Strawberry GraphQL"}
