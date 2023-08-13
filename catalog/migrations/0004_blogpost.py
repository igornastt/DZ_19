from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('catalog', '0003_alter_category_options_alter_product_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('content', models.TextField()),
                ('preview', models.ImageField(upload_to='blog_previews/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_published', models.BooleanField(default=False)),
                ('views', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'блоговая запись',
                'verbose_name_plural': 'блоговые записи',
                'ordering': ('title',),
            },
        ),
    ]
