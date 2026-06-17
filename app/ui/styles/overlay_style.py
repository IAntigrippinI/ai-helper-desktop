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

    TitleLabel {{
        color: white;
    }}

    BodyLabel {{
        color: rgba(255, 255, 255, 215);
        font-size: 14px;
    }}

    SectionButton {{
        text-align: left;
        padding-left: 10px;
    }}
"""