# Generated by Django 5.0.3 on 2024-05-05 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_alter_productcomment_user_dislike_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]