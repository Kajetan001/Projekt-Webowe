import { MainNav } from "@/components/MainNav";
import { navigationLinks } from "../config/navigationLinks";
import { Input } from "@/components/ui/Input";
import { Form } from "@/components/ui/Form";
import { Button } from "@/components/ui/Button";
import { UserNav } from "./CustomersPage/components/UserNav";
import { useEffect, useState } from "react";
import { SelectScrollUpButton } from "@radix-ui/react-select";

export const AddCustomerPage = () => {
  const [name, setName] = useState("")
  const [surname, setSurname] = useState("")
  const [email, setEmail] = useState("")
  const [phone_number, setPhoneNumber] = useState("")

  const submit = (e) => {
    e.preventDefault();
    
    fetch("http://127.0.0.1:8000/customers/" , {
      method:"POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({"name":name, "surname":surname, "email":email, "phone_number":phone_number})
    }).then((response) => response.json())

    setName("")
    setSurname("")
    setEmail("")
    setPhoneNumber("")
  }
  
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
          <h2 className="text-3xl font-bold tracking-tight">Add customer</h2>
        </div>
        <div className="hidden h-full flex-1 flex-col space-y-8 md:flex">
          <Form>
            <Input value={name} onChange={(e) => setName(e.target.value)} type="text" name="name" placeholder="Name"/>
            <Input value={surname} onChange={(e) => setSurname(e.target.value)} type="text" name="surname" placeholder="Surname"/>
            <Input value={email} onChange={(e) => setEmail(e.target.value)} type="text" name="email" placeholder="Email"/>
            <Input value={phone_number} onChange={(e) => setPhoneNumber(e.target.value)} type="text" name="phone_number" placeholder="Phone Number"/>
            <Button type="submit" onClick = {submit}>Add</Button>
          </Form>
        </div>
      </div>
    </div>
  );
};
