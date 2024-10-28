from tortoise.models import Model
from tortoise import fields

class productlist(Model):
    product_id = fields.IntField(pk=True)
    name = fields.CharField(max_length=225)
    stock = fields.IntField()
    sold = fields.IntField()
    price = fields.CharField(max_length=100)
    img_link = fields.CharField(max_length=200)
    
    class Meta:
        table = "productlist"
    
    def __str__(self):
        return self.product_id