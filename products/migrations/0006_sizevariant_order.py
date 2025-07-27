
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_coupon_discount_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='sizevariant',
            name='order',
            field=models.IntegerField(default=0),
        ),
    ]
