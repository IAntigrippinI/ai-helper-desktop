from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QScrollArea, QSizePolicy

from qfluentwidgets import BodyLabel

from app.config.ai import ai_config
from app.ui.widgets.setting_value import SettingValue


class SettingsWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Expanding,
        )

        self._init_ui()

    def _init_ui(self) -> None:
        root_layout = QVBoxLayout(self)
        root_layout.setContentsMargins(0, 0, 0, 0)
        root_layout.setSpacing(0)

        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setObjectName("SettingsScrollArea")
        self.scroll_area.setFrameShape(QScrollArea.Shape.NoFrame)

        self.settings_container = QWidget()
        self.settings_container.setObjectName("settingsContainer")
        self.settings_container.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Minimum,
        )

        self.settings_layout = QVBoxLayout(self.settings_container)
        self.settings_layout.setContentsMargins(6, 6, 6, 6)
        self.settings_layout.setSpacing(6)

        # ВАЖНО: все настройки прижимаются к верху
        self.settings_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.scroll_area.setWidget(self.settings_container)

        settings = [ai_config]

        for s in settings:
            group_label = BodyLabel(str(s._CONFIG_NAME))
            group_label.setObjectName("settingsGroupTitle")
            group_label.setSizePolicy(
                QSizePolicy.Policy.Expanding,
                QSizePolicy.Policy.Fixed,
            )

            self.settings_layout.addWidget(group_label)

            for k, v in s._get_config_attrs().items():
                self.settings_layout.addWidget(SettingValue(k, v))

        # ВАЖНО: пустота теперь будет только снизу, а не между элементами
        self.settings_layout.addStretch(1)

        root_layout.addWidget(self.scroll_area)