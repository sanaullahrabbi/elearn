# Generated by Django 3.2.9 on 2022-04-27 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_article', '0003_auto_20220425_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='categories',
            field=models.CharField(choices=[('', 'Please Select'), ('How To Articles', 'How To Articles'), ('List Articles', 'List Articles'), ('Round Up Articles', 'Round Up Articles'), ('Guide Articles', 'Guide Articles'), ('Comparison Articles', 'Comparison Articles')], default='', max_length=255, null=True),
        ),
    ]
