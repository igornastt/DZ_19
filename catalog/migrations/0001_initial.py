from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='наименование')),
                ('text', models.TextField(max_length=10000, verbose_name='описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='изображение')),
                ('category', models.CharField(verbose_name='категория')),
                ('price', models.IntegerField(verbose_name='цена')),
                ('date_creation', models.DateTimeField(verbose_name='дата создания')),
                ('date_change', models.DateTimeField(verbose_name='дата изменений')),
            ],
            options={
                'verbose_name': 'кетегория',
                'verbose_name_plural': 'кадегории',
                'ordering': ('title',),
            },
        ),
    ]
