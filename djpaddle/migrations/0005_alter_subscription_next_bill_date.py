# Generated by Django 4.1.4 on 2022-12-31 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("djpaddle", "0004_auto_20210119_0436"),
    ]

    operations = [
        migrations.AlterField(
            model_name="subscription",
            name="next_bill_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]