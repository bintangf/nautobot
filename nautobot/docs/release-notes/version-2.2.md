<!-- markdownlint-disable MD024 -->

# Nautobot v2.2

This document describes all new features and changes in Nautobot 2.2.

## Release Overview

### Added

#### Contact and Team Models ([#230](https://github.com/nautobot/nautobot/issues/230))

Contact and Team are models that represent an individual and a group of individuals who can be linked to an object. Contacts and teams store the necessary information (name, phone number, email, and address) to uniquely identify and contact them. They are added to track ownerships of organizational entities and to manage resources more efficiently in Nautobot. Check out the documentation for [contact](../user-guide/core-data-model/extras/contact.md) and [team](../user-guide/core-data-model/extras/team.md). There is also a [user guide](../user-guide/feature-guides/contact-and-team.md) available on how to utilize these models.

#### Software Image File and Software Version models ([#1](https://github.com/nautobot/nautobot/issues/1))

New models have been added for software image files and software versions. These models are used to track the software versions of devices, inventory items and virtual machines and their associated image files. These models have been ported from the [Device Lifecycle Management App](https://github.com/nautobot/nautobot-app-device-lifecycle-mgmt/) and a future update to that app will migrate all existing data from the `nautobot_device_lifecycle_mgmt.SoftwareImageLCM` and `nautobot_device_lifecycle_mgmt.SoftwareLCM` models to the `dcim.SoftwareImageFile` and `dcim.SoftwareVersion` models added here.

Software versions must be associated to a platform. Software image files must be associated to one software version and may be associated to one or more device types. Devices, inventory items and virtual machines may be associated to one software version to track their current version. See the documentation for [software image file](../user-guide/core-data-model/dcim/softwareimagefile.md) and [software version](../user-guide/core-data-model/dcim/softwareversion.md). There is also a [user guide](../user-guide/feature-guides/software-image-files-and-versions.md) with instructions on how to create these models.

#### Prefix and VLAN Many Locations ([#4334](https://github.com/nautobot/nautobot/issues/4334), [#4412](https://github.com/nautobot/nautobot/issues/4412))

The Prefix and VLAN models have replaced their single `location` foreign-key field with a many-to-many `locations` field, allowing multiple Locations to be attached to a single Prefix or VLAN. To ensure backwards compatibility with pre-2.2 code, these models now have a `location` property which can be get or set for the case of a single associated Location, but will raise a `MultipleObjectsReturned` exception if the Prefix or VLAN in question has more than one associated Location. REST API versions 2.0 and 2.1 similarly still have a `location` field, while REST API version 2.2 and later replace this with `locations`.

#### Syntax highlighting ([#5098](https://github.com/nautobot/nautobot/issues/5098))

Language syntax highlighting for GraphQL, JSON, XML and YAML is now supported in the UI via JavaScript. To enable the feature, a code snippet has to be wrapped in the following HTML structure:

```html
<pre><code class="language-{graphql,json,xml,yaml}">...</code></pre>
```

[`render_json`](../user-guide/platform-functionality/template-filters.md#render_json) and [`render_yaml`](../user-guide/platform-functionality/template-filters.md#render_yaml) template filters default to this new behavior with an optional opt-out `syntax_highlight=False` arg.

#### Jobs tile view ([#5129](https://github.com/nautobot/nautobot/issues/5129))

Job list is now available in two display variants: list and tiles. List is a standard table view with no major changes introduced. Tiles is a new type of view displaying jobs in a two-dimensional grid.

### Changed

#### Data Imports as a System Job ([#5064](https://github.com/nautobot/nautobot/issues/5064))

The CSV import functionality for all models has been changed from a synchronous operation to an asynchronous background task (system Job). As a result, imports of large CSV files will no longer fail due to browser timeout.

!!! tip
    Users now must have the `run` action permission for `extras > job` (specifically the `nautobot.core.jobs.ImportObjects` Job) in order to import objects, in addition to the normal `add` permissions for the object type being imported.