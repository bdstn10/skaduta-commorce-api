from tortoise.models import Model
from tortoise import fields

class productlist(Model):
    product_id = fields.IntField(pk=True)
    name = fields.CharField(max_length=225)
    img_link = fields.CharField(max_length=200)
    store_id = fields.ForeignKeyField(
        'models.storelist',
        on_delete=fields.CASCADE
    )
    
    class Meta:
        table = "productlist"
    
    def __str__(self):
        return self.product_id
    
class storelist(Model):
    store_id = fields.IntField(pk=True)
    name = fields.CharField(max_length=225)
    location = fields.CharField(max_length=225)
    
class productvariants(Model):
    variant_id = fields.IntField(pk=True)
    variant_title = fields.CharField(max_length=255)
    stock = fields.IntField()
    sold = fields.IntField()
    price = fields.CharField(max_length=100)
    product_id = fields.ForeignKeyField(
        'models.productlist',
        on_delete=fields.CASCADE
    )
    