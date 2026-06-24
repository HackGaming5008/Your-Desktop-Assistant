import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QTextEdit, QLineEdit, QPushButton, QListWidget,
    QLabel, QFrame
)
from PyQt6.QtCore import Qt


class ChatWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Chat Application")
        self.resize(1000, 700)

        main_layout = QHBoxLayout(self)

        # =========================
        # Sidebar
        # =========================
        sidebar = QFrame()
        sidebar.setFixedWidth(250)

        sidebar_layout = QVBoxLayout(sidebar)

        title = QLabel("Chats")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.chat_list = QListWidget()
        self.chat_list.addItems([
            "General",
            "Friends",
            "Work",
            "AI Assistant"
        ])

        new_chat_btn = QPushButton("New Chat")
        new_chat_btn.setCursor(Qt.CursorShape.PointingHandCursor)

        sidebar_layout.addWidget(title)
        sidebar_layout.addWidget(self.chat_list)
        sidebar_layout.addWidget(new_chat_btn)

        # =========================
        # Chat Area
        # =========================
        chat_container = QFrame()
        chat_layout = QVBoxLayout(chat_container)

        header = QLabel("General Chat")
        header.setFixedHeight(40)

        self.chat_display = QTextEdit()
        self.chat_display.setReadOnly(True)

        self.chat_display.append("Alice: Hello!")
        self.chat_display.append("Bob: Hi there!")

        # Message Input
        input_layout = QHBoxLayout()

        self.message_input = QLineEdit()
        self.message_input.setPlaceholderText("Type a message...")

        send_btn = QPushButton("Send")
        send_btn.setCursor(Qt.CursorShape.PointingHandCursor)

        input_layout.addWidget(self.message_input)
        input_layout.addWidget(send_btn)

        chat_layout.addWidget(header)
        chat_layout.addWidget(self.chat_display)
        chat_layout.addLayout(input_layout)

        # =========================
        # Add to Main Layout
        # =========================
        main_layout.addWidget(sidebar)
        main_layout.addWidget(chat_container)

        # =========================
        # Styling
        # =========================
        self.setStyleSheet("""
            QWidget {
                background-color: #202123;
                color: white;
                font-size: 14px;
            }

            QListWidget {
                background-color: #2b2d31;
                border: none;
                padding: 5px;
            }

            QTextEdit {
                background-color: #2b2d31;
                border: none;
                padding: 10px;
            }

            QLineEdit {
                background-color: #2b2d31;
                border: none;
                padding: 10px;
                border-radius: 8px;
            }

            QPushButton {
                background-color: white;
                color: black;
                border: none;
                padding: 10px;
                border-radius: 8px;
            }

            QPushButton:hover {
                background-color: #c4c4c4;
            }

            QLabel {
                font-weight: bold;
            }
        """)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = ChatWindow()
    window.show()

    sys.exit(app.exec())