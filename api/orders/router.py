from fastapi import APIRouter, HTTPException, Query

from .storage import get_orders_storage
from .schema import OrderCreateSchema, OrderUpdateSchema, Order

router = APIRouter()


ORDERS_STORAGE = get_orders_storage()

def biggest_element(key_list: list):
    list = key_list
    list.sort(reverse=True)
    return list[0]

@router.get("/")
async def get_orders() -> list[Order]:
    return list(get_orders_storage().values())

@router.get("/{order_id}")
async def get_order(order_id: int) -> Order:
    try:
        return ORDERS_STORAGE[order_id]
    except KeyError:
        raise HTTPException(
            status_code=404, detail=f"Order with ID={order_id} does not exist."
        )

@router.patch("/{order_id}")
async def update_order(
    order_id: int, updated_order: OrderUpdateSchema
) -> Order:
    try:
        if updated_order.date:
            ORDERS_STORAGE[order_id].date = updated_order.date
        if updated_order.quantity:
            ORDERS_STORAGE[order_id].quantity = updated_order.quantity
        if updated_order.customer_id:
            ORDERS_STORAGE[order_id].customer_id = updated_order.customer_id
        if updated_order.product_id:
            ORDERS_STORAGE[order_id].product_id = updated_order.product_id

        return ORDERS_STORAGE[order_id]
    except KeyError:
        raise HTTPException(
            status_code=404, detail=f"Order with ID={order_id} does not exist."
        )

@router.delete("/{order_id}")
async def delete_order(order_id: int) -> None:
    try:
        del ORDERS_STORAGE[order_id]
    except KeyError:
        raise HTTPException(
            status_code=404, detail=f"Order with ID={order_id} does not exist."
        )

@router.post("/")
async def create_order(order: OrderCreateSchema) -> Order:
    id = biggest_element(list(ORDERS_STORAGE.keys())) + 1 if ORDERS_STORAGE else 0
    ORDERS_STORAGE[id] = Order(**order.dict(), id=id)

    return ORDERS_STORAGE[id]

