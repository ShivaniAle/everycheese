# Generated by Django 3.1.1 on 2023-10-11 04:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cheeses', '0006_cheese_firmness'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='firmness',
        ),
        migrations.AddField(
            model_name='cheese',
            name='rating',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=3),
        ),
        migrations.AlterField(
            model_name='cheese',
            name='firmness',
            field=models.CharField(choices=[('unspecified', 'Unspecified'), ('soft', 'Soft'), ('semi-soft', 'Semi-Soft'), ('semi-hard', 'Semi-Hard'), ('hard', 'Hard')], default='unspecified', max_length=20, verbose_name='Firmness'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='cheese',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ratings', to='cheeses.cheese'),
        ),
    ]