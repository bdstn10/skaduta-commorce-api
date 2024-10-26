from tortoise.models import Model
from tortoise import fields

class productlist(Model):
    name = fields.CharField(max_length=225)
    stock = fields.IntField()
    price = fields.CharField(max_length=100)
    
    class Meta:
        table = "productlist"
    
    def __str__(self):
        return self.product_id