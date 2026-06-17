from app.config.windows import CARD_ALPHA

OVERLAY_STYLE = f"""
    QWidget#overlayCard {{
        background-color: rgba(32, 32, 32, {CARD_ALPHA});
        border-radius: 22px;
        border: 1px solid rgba(255, 255, 255, 45);
    }}

    QWidget#sidebar {{
        background-color: rgba(255, 255, 255, 18);
        border-radius: 14px;
    }}

    QWidget#page {{
        background-color: rgba(255, 255, 255, 12);
        border-radius: 14px;
    }}

    QScrollArea#chatScrollArea {{
        background: transparent;
        border: none;
    }}

    QWidget#userBubble {{
        background-color: rgba(0, 120, 215, 210);
        border-radius: 14px;
    }}

    QWidget#assistantBubble {{
        background-color: rgba(68, 18, 74, 210);
        border-radius: 14px;
    }}

    TitleLabel {{
        color: white;
    }}

    BodyLabel {{
        color: rgba(255, 255, 255, 225);
        font-size: 14px;
    }}

    QLineEdit {{
        background-color: rgba(255, 255, 255, 30);
        color: white;
        border: 1px solid rgba(255, 255, 255, 45);
        border-radius: 10px;
        padding: 8px 10px;
    }}

    QLineEdit::placeholder {{
        color: rgba(255, 255, 255, 120);
    }}
    
    QWidget#settingsContainer {{
        background: transparent;
    }}

    QWidget#settingValue {{
        background-color: rgba(87, 11, 97, 45);
        border-radius: 12px;
    }}

    QWidget#settingValue:hover {{
        background-color: rgba(87, 11, 97, 70);
    }}

    BodyLabel#settingsGroupTitle {{
        color: rgba(255, 255, 255, 230);
        font-size: 14px;
        font-weight: 600;
        padding-top: 4px;
        padding-bottom: 4px;
    }}

    QScrollArea#SettingsScrollArea {{
        background: transparent;
        border: none;
    }}

    QScrollArea#SettingsScrollArea::viewport {{
        background: transparent;
    }}

    QLineEdit {{
        background-color: rgba(255, 255, 255, 30);
        color: white;
        border: 1px solid rgba(255, 255, 255, 45);
        border-radius: 10px;
        padding: 4px 8px;
    }}

    QLineEdit::placeholder {{
        color: rgba(255, 255, 255, 120);
    }}
"""