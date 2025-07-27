
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_coupon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='coupon_code',
            field=models.CharField(max_length=10),
        ),
    ]
