from fastapi import APIRouter, HTTPException, Query

from .storage import get_products_storage
from .schema import ProductCreateSchema, ProductUpdateSchema, Product

router = APIRouter()


PRODUCTS_STORAGE = get_products_storage()

def biggest_element(key_list: list):
    list = key_list
    list.sort(reverse=True)
    return list[0]

@router.get("/")
async def get_products() -> list[Product]:
    return list(get_products_storage().values())

@router.get("/{product_id}")
async def get_product(product_id: int) -> Product:
    try:
        return PRODUCTS_STORAGE[product_id]
    except KeyError:
        raise HTTPException(
            status_code=404, detail=f"Product with ID={product_id} does not exist."
        )

@router.patch("/{product_id}")
async def update_product(
    product_id: int, updated_product: ProductUpdateSchema
) -> Product:
    try:
        if updated_product.name:
            PRODUCTS_STORAGE[product_id].name = updated_product.name
        if updated_product.brand:
            PRODUCTS_STORAGE[product_id].brand = updated_product.brand
        if updated_product.release_date:
            PRODUCTS_STORAGE[product_id].release_date = updated_product.release_date
        if updated_product.description:
            PRODUCTS_STORAGE[product_id].description = updated_product.description

        return PRODUCTS_STORAGE[product_id]
    except KeyError:
        raise HTTPException(
            status_code=404, detail=f"Product with ID={product_id} does not exist."
        )


@router.delete("/{product_id}")
async def delete_product(product_id: int) -> None:
    try:
        del PRODUCTS_STORAGE[product_id]
    except KeyError:
        raise HTTPException(
            status_code=404, detail=f"Product with ID={product_id} does not exist."
        )

@router.post("/")
async def create_product(product: ProductCreateSchema) -> Product:
    id = biggest_element(list(PRODUCTS_STORAGE.keys())) + 1 if PRODUCTS_STORAGE else 0
    PRODUCTS_STORAGE[id] = Product(**product.dict(), id=id)

    return PRODUCTS_STORAGE[id]

