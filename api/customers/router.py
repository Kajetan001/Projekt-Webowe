from fastapi import APIRouter, HTTPException, Query

from .storage import get_customers_storage
from .schema import CustomerCreateSchema, CustomerUpdateSchema, Customer

router = APIRouter()


CUSTOMERS_STORAGE = get_customers_storage()

def biggest_element(key_list: list):
    list = key_list
    list.sort(reverse=True)
    return list[0]

@router.get("/")
async def get_customers() -> list[Customer]:
    return list(get_customers_storage().values())

@router.get("/{customer_id}")
async def get_customer(customer_id: int) -> Customer:
    try:
        return CUSTOMERS_STORAGE[customer_id]
    except KeyError:
        raise HTTPException(
            status_code=404, detail=f"Customer with ID={customer_id} does not exist."
        )

@router.patch("/{customer_id}")
async def update_customer(
    customer_id: int, updated_customer: CustomerUpdateSchema
) -> Customer:
    try:
        if updated_customer.name:
            CUSTOMERS_STORAGE[customer_id].name = updated_customer.name
        if updated_customer.surname:
            CUSTOMERS_STORAGE[customer_id].surname = updated_customer.surname
        if updated_customer.email:
            CUSTOMERS_STORAGE[customer_id].email = updated_customer.email
        if updated_customer.phone_number:
            CUSTOMERS_STORAGE[customer_id].phone_number = updated_customer.phone_number

        return CUSTOMERS_STORAGE[customer_id]
    except KeyError:
        raise HTTPException(
            status_code=404, detail=f"Customer with ID={customer_id} does not exist."
        )


@router.delete("/{customer_id}")
async def delete_customer(customer_id: int) -> None:
    try:
        del CUSTOMERS_STORAGE[customer_id]
    except KeyError:
        raise HTTPException(
            status_code=404, detail=f"Customer with ID={customer_id} does not exist."
        )

@router.post("/")
async def create_customer(customer: CustomerCreateSchema) -> Customer:
    id = biggest_element(list(CUSTOMERS_STORAGE.keys())) + 1 if CUSTOMERS_STORAGE else 0
    CUSTOMERS_STORAGE[id] = Customer(**customer.dict(), id=id)

    return CUSTOMERS_STORAGE[id]

