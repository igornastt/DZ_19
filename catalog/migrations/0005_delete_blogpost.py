from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_blogpost'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BlogPost',
        ),
    ]
