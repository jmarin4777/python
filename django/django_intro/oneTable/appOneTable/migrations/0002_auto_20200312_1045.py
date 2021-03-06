# Generated by Django 2.2 on 2020-03-12 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appOneTable', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dungeon',
            old_name='prisoners',
            new_name='num_people_inside',
        ),
        migrations.CreateModel(
            name='Prisoner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('dungeon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prisoners', to='appOneTable.Dungeon')),
            ],
        ),
    ]
