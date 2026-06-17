from qfluentwidgets import TransparentPushButton


def create_section_button(text: str, parent=None) -> TransparentPushButton:
    """
    Создаёт кнопку раздела для бокового меню.
    """

    button = TransparentPushButton(parent=parent)
    button.setText(text)

    button.setCheckable(True)
    button.setFixedHeight(36)

    return button