from typing import List
from customer.models import Customer


class CustomerController:
    def create(self, name: str, num_doc: str, phone: str) -> Customer:
        cust = Customer(name=name, num_doc=num_doc, phone=phone)
        cust.save()
        return cust

    def update(self, id_: int, name: str, num_doc: str, phone: str) -> Customer:
        cust = self.get_by_id(id_)
        cust.name = name
        cust.num_doc = num_doc
        cust.phone = phone
        cust.save()
        return cust

    def delete(self, id_: int) -> None:
        cust = self.get_by_id(id_)
        cust.delete()

    def get_all(self) -> List[Customer]:
        return Customer.objects.all()

    def get_by_id(self, id_: int) -> Customer:
        return Customer.objects.filter(id=id_).get()
