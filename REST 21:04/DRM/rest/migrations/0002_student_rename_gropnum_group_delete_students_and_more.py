# Generated by Django 4.1.7 on 2023-04-21 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='ФИО')),
                ('age', models.IntegerField(verbose_name='Возраст')),
                ('sex', models.IntegerField(choices=[(1, 'Ж'), (2, 'М')], verbose_name='Sex')),
            ],
        ),
        migrations.RenameModel(
            old_name='GropNum',
            new_name='Group',
        ),
        migrations.DeleteModel(
            name='Students',
        ),
        migrations.AddField(
            model_name='student',
            name='group',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='rest.group'),
        ),
    ]
