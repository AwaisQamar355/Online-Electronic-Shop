# Generated by Django 3.2.25 on 2024-07-17 07:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0004_signup'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=155)),
                ('lastname', models.CharField(max_length=155)),
                ('country', models.CharField(max_length=155)),
                ('address', models.CharField(max_length=155)),
                ('city', models.CharField(max_length=155)),
                ('state', models.CharField(max_length=155)),
                ('postcode', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('amount', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=300)),
                ('image', models.ImageField(default='', upload_to='shop/imagess')),
                ('quantity', models.CharField(max_length=20)),
                ('price', models.CharField(max_length=60)),
                ('total', models.CharField(max_length=3000)),
                ('oredr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.checkout')),
            ],
        ),
    ]
