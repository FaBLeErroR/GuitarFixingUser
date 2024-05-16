from PySide6 import QtWidgets, QtSql


class Data:    
    def __init__(self):
        super(Data, self).__init__()
        self.create_connection()

    def create_connection(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('guitar.db')

        if not db.open():
            QtWidgets.QMessageBox.critical(None, "Cannot open database",
            "Click Cancel to exit.", QtWidgets.QMessageBox.Cancel)
            return False

        query = QtSql.QSqlQuery()
        

        query.exec('''CREATE TABLE IF NOT EXISTS Characteristic (
        characteristic_id INTEGER PRIMARY KEY AUTOINCREMENT,
        characteristic_name TEXT,
        min_acceptable_val REAL,
        max_acceptable_val REAL
        )''')

        query.exec('''CREATE TABLE IF NOT EXISTS Detail (
        detail_id INTEGER PRIMARY KEY AUTOINCREMENT,
        detail_name TEXT
        )''')
        
        query.exec('''CREATE TABLE IF NOT EXISTS Characteristic_Diagnostic (
        chara_diag_id INTEGER PRIMARY KEY AUTOINCREMENT,
        characteristic_id INTEGER,
        diagnostic_id INTEGER,
        repair_id INTEGER,
        characteristics_value_id INTEGER,
        FOREIGN KEY (characteristic_id) REFERENCES Characteristic(characteristic_id),
        FOREIGN KEY (characteristics_value_id) REFERENCES Characteristic_Value(characteristics_value_id),
        FOREIGN KEY (diagnostic_id) REFERENCES Diagnostic(diagnostic_id),
        FOREIGN KEY (repair_id) REFERENCES Repair(repair_id)
        )''')

        query.exec('''CREATE TABLE IF NOT EXISTS Diagnostic (
        diagnostic_id INTEGER PRIMARY KEY AUTOINCREMENT,
        diagnostic_name TEXT,
        min_value REAL,
        max_value REAL
        )''')

        query.exec('''CREATE TABLE IF NOT EXISTS Repair (
        repair_id INTEGER PRIMARY KEY AUTOINCREMENT,
        repair_name TEXT,
        action_id INTEGER,
        FOREIGN KEY (action_id) REFERENCES Action(action_id)
        )''')

        query.exec('''CREATE TABLE IF NOT EXISTS Action (
        action_id INTEGER PRIMARY KEY AUTOINCREMENT,
        action_name TEXT
        )''')
        return True

    def execute_query_with_params(self, sql_query, query_values=None):
        query = QtSql.QSqlQuery()
        query.prepare(sql_query)

        if query_values is not None:
            for query_value in query_values:
                query.addBindValue(query_value)

        query.exec()

        return query
    
    def get_total(self, column, tablice):
        sql_query = f"SELECT {column} FROM {tablice}"


        query = self.execute_query_with_params(sql_query, [])

        result_list = []
        query.first()
        result_list.append(query.value(0))
        while query.next():
            result_list.append(query.value(0))

        return result_list

    #choose diagnostic field
    def get_diagnostic(self):
        return self.get_total(column="diagnostic_name", tablice="Diagnostic")
    
    def get_repair(self, curent_diagnostic):
        sql_query = '''SELECT DISTINCT Repair.repair_name
                    FROM Repair
                    JOIN Characteristic_Diagnostic ON Repair.repair_id = Characteristic_Diagnostic.repair_id
                    JOIN Diagnostic ON Characteristic_Diagnostic.diagnostic_id = Diagnostic.diagnostic_id
                    WHERE Diagnostic.diagnostic_name = "''' + curent_diagnostic + '";'


        query = self.execute_query_with_params(sql_query, [])

        result_list = []
        query.first()
        result_list.append(query.value(0))
        while query.next():
            result_list.append(query.value(0))

        return result_list
    
    def is_float(self, element):
        #If you expect None to be passed:
        if element is None: 
            return False
        try:
            float(element)
            return True
        except ValueError:
            return False

    def get_diagnostic_by_table(self, characteristics):
        sql_query = ''
        print(characteristics[0][1])
        if self.is_float(characteristics[0][1]):
            value = float(characteristics[0][1])
            sql_query += f'''SELECT DISTINCT Diagnostic.diagnostic_name
                        FROM Diagnostic
                        JOIN Diagnostic_Values ON Diagnostic.diagnostic_id = Diagnostic_Values.diagnostic_id
                        WHERE (Diagnostic_Values.diagnostic_characteristic_value = '{characteristics[0][0]}' AND {value} > Diagnostic_Values.min_value AND {value} < Diagnostic_Values.max_value)'''
        else:
            sql_query += f'''SELECT DISTINCT Diagnostic.diagnostic_name
                        FROM Diagnostic
                        JOIN Diagnostic_Values ON Diagnostic.diagnostic_id = Diagnostic_Values.diagnostic_id
                        WHERE (Diagnostic_Values.diagnostic_characteristic_value = '{characteristics[0][0]}' AND Diagnostic_Values.diagnostic_value = '{characteristics[0][1]}')'''

        for i in range(1, len(characteristics)):
            if self.is_float(characteristics[i][1]):
                value = float(characteristics[i][1])
                sql_query += f''' OR (Diagnostic_Values.diagnostic_characteristic_value = '{characteristics[i][0]}' AND {value} > Diagnostic_Values.min_value AND {value} < Diagnostic_Values.max_value)'''
            else:
                sql_query += f''' OR (Diagnostic_Values.diagnostic_characteristic_value = '{characteristics[i][0]}' AND Diagnostic_Values.diagnostic_value = '{characteristics[i][1]}')'''

        print(sql_query)
        query = self.execute_query_with_params(sql_query, [])

        result_list = []
        query.first()
        result_list.append(query.value(0))
        while query.next():
            result_list.append(query.value(0))

        return result_list