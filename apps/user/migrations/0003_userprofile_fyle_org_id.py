# Generated by Django 3.0.4 on 2020-03-18 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200315_1139'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='fyle_org_id',
            field=models.CharField(help_text='Organisation id in Fyle', max_length=255, null=True),
        ),
    ]