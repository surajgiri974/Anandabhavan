from django.db import models

# Create your models here.
class Customer(models.Model):
    customer_id = models.AutoField(db_column='customer_ID', primary_key=True)  # Field name made lowercase.
    customer_name = models.CharField(max_length=100)
    customer_email = models.CharField(max_length=256)
    customer_mobile = models.BigIntegerField()
    customer_password = models.CharField(max_length=24)
    account_type = models.IntegerField(db_column='Account_type', db_comment='1 = Free\r\n2 = Premium')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customer'