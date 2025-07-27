
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_coupon_coupon_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='discount_amount',
            field=models.IntegerField(default=100),
        ),
    ]
