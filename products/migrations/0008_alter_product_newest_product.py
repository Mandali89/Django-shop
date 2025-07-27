
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_product_newest_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='newest_product',
            field=models.BooleanField(default=False),
        ),
    ]
