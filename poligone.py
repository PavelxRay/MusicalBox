import sys
import pymysql
from config import host, user, password, db_name
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QStackedWidget


class LoginWindow(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.setWindowTitle('Вход в аккаунт')
        self.setGeometry(100, 100, 800, 800)
        self.stacked_widget = stacked_widget

        # Создаем виджет QLabel для отображения фоновой картинки
        self.background_label = QLabel(self)
        pixmap = QPixmap('fon3.jpg')  # Укажите путь к вашей фоновой картинке
        self.background_label.setPixmap(pixmap)
        self.background_label.setGeometry(0, 0, self.width(), self.height())

        self.login_label = QLabel('Логин:', self)
        self.login_input = QLineEdit(self)

        self.password_label = QLabel('Пароль:', self)
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)

        self.login_button = QPushButton('Войти', self)
        self.register_button = QPushButton('Зарегистрироваться', self)

        layout = QVBoxLayout()
        layout.addStretch()

        input_layout = QVBoxLayout()
        input_layout.addWidget(self.login_label)
        input_layout.addWidget(self.login_input)
        input_layout.addWidget(self.password_label)
        input_layout.addWidget(self.password_input)

        buttons_layout = QHBoxLayout()
        buttons_layout.addStretch()
        buttons_layout.addWidget(self.login_button)
        buttons_layout.addWidget(self.register_button)

        hlayout = QHBoxLayout()
        hlayout.addStretch()
        hlayout.addLayout(input_layout)
        hlayout.addStretch()

        layout.addLayout(hlayout)
        layout.addLayout(buttons_layout)
        layout.addStretch()

        self.setLayout(layout)

        self.login_button.clicked.connect(self.login)
        self.register_button.clicked.connect(self.register)

    def login(self):
        username = self.login_input.text()
        password1 = self.password_input.text()
        # Проверка логина и пароля в базе данных
        try:
            # Подключение к базе данных
            connection = pymysql.connect(
                host=host,
                user=user,
                password=password,
                database=db_name
            )

            # Создание объекта курсора
            cursor = connection.cursor()

            # Выполнение SQL-запроса для проверки логина и пароля
            query = "SELECT * FROM users WHERE Login=%s AND Password=%s"
            cursor.execute(query, (username, password1))

            # Получение результата запроса
            result = cursor.fetchone()

            if result:
                self.stacked_widget.setCurrentIndex(1)  # Переключение на индекс главного окна
            else:
                self.show_error_message("Неверный логин или пароль.")

            cursor.close()
            connection.close()

        except pymysql.Error as e:
            print(f"Ошибка при подключении к базе данных: {e}")

    def register(self):
        self.stacked_widget.setCurrentIndex(2)  # Переключение на индекс окна регистрации


class MainWindow(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.setWindowTitle('Главная страница')
        self.setGeometry(100, 100, 800, 800)
        self.stacked_widget = stacked_widget

        self.label = QLabel('Добро пожаловать!', self)
        self.logout_button = QPushButton('Выйти', self)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.logout_button)
        self.setLayout(layout)

        self.logout_button.clicked.connect(self.logout)

    def logout(self):
        self.stacked_widget.setCurrentIndex(0)  # Переключение на индекс окна входа


class RegistrationWindow(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.setWindowTitle('Регистрация')
        self.setGeometry(100, 100, 800, 800)
        self.stacked_widget = stacked_widget

        self.register_label = QLabel('Регистрация', self)

        self.mail_label = QLabel('e-mail:', self)
        self.mail_input = QLineEdit(self)

        self.Name_label = QLabel('Имя:', self)
        self.Name_input = QLineEdit(self)

        self.Surname_label = QLabel('Фамилия:', self)
        self.Surname_input = QLineEdit(self)

        self.username_label = QLabel('Логин:', self)
        self.username_input = QLineEdit(self)

        self.password_label = QLabel('Пароль:', self)
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)

        self.confirm_password_label = QLabel('Подтвердите пароль:', self)
        self.confirm_password_input = QLineEdit(self)
        self.confirm_password_input.setEchoMode(QLineEdit.Password)

        self.register_button = QPushButton('Зарегистрироваться', self)
        self.back_button = QPushButton('Назад', self)

        layout = QVBoxLayout()
        layout.addStretch()
        layout.addWidget(self.register_label)
        layout.addWidget(self.mail_label)
        layout.addWidget(self.mail_input)
        layout.addWidget(self.Name_label)
        layout.addWidget(self.Name_input)
        layout.addWidget(self.Surname_label)
        layout.addWidget(self.Surname_input)
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.confirm_password_label)
        layout.addWidget(self.confirm_password_input)
        layout.addWidget(self.register_button)
        layout.addWidget(self.back_button)
        layout.addStretch()

        self.setLayout(layout)

        self.register_button.clicked.connect(self.register)
        self.back_button.clicked.connect(self.back)

    def register(self):
        username = self.username_input.text()
        password1 = self.password_input.text()
        mail = self.mail_input.text()
        Name = self.Name_input.text()
        Surname = self.Surname_input.text()
        password2 = self.confirm_password_input.text()

        if password1 != password2:
            self.show_error_message("Пароли не совпадают.")
            return

        try:
            # Подключение к базе данных
            connection = pymysql.connect(
                host=host,
                user=user,
                password=password,
                database=db_name
            )

            # Создание объекта курсора
            cursor = connection.cursor()

            # Проверка, что логин не занят
            query = "SELECT * FROM users WHERE Login=%s"
            cursor.execute(query, (username,))
            result = cursor.fetchone()

            if result:
                self.show_error_message("Логин уже занят.")
                cursor.close()
                connection.close()
                return

            # Вставка нового пользователя в базу данных
            query = "INSERT INTO users (Login, Password, e-mail, Name, Surname) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, (username, password1, mail, Name, Surname))
            connection.commit()

            self.show_message("Регистрация прошла успешно.")

            cursor.close()
            connection.close()

            self.stacked_widget.setCurrentIndex(0)  # Переключение на индекс окна входа

        except pymysql.Error as e:
            print(f"Ошибка при подключении к базе данных: {e}")

    def back(self):
        self.stacked_widget.setCurrentIndex(0)  # Переключение на индекс окна входа

    def show_error_message(self, message):
        # Отображение сообщения об ошибке
        # Здесь вы можете использовать QMessageBox или другой способ показа сообщения
        print(f"Ошибка: {message}")

    def show_message(self, message):
        # Отображение обычного сообщения
        # Здесь вы можете использовать QMessageBox или другой способ показа сообщения
        print(f"Сообщение: {message}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    stacked_widget = QStackedWidget()

    login_window = LoginWindow(stacked_widget)
    main_window = MainWindow(stacked_widget)
    registration_window = RegistrationWindow(stacked_widget)

    stacked_widget.addWidget(login_window)
    stacked_widget.addWidget(main_window)
    stacked_widget.addWidget(registration_window)

    stacked_widget.setCurrentIndex(0)  # Установка начального индекса окна входа

    stacked_widget.show()

    sys.exit(app.exec_())
