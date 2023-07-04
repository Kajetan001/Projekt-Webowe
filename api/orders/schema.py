from pydantic import BaseModel

class OrderCreateSchema(BaseModel):
    date: str
    quantity : int
    customer_id: int
    product_id: int

    class Config:
        schema_extra = {
            "example": {
                "date": "01.01.1970",
                "quantity": 1,
                "customer_id": 0,
                "product_id": 0
            }
        }


class OrderUpdateSchema(BaseModel):
    date: str | None
    quantity: int | None
    customer_id: int | None
    product_id: int | None

    class Config:
        schema_extra = {
            "example": {
                "quantity": 10
            }
        }


class Order(OrderCreateSchema):
    id: int