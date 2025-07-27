
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_product_last_visit_product_num_visits_product_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='last_visit',
        ),
        migrations.RemoveField(
            model_name='product',
            name='num_visits',
        ),
    ]
