from pydantic import BaseModel

class ProductCreateSchema(BaseModel):
    name: str
    brand: str
    release_date: str
    description: str

    class Config:
        schema_extra = {
            "example": {
                "name": "iPhone 20",
                "brand": "Apple",
                "release_date": "01.01.1970",
                "description": "standard product",
            }
        }

class ProductUpdateSchema(BaseModel):
    name: str | None
    brand: str | None
    release_date: str | None
    description: str | None

    class Config:
        schema_extra = {
            "example": {
                "name": "iPhone 19",
                "description": "sub-standard product"
            }
        }

class Product(ProductCreateSchema):
    id: int