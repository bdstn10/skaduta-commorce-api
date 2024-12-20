from tortoise.models import Model
from tortoise import fields

class productlist(Model):
    product_id = fields.IntField(pk=True)
    name = fields.CharField(max_length=225, unique=True)
    cover_link = fields.CharField(max_length=200)
    with_variant = fields.BooleanField()
    store_id = fields.ForeignKeyField(
        'models.storelist',
        on_delete=fields.CASCADE
    )
    
    class Meta:
        table = "productlist"
    
    def __str__(self):
        return self.name
    
class productdetails(Model):
    variant_name = fields.CharField(max_length=255, null=True)
    variant_option = fields.CharField(max_length=255, null=True)
    stock = fields.IntField()
    sold = fields.IntField()
    price = fields.CharField(max_length=100)
    product_id = fields.ForeignKeyField(
        'models.productlist',
        on_delete=fields.CASCADE
    )

class storelist(Model):
    store_id = fields.IntField(pk=True)
    name = fields.CharField(max_length=225, unique=True)
    location = fields.CharField(max_length=225)
    owner = fields.OneToOneField(
        'models.userlist',
        on_delete=fields.CASCADE
    )

class userlist(Model):
    uid = fields.IntField(pk=True)
    username = fields.CharField(max_length=255)
    email = fields.CharField(max_length=225)
    phone = fields.CharField(max_length=15)
    gender = fields.CharField(max_length=1)

class cart(Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField('models.userlist', on_delete=fields.CASCADE)
    
class cartitem(Model):
    cart = fields.ForeignKeyField('models.cart', on_delete=fields.CASCADE)
    product = fields.ForeignKeyField('models.productlist', on_delete=fields.CASCADE)
    variant_name = fields.CharField(max_length=255, null=True)
    variant_option = fields.CharField(max_length=255, null=True)
    quantity = fields.IntField()
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)