# Generated by Django 2.2.6 on 2021-10-22 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_name', models.CharField(max_length=100, verbose_name='Издательство')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='p_library.Publisher'),
        ),
    ]