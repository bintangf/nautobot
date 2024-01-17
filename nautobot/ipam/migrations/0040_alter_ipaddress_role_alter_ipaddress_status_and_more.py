# Generated by Django 4.2.9 on 2024-01-17 18:52

from django.db import migrations
import django.db.models.deletion

import nautobot.extras.models.roles
import nautobot.extras.models.statuses


class Migration(migrations.Migration):
    dependencies = [
        ("extras", "0105_alter_configcontext_cluster_groups_and_more"),
        ("ipam", "0039_alter_ipaddresstointerface_ip_address"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ipaddress",
            name="role",
            field=nautobot.extras.models.roles.RoleField(
                blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to="extras.role"
            ),
        ),
        migrations.AlterField(
            model_name="ipaddress",
            name="status",
            field=nautobot.extras.models.statuses.StatusField(
                on_delete=django.db.models.deletion.PROTECT, to="extras.status"
            ),
        ),
        migrations.AlterField(
            model_name="prefix",
            name="role",
            field=nautobot.extras.models.roles.RoleField(
                blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to="extras.role"
            ),
        ),
        migrations.AlterField(
            model_name="prefix",
            name="status",
            field=nautobot.extras.models.statuses.StatusField(
                on_delete=django.db.models.deletion.PROTECT, to="extras.status"
            ),
        ),
        migrations.AlterField(
            model_name="vlan",
            name="role",
            field=nautobot.extras.models.roles.RoleField(
                blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to="extras.role"
            ),
        ),
        migrations.AlterField(
            model_name="vlan",
            name="status",
            field=nautobot.extras.models.statuses.StatusField(
                on_delete=django.db.models.deletion.PROTECT, to="extras.status"
            ),
        ),
    ]
