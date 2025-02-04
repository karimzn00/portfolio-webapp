# Generated by Django 2.2.12 on 2020-11-23 18:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MyProfile', '0011_auto_20201122_1941'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skills',
            name='description',
        ),
        migrations.AddField(
            model_name='language',
            name='level',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='skills',
            name='level',
            field=models.CharField(default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='myprofile',
            name='skills',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyProfile.Skills'),
        ),
        migrations.RemoveField(
            model_name='myprofile',
            name='social_media',
        ),
        migrations.AddField(
            model_name='myprofile',
            name='social_media',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='MyProfile.socialMedia'),
            preserve_default=False,
        ),
    ]
