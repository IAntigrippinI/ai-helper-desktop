from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit,
    QSizePolicy,
)

from qfluentwidgets import BodyLabel


class SettingValue(QWidget):
    """
    Виджет одной настройки.

    Отображение:
        NAME
        [ value ]
    """

    ROW_HEIGHT = 78

    def __init__(self, name: str, value: str, parent=None):
        super().__init__(parent)

        self._name = name
        self._value = value

        # Важно: вся строка настройки фиксированная по высоте
        self.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Fixed,
        )
        self.setFixedHeight(self.ROW_HEIGHT)

        self._init_ui()

    def _init_ui(self) -> None:
        root_layout = QHBoxLayout(self)
        root_layout.setContentsMargins(0, 0, 0, 0)
        root_layout.setSpacing(0)

        container = QWidget(self)
        container.setObjectName("settingValue")

        container.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Fixed,
        )
        container.setFixedHeight(72)

        container_layout = QVBoxLayout(container)
        container_layout.setContentsMargins(12, 6, 12, 8)
        container_layout.setSpacing(4)

        self.label = BodyLabel(self._name)
        self.label.setObjectName("settingName")
        self.label.setFixedHeight(20)
        self.label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)

        self.input = QLineEdit()
        self.input.setText(str(self._value) if self._value is not None else "")
        self.input.setFixedHeight(30)
        self.input.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Fixed,
        )

        container_layout.addWidget(self.label)
        container_layout.addWidget(self.input)

        root_layout.addWidget(container)