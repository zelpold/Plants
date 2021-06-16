import pymysql
from config import bd_info


class DataBaseController:
    def __init__(self):
        try:
            self.connection = pymysql.connect(host=bd_info["host"], port=3306,
                                              user=bd_info["user"], password=bd_info["password"],
                                              db=bd_info["db"])
            self.cursor = self.connection.cursor()
            self.connection.close()
        except pymysql.Error as e:
            print(e)

    def get_plants(self, name=" ", category=" ", autor=" "):
        self.connect_database()
        flag = False
        q_string = "SELECT * From sorts"
        if name != " ":
            q_string += " WHERE name LIKE \'%" + name + "%\'"
            flag = True
        if category != " ":
            if flag:
                q_string += " AND category LIKE \'%" + category + "%\'"
            else:
                flag = True
                q_string += " WHERE category LIKE \'%" + category + "%\'"
        if autor != " ":
            if flag:
                q_string += " AND autor LIKE \'%" + autor + "%\'"
            else:
                q_string += " WHERE autor LIKE \'%" + autor + "%\'"
        self.cursor.execute(q_string)
        plants = self.cursor.fetchall()
        self.connect_close()
        return plants

    def get_cur_plants(self, name):
        self.connect_database()
        self.cursor.execute("SELECT * From sorts WHERE name = \'" + name + "\'")
        plant = self.cursor.fetchall()
        self.cursor.execute("SELECT insect From insects WHERE sort = \'" + name + "\'")
        insects = self.cursor.fetchall()
        self.cursor.execute("SELECT sick From sicks WHERE sort = \'" + name + "\'")
        sicks = self.cursor.fetchall()
        self.cursor.execute("SELECT parent From parents WHERE child = \'" + name + "\'")
        parents = self.cursor.fetchall()
        self.cursor.execute("SELECT child From parents WHERE parent = \'" + name + "\'")
        children = self.cursor.fetchall()
        self.cursor.execute("SELECT fond From fonds WHERE sort = \'" + name + "\'")
        fond = self.cursor.fetchall()
        self.connect_close()
        return plant[0], insects, sicks, parents, children, fond

    def get_worker(self, login, password):
        self.connect_database()
        self.cursor.execute("SELECT * From users WHERE login = \'" + login + "\' AND password = \'" + password + "\'")
        user = self.cursor.fetchall()
        self.connect_close()
        if user:
            return True
        else:
            return False

    def plant_exist(self, name):
        self.connect_database()
        self.cursor.execute("SELECT * From sorts WHERE name = \'" + name + "\'")
        plant = self.cursor.fetchall()
        self.connect_close()
        if plant:
            return True
        else:
            return False

    def delete_plant(self, name):
        self.connect_database()
        self.cursor.execute("DELETE From sorts WHERE name = \'" + name + "\'")
        self.connect_close()

    def update_data(self, name, category, autor, fruit, fruit_feature, frost_resistance):
        self.connect_database()
        self.cursor.execute("SELECT * FROM sorts WHERE name = \'"+name+"\'")
        exist = self.cursor.fetchall()
        if exist:
            self.cursor.execute("UPDATE sorts SET category = \'"+category + "\', autor = \'" + autor +
                                "\', fruit = \'" + fruit + "\', fruit_feature = \'" + fruit_feature +
                                "\', frost_resistance = \'" + frost_resistance + "\' WHERE name = \'"+name+"\'")
        else:
            self.cursor.execute("INSERT INTO sorts (name, category, autor, fruit, fruit_feature, frost_resistance)" +
                                "VALUES (\'" + name + "\', \'" + category + "\', \'" + autor + "\', \'" + fruit +
                                "\', \'" + fruit_feature + "\', \'" + frost_resistance + "\')")
        self.connect_close()

    def update_data_lists(self, name, insects, sicks, parents, children, fonds):
        self.connect_database()
        self.cursor.execute("DELETE From insects WHERE sort = \'" + name + "\'")
        for idx in range(0, insects.count()):
            self.cursor.execute("INSERT INTO insects (insect, sort) VALUES (\'" +
                                insects.item(idx).text()+"\', \'" + name + "\')")

        self.cursor.execute("DELETE From sicks WHERE sort = \'" + name + "\'")
        for idx in range(0, sicks.count()):
            self.cursor.execute("INSERT INTO sicks (sick, sort) VALUES (\'" +
                                sicks.item(idx).text()+"\', \'" + name + "\')")

        self.cursor.execute("DELETE From parents WHERE child = \'" + name + "\'")
        for idx in range(0, parents.count()):
            self.cursor.execute("INSERT INTO parents (parent, child) VALUES (\'" +
                                parents.item(idx).text() + "\', \'" + name + "\')")

        self.cursor.execute("DELETE From parents WHERE parent = \'" + name + "\'")
        for idx in range(0, children.count()):
            self.cursor.execute("INSERT INTO parents (parent, child) VALUES (\'" +
                                name + "\', \'" + children.item(idx).text() + "\')")

        self.cursor.execute("DELETE From fonds WHERE sort = \'" + name + "\'")
        for idx in range(0, fonds.count()):
            self.cursor.execute("INSERT INTO fonds (fond, sort) VALUES (\'" +
                                fonds.item(idx).text() + "\', \'" + name + "\')")

        self.connection.close()

    def connect_database(self):
        self.connection = pymysql.connect(host=bd_info["host"], port=3306,
                                          user=bd_info["user"], password=bd_info["password"],
                                          db=bd_info["db"], autocommit=True)
        self.cursor = self.connection.cursor()

    def connect_close(self):
        self.connection.close()
