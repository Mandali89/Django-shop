
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_profile_shippingaddress'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='shippingaddress',
            new_name='shipping_address',
        ),
    ]
