from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
from fastapi.responses import RedirectResponse
from tkinter import *
from gui import OrderGUI

app = FastAPI()

class OrderData(BaseModel):
    products: list
    currency: str
    external_id: str
    description: str

class OrderResponse(BaseModel):
    created_at: str
    updated_at: str
    uuid: str
    amount: int
    back_url: str
    notify_url: str
    description: str
    status: str
    currency: str
    checkout_url: str
    external_id: str
    receiver: str
    products: list

class ErrorResponse(BaseModel):
    detail: list

create_order_url = "https://api-dev.asadalpay.com/api/orders/create-order"

api_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJsZWdhbF9lbnRpdHlfaWQiOjcsImNyZWF0ZWRfYXQiOiIyMDIzLTA5LTIxIDA5OjE1OjExLjYwNDQyOSIsInBhc3N3b3JkIjoiOWViZmZkMjQtNzI2Ny00NjZkLTk0MTctZGViMTY4YzZmM2RmIn0.OLy0oUg3rUqWxJp8veLMeOXlbyQrsIJF2BqtsmQYY78"  

@app.post("api/orders/create-order", response_model=OrderResponse, responses={422: {"model": ErrorResponse}})
async def create_order(order_data: OrderData):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    response = requests.post(create_order_url, headers=headers, json=order_data.dict())

    if response.status_code == 201:
        response_data = response.json()
        return RedirectResponse(url=response_data['checkout_url'], status_code=303)
    else:
        raise HTTPException(status_code=422, detail=response.json())

@app.get("/order/{order_uuid}", response_model=OrderResponse, responses={404: {"model": ErrorResponse}})
async def get_order(order_uuid: str):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    response = requests.get(f"https://api-dev.asadalpay.com/api/orders/{order_uuid}", headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=404, detail=response.json())

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
root = Tk()
app = OrderGUI(root)
root.mainloop()