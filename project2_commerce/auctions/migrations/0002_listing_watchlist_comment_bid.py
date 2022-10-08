# Generated by Django 4.1 on 2022-09-25 07:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('desc', models.CharField(blank=True, max_length=200, null=True)),
                ('img', models.URLField(blank=True, null=True)),
                ('category', models.CharField(blank=True, max_length=50, null=True)),
                ('active_status', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL)),
                ('winner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bidwinner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Watchlist',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('list_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='watchlisted', to='auctions.listing')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='watchlist', to='auctions.listing')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('comment', models.CharField(max_length=200)),
                ('list_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='list_comments', to='auctions.listing')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_comments', to='auctions.listing')),
            ],
        ),
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('amount', models.IntegerField()),
                ('winner', models.BooleanField(default=False)),
                ('list_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bids', to='auctions.listing')),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='biddings', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]