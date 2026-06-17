import loguru
from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QScrollArea,
    QLineEdit,
)

from qfluentwidgets import PrimaryPushButton

from app.ai.connector import openai_connector
from app.ui.widgets.chat_message import ChatMessage


class ChatPanel(QWidget):
    """
    Панель чата:
    - сверху список сообщений;
    - снизу поле ввода и кнопка отправки.
    """

    def __init__(self, parent=None):
        super().__init__(parent)

        self._init_ui()

    def _init_ui(self) -> None:
        root_layout = QVBoxLayout(self)
        root_layout.setContentsMargins(0, 0, 0, 0)
        root_layout.setSpacing(10)

        # Область прокрутки
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setObjectName("chatScrollArea")

        # Контейнер сообщений внутри скролла
        self.messages_container = QWidget()
        self.messages_layout = QVBoxLayout(self.messages_container)
        self.messages_layout.setContentsMargins(4, 4, 4, 4)
        self.messages_layout.setSpacing(6)

        # Растяжка внизу, чтобы сообщения шли сверху вниз
        self.messages_layout.addStretch()

        self.scroll_area.setWidget(self.messages_container)

        # Нижняя панель ввода
        input_layout = QHBoxLayout()

        self.input = QLineEdit()
        self.input.setPlaceholderText("Введите сообщение...")
        self.input.returnPressed.connect(self._handle_send)

        self.send_button = PrimaryPushButton("Отправить")
        self.send_button.clicked.connect(self._handle_send)

        input_layout.addWidget(self.input)
        input_layout.addWidget(self.send_button)

        root_layout.addWidget(self.scroll_area)
        root_layout.addLayout(input_layout)

    def add_message(self, text: str, role: str) -> None:
        """
        Добавляет сообщение в чат.
        """

        message = ChatMessage(text=text, role=role)

        # Вставляем перед stretch, чтобы stretch всегда оставался внизу
        self.messages_layout.insertWidget(
            self.messages_layout.count() - 1,
            message,
        )

        self._scroll_to_bottom()

    def _handle_send(self) -> None:
        """
        Обработка отправки сообщения пользователя.
        """

        text = self.input.text().strip()

        if not text:
            return

        self.input.clear()

        # Сообщение пользователя справа
        self.add_message(text, role="user")

        response = openai_connector.get_response(text)
        loguru.logger.debug(response)
        # Пока просто тестовый ответ ИИ слева
        # Потом здесь будет вызов твоего AIService
        self.add_message(
            response.content,
            role="assistant",
        )

    def _scroll_to_bottom(self) -> None:
        """
        Прокручивает чат вниз после добавления нового сообщения.
        """

        QTimer.singleShot(
            0,
            lambda: self.scroll_area.verticalScrollBar().setValue(
                self.scroll_area.verticalScrollBar().maximum()
            ),
        )