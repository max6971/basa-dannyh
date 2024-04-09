class User:
    def __init__(self, user_id, name, access_level='user'):
        self.user_id = user_id
        self.name = name
        self.access_level = access_level

    def __repr__(self):
        return f"{self.user_id}: {self.name} ({self.access_level})"


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name, 'admin')

    def add_user(self, users_list, user):
        users_list.append(user)
        print(f"Пользователь {user.name} добавлен.")

    def remove_user(self, users_list, user_id):
        for i, user in enumerate(users_list):
            if user.user_id == user_id:
                del users_list[i]
                print(f"Пользователь с ID {user_id} удален.")
                return
        print("Пользователь не найден.")


def main():
    users = []
    admin = Admin("A100", "Admin")

    while True:
        action = input("Выберите действие: добавить (add), удалить (remove), показать (show), выход (exit): ")
        if action == "add":
            user_id = input("Введите ID пользователя: ")
            name = input("Введите имя пользователя: ")
            access_level = input("Введите уровень доступа (user/admin): ")

            if access_level == "admin":
                new_user = Admin(user_id, name)
            else:
                new_user = User(user_id, name)

            admin.add_user(users, new_user)

        elif action == "remove":
            remove_id = input("Введите ID пользователя для удаления: ")
            admin.remove_user(users, remove_id)

        elif action == "show":
            print("Список пользователей:")
            for user in users:
                print(user)

        elif action == "exit":
            print("Выход.")
            break
        else:
            print("Неизвестное действие.")


if __name__ == "__main__":
    main()