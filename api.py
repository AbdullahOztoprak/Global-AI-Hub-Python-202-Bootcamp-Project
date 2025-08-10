
from fastapi import FastAPI
from pydantic import BaseModel

# Pydantic models
class BookModel(BaseModel):
	title: str
	author: str
	isbn: str

class ISBNModel(BaseModel):
	isbn: str

app = FastAPI()
