import sys

from PySide6.QtWidgets import QApplication
from qfluentwidgets import Theme, setTheme

from app.overlay_window import OverlayWindow


def main() -> int:
    app = QApplication(sys.argv)

    setTheme(Theme.DARK)

    window = OverlayWindow()
    window.show()

    return app.exec()


if __name__ == "__main__":
    sys.exit(main())