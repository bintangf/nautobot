# Generated by Django 4.2.9 on 2024-01-17 18:52

from django.db import migrations
import django.db.models.deletion

import nautobot.core.models.fields
import nautobot.extras.models.statuses


class Migration(migrations.Migration):
    dependencies = [
        ("extras", "0104_contact_contactassociation_team"),
        ("dcim", "0053_create_hardware_family_model"),
        ("circuits", "0019_remove_providernetwork_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="circuit",
            name="status",
            field=nautobot.extras.models.statuses.StatusField(
                on_delete=django.db.models.deletion.PROTECT, to="extras.status"
            ),
        ),
        migrations.AlterField(
            model_name="circuittermination",
            name="_path",
            field=nautobot.core.models.fields.ForeignKeyWithAutoRelatedName(
                blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to="dcim.cablepath"
            ),
        ),
    ]
