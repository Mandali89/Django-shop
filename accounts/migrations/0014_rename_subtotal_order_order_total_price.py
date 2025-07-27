
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_order_orderitem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='subtotal',
            new_name='order_total_price',
        ),
    ]
