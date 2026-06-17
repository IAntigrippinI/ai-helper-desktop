from PySide6.QtWidgets import QApplication, QSystemTrayIcon, QStyle


class NotificationService:
    """
    Сервис для отправки уведомлений Windows через системный трей.

    Важно:
    - объект QSystemTrayIcon нужно хранить в памяти;
    - если создать его внутри функции и не сохранить, уведомление может не появиться;
    - на Windows уведомления могут зависеть от настроек системы и режима "Не беспокоить".
    """

    def __init__(self, app: QApplication):
        self.app = app

        # Проверяем, доступен ли системный трей
        self.is_available = QSystemTrayIcon.isSystemTrayAvailable()

        # Берём стандартную системную иконку,
        # чтобы пока не подключать свой .ico файл
        icon = app.style().standardIcon(QStyle.StandardPixmap.SP_ComputerIcon)

        self.tray_icon = QSystemTrayIcon(icon)

        # Подсказка при наведении на иконку в трее
        self.tray_icon.setToolTip("Overlay App")

        # Без show() уведомления через showMessage() могут не отображаться
        self.tray_icon.show()

    def show_info(self, title: str, message: str, duration_ms: int = 4000) -> None:
        """
        Показать информационное уведомление.

        duration_ms — примерное время отображения уведомления.
        Windows может игнорировать это значение и показывать уведомление по своим правилам.
        """

        if not self.is_available:
            print("System tray is not available")
            return

        self.tray_icon.showMessage(
            title,
            message,
            QSystemTrayIcon.MessageIcon.Information,
            duration_ms,
        )

    def show_warning(self, title: str, message: str, duration_ms: int = 4000) -> None:
        """
        Показать предупреждение.
        """

        if not self.is_available:
            print("System tray is not available")
            return

        self.tray_icon.showMessage(
            title,
            message,
            QSystemTrayIcon.MessageIcon.Warning,
            duration_ms,
        )