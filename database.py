from sqlite3 import connect

connection = connect('database.db')
cursor = connection.cursor()


def add_remainder(lst):
    cursor.execute("INSERT INTO reminders"
                   "(user_id, reminder, time)"
                   "VALUES (?, ?, ?);", lst)
    connection.commit()


def read_reminder():
    cursor.execute("SELECT * FROM reminders")
    return cursor.fetchall()


def del_reminder(value):
    cursor.execute("DELETE FROM reminders WHERE id== ?", (value,))
    connection.commit()


def read_from_database():
    cursor.execute('SELECT time, reminder, user_id, id FROM reminders')
    connection.commit()
    return cursor.fetchall()


if __name__ == '__main__':
    # x = read_reminder()
    # print(x)
    y = read_from_database()
    print(y)
