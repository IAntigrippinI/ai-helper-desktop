from PySide6.QtCore import Qt, QPoint
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QStackedWidget,
)

from qfluentwidgets import (
    CardWidget,
    TitleLabel,
    BodyLabel,
    PrimaryPushButton,
    TransparentPushButton,
)

from app.config.windows import (
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    WINDOW_TITLE,
    TITLE_TEXT,
    DESCRIPTION_TEXT,
    APP_VERSION
)
from app.services.notification import NotificationService
from app.ui.styles.overlay_style import OVERLAY_STYLE
from app.ui.widgets.section_button import create_section_button


class OverlayWindow(QWidget):
    def __init__(self, notification_service: NotificationService):
        super().__init__()

        self.notification_service = notification_service

        self._drag_position = QPoint()
        self.section_buttons: list[TransparentPushButton] = []

        self.setWindowTitle(WINDOW_TITLE)

        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint
            | Qt.WindowType.WindowStaysOnTopHint
        )

        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.resize(WINDOW_WIDTH, WINDOW_HEIGHT)

        self._init_ui()
        self.setStyleSheet(OVERLAY_STYLE)

    def _init_ui(self) -> None:
        root_layout = QVBoxLayout(self)
        root_layout.setContentsMargins(12, 12, 12, 12)

        card = CardWidget(self)
        card.setObjectName("overlayCard")

        card_layout = QVBoxLayout(card)
        card_layout.setContentsMargins(22, 18, 22, 18)
        card_layout.setSpacing(14)

        header_layout = self._create_header()
        content_layout = self._create_content()
        footer_layout = self._create_footer()

        card_layout.addLayout(header_layout)
        card_layout.addLayout(content_layout)
        card_layout.addLayout(footer_layout)

        root_layout.addWidget(card)

    def _create_header(self) -> QHBoxLayout:
        header_layout = QHBoxLayout()

        title = TitleLabel(TITLE_TEXT)

        minimize_button = TransparentPushButton("—")
        minimize_button.setFixedWidth(42)
        minimize_button.clicked.connect(self.showMinimized)

        close_button = TransparentPushButton("✕")
        close_button.setFixedWidth(42)
        close_button.clicked.connect(self.quit_app)

        header_layout.addWidget(title)
        header_layout.addStretch()
        header_layout.addWidget(minimize_button)
        header_layout.addWidget(close_button)

        return header_layout


    def _create_footer(self) -> QHBoxLayout:
        footer_layout = QHBoxLayout()

        version_label = BodyLabel(f"v. {APP_VERSION}")
        version_label.setAlignment(Qt.AlignmentFlag.AlignRight)

        footer_layout.addWidget(version_label)
        return footer_layout

    def _create_content(self) -> QHBoxLayout:
        content_layout = QHBoxLayout()
        content_layout.setSpacing(14)

        self.sidebar = QWidget()
        self.sidebar.setObjectName("sidebar")

        sidebar_layout = QVBoxLayout(self.sidebar)
        sidebar_layout.setContentsMargins(10, 10, 10, 10)
        sidebar_layout.setSpacing(8)

        self.pages = QStackedWidget()

        # Добавляем разделы
        self._add_section(
            title="Главная",
            page=self._create_home_page(),
            sidebar_layout=sidebar_layout,
        )

        self._add_section(
            title="ИИ",
            page=self._create_ai_page(),
            sidebar_layout=sidebar_layout,
        )

        self._add_section(
            title="Настройки",
            page=self._create_settings_page(),
            sidebar_layout=sidebar_layout,
        )

        sidebar_layout.addStretch()

        content_layout.addWidget(self.sidebar, 1)
        content_layout.addWidget(self.pages, 3)

        # Выбираем первый раздел по умолчанию
        self._set_active_section(0)

        return content_layout

    def _add_section(self, title: str, page: QWidget, sidebar_layout: QVBoxLayout) -> None:
        """
        Добавляет кнопку раздела и соответствующую страницу.
        """

        index = self.pages.addWidget(page)

        button = create_section_button(title)
        button.clicked.connect(lambda checked=False, i=index: self._set_active_section(i))

        self.section_buttons.append(button)
        sidebar_layout.addWidget(button)

    def _set_active_section(self, index: int) -> None:
        """
        Переключает активный раздел.
        """

        self.pages.setCurrentIndex(index)

        for button_index, button in enumerate(self.section_buttons):
            button.setChecked(button_index == index)

    def _create_home_page(self) -> QWidget:
        page = QWidget()
        page.setObjectName("page")

        layout = QVBoxLayout(page)
        layout.setContentsMargins(16, 14, 16, 14)
        layout.setSpacing(12)

        description = BodyLabel(DESCRIPTION_TEXT)

        notify_button = PrimaryPushButton("Показать уведомление")
        notify_button.clicked.connect(self._show_test_notification)

        layout.addWidget(description)
        layout.addWidget(notify_button)
        layout.addStretch()

        return page

    def _create_ai_page(self) -> QWidget:
        page = QWidget()
        page.setObjectName("page")

        layout = QVBoxLayout(page)
        layout.setContentsMargins(16, 14, 16, 14)
        layout.setSpacing(12)

        title = BodyLabel("Здесь потом будет раздел для работы с ИИ.")
        button = PrimaryPushButton("Тест ИИ-раздела")
        button.clicked.connect(
            lambda: self.notification_service.show_info(
                "ИИ-раздел",
                "Пока это просто тестовая кнопка.",
            )
        )

        layout.addWidget(title)
        layout.addWidget(button)
        layout.addStretch()

        return page

    def _create_settings_page(self) -> QWidget:
        page = QWidget()
        page.setObjectName("page")

        layout = QVBoxLayout(page)
        layout.setContentsMargins(16, 14, 16, 14)
        layout.setSpacing(12)

        title = BodyLabel("Здесь потом будут настройки приложения.")
        button = PrimaryPushButton("Показать warning")
        button.clicked.connect(
            lambda: self.notification_service.show_warning(
                "Настройки",
                "Это пример предупреждения.",
            )
        )

        layout.addWidget(title)
        layout.addWidget(button)
        layout.addStretch()

        return page

    def _show_test_notification(self) -> None:
        """
        Тестовое уведомление Windows.
        """

        self.notification_service.show_info(
            title=WINDOW_TITLE,
            message="Разработка идет...",
        )

    def quit_app(self) -> None:
        app = QApplication.instance()

        if app is not None:
            app.quit()

    def mousePressEvent(self, event) -> None:
        """
        Запоминаем позицию мыши при нажатии,
        чтобы можно было перетаскивать окно.
        """

        if event.button() == Qt.MouseButton.LeftButton:
            self._drag_position = (
                event.globalPosition().toPoint()
                - self.frameGeometry().topLeft()
            )
            event.accept()

    def mouseMoveEvent(self, event) -> None:
        """
        Перетаскиваем окно мышкой.
        """

        if event.buttons() == Qt.MouseButton.LeftButton:
            self.move(event.globalPosition().toPoint() - self._drag_position)
            event.accept()