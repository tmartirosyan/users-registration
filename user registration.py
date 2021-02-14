import os


class User:
    isRegistrated = False

    def __init__(self, name: str, surname: str, age: int, login: str, password: str):
        userInfo = {'name': name, 'surname': surname, 'age': age, 'login': login, 'password': password}
        path = os.environ['USERPROFILE'] + "\\Desktop\\"
        self.isRegistrated = self.Registrate(path, userInfo)

    def Registrate(self, path: str, info: dict) -> bool:
        if os.path.exists(path + f"{info['name']}--{info['surname']}"):
            print("Your are almost registrated...")
            return False
        path += f"{info['name']}--{info['surname']}"
        os.mkdir(path)
        with open(f"{path}\\info.txt", "w+") as file:
            file.write("=" * 30 + "\n")
            file.write(f"\tName: {info['name']}\n\tSurname: {info['surname']}\n\tAge: {info['age']}"
                       f"\n\tLogin: {info['login']}\n\tPassword: {info['password']}")
            file.write("\n" + ("=" * 30))
        print("You are registrated successfully")
        return True


def AppendNewUserInfoToData(data: list, path: str):
    with open(path + "\\users.txt", "a+") as usersFile:
        usersFile.write("=" * 30)
        for infoIndex in range(len(data)):
            usersFile.write("\n\t" + str(data[infoIndex]))
        usersFile.write("\n" + ("=" * 30) + "\n")


name = "Artyom"
surname = "Hakobyan"
age = 21
login = "arthakobyan@gmail.com"
password = "0000"
user = User(name, surname, age, login, password)
if user.isRegistrated:
    path = os.environ['USERPROFILE'] + "\\Desktop"
    if not os.path.exists(path + "\\DataUsers"):
        os.mkdir(path + "\\DataUsers")
    path += "\\DataUsers"
    AppendNewUserInfoToData([name, surname, age, login, password], path)