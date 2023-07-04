import { MainNav } from "@/components/MainNav";

import { DataTable } from "./components/DataTable";
import { Columns } from "./components/Columns";
import { UserNav } from "./components/UserNav";
import { navigationLinks } from "../../config/navigationLinks";
import { useEffect, useState } from "react";

export const OrdersPage = () => {
  const [data, setData] = useState({
    orders: [],
    customers: [],
    products: []
  });

  useEffect(() => {
    const fetchData = async () => {
        const [ordersResponse, customersResponse, productsResponse] = await Promise.all([
          fetch("http://127.0.0.1:8000/orders").then((response) => response.json()),
          fetch("http://127.0.0.1:8000/customers").then((response) => response.json()),
          fetch("http://127.0.0.1:8000/products").then((response) => response.json())
        ]);
  
        setData((prevState) => ({
          ...prevState,
          orders: ordersResponse,
          customers: customersResponse,
          products: productsResponse
        }));
    };
  
    fetchData();
    console.log(data.orders)
  }, []);

  const updatedOrders = data.orders.map((order) => {
    const matchingProduct = data.products.find((product) => product.id === order.product_id);
    const matchingCustomer = data.customers.find((customer) => customer.id === order.customer_id);
  
    if (matchingProduct) {
      order = { ...order, product_name: matchingProduct.name };
    }
    if (matchingCustomer) {
      order = { ...order, customer_name: matchingCustomer.name + " " + matchingCustomer.surname};
    }
  
    return order;
  });
  
  
  return (
    <div className="hidden flex-col md:flex">
      <div className="border-b">
        <div className="flex h-16 items-center px-4">
          <MainNav className="mx-6" links={navigationLinks} />
          <div className="ml-auto flex items-center space-x-4">
            <UserNav />
          </div>
        </div>
      </div>
      <div className="flex-1 space-y-4 p-8 pt-6">
        <div className="flex items-center justify-between space-y-2">
          <h2 className="text-3xl font-bold tracking-tight">Orders</h2>
        </div>
        <div className="hidden h-full flex-1 flex-col space-y-8 md:flex">
          <DataTable
            data={updatedOrders}
            columns={Columns}
          />
        </div>
      </div>
    </div>
  );
};
