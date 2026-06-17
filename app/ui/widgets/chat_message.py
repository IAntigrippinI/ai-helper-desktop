from typing import Literal

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout
from qfluentwidgets import BodyLabel

MessageRole = Literal["user", "assistant"]

class ChatMessage(QWidget):

    def __init__(self, text: str, role: MessageRole):
        super().__init__()

        self._text = text
        self._role = role

        self._init_ui()


    def _init_ui(self):
        root_layout = QHBoxLayout(self)
        root_layout.setContentsMargins(0, 4, 0, 4)


        bubble = QWidget()
        bubble.setObjectName('userBubble' if self._role == 'user' else 'assistantBubble')
        bubble.setMaximumWidth(500)

        bubble_layout = QVBoxLayout(bubble)
        bubble_layout.setContentsMargins(12, 8, 12, 8)

        label = BodyLabel(self._text)
        label.setWordWrap(True)

        if self._role == "user":
            label.setAlignment(Qt.AlignmentFlag.AlignRight)
        else:
            label.setAlignment(Qt.AlignmentFlag.AlignLeft)

        bubble_layout.addWidget(label)

        if self._role == "user":
            # Пустое место слева, сообщение справа
            root_layout.addStretch()
            root_layout.addWidget(bubble)
        else:
            # Сообщение слева, пустое место справа
            root_layout.addWidget(bubble)
            root_layout.addStretch()
