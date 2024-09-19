from sqlalchemy.orm import Session
from app.database.crud import create_item, get_item
from app.schemas.item_schema import ItemCreate

class ItemService:
    @staticmethod
    def create_item(db: Session, item: ItemCreate):
        return create_item(db, item)

    @staticmethod
    def get_item(db: Session, item_id: int):
        return get_item(db, item_id)   
