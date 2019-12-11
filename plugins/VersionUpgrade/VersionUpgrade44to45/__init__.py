# Copyright (c) 2019 Ultimaker B.V.
# Cura is released under the terms of the LGPLv3 or higher.

from typing import Any, Dict, TYPE_CHECKING

from . import VersionUpgrade44to45


if TYPE_CHECKING:
    from UM.Application import Application

upgrade = VersionUpgrade44to45.VersionUpgrade44to45()


def getMetaData() -> Dict[str, Any]:
    return {
        "version_upgrade": {
            # From                           To                              Upgrade function
            ("preferences", 6000010): ("preferences", 6000011, upgrade.upgradePreferences),
            ("machine_stack", 4000010): ("machine_stack", 4000011, upgrade.upgradeStack),
            ("extruder_train", 4000010): ("extruder_train", 4000011, upgrade.upgradeStack),
            ("definition_changes", 4000010): ("definition_changes", 4000011, upgrade.upgradeInstanceContainer),
            ("quality_changes", 4000010): ("quality_changes", 4000011, upgrade.upgradeInstanceContainer),
            ("quality", 4000010): ("quality", 4000011, upgrade.upgradeInstanceContainer),
            ("user", 4000010): ("user", 4000011, upgrade.upgradeInstanceContainer),
        },
        "sources": {
            "preferences": {
                "get_version": upgrade.getCfgVersion,
                "location": {"."}
            },
            "machine_stack": {
                "get_version": upgrade.getCfgVersion,
                "location": {"./machine_instances"}
            },
            "extruder_train": {
                "get_version": upgrade.getCfgVersion,
                "location": {"./extruders"}
            },
            "definition_changes": {
                "get_version": upgrade.getCfgVersion,
                "location": {"./definition_changes"}
            },
            "quality_changes": {
                "get_version": upgrade.getCfgVersion,
                "location": {"./quality_changes"}
            },
            "quality": {
                "get_version": upgrade.getCfgVersion,
                "location": {"./quality"}
            },
            "user": {
                "get_version": upgrade.getCfgVersion,
                "location": {"./user"}
            }
        }
    }


def register(app: "Application") -> Dict[str, Any]:
    return {"version_upgrade": upgrade}
