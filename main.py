import sys

from PySide6.QtWidgets import QApplication
from qfluentwidgets import Theme, setTheme

from app.utils import start_up




def main() -> int:
    print("Initializing settings...")
    start_up._init_path()

    from app.config.windows import APP_NAME
    from app.services.notification import NotificationService
    from app.ui.windows.overlay_window import OverlayWindow

    app = QApplication(sys.argv)
    app.setApplicationName(APP_NAME)

    # Пока оставляем False, чтобы окно не закрывалось само из-за особенностей оверлея
    app.setQuitOnLastWindowClosed(False)

    setTheme(Theme.DARK)

    notification_service = NotificationService(app)

    window = OverlayWindow(notification_service=notification_service)

    # Держим ссылки, чтобы Python не удалил объекты
    app.window = window
    app.notification_service = notification_service

    window.show()

    return app.exec()


if __name__ == "__main__":
    sys.exit(main())