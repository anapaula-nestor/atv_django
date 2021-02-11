from typing import List

from product.models import Product


class ProductController:
    def create(self, name: str, description: str, price: float) -> Product:
        prod = Product(name=name, description=description, price=price)
        prod.save()
        return prod

    def update(self, id_: int, name: str, description: str, price: float) -> Product:
        prod = self.get_by_id(id_)
        prod.name = name
        prod.description = description
        prod.price = price
        prod.save()
        return prod

    def delete(self, id_: int) -> None:
        prod = self.get_by_id(id_)
        prod.delete()

    def get_all(self) -> List[Product]:
        return Product.objects.all()

    def get_by_id(self, id_: int) -> Product:
        return Product.objects.filter(id=id_).get()
