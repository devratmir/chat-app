import sqlite3
if __name__ != "__main__":
    from auth.exceptions import Exceptions
    import auth.users as users

else:
    from exceptions import Exceptions
    import users

conn = sqlite3.connect("auth/users.db")


cursor = conn.cursor()

def user_exists(username) -> bool:
    # Check username is not taken
    cursor.execute("SELECT * FROM USERS WHERE username = ?", (username,))
    result = cursor.fetchone()
    return bool(result)

def create_user(username, password) -> None:
    if user_exists(username):
        raise Exceptions.NameTakenError(f"Username {username} is already taken.")
    
    cursor.execute("INSERT INTO USERS (username, password) VALUES (?, ?)", (username, password))
    conn.commit()

def user_info(username: str) -> users.User:
    if not user_exists(username):
        raise Exceptions.UnknownUserError(username)
    
    cursor.execute("SELECT * from USERS where username = ?", (username,))

    user = cursor.fetchone()
    return users.User(*user)

def update_user(username: str, details: users.User):
    """Update username/password of a user. ID cannot be changed."""
    if not user_exists(username):
        raise Exceptions.UnknownUserError(username)
    
    if user_exists(details.username):
        raise Exceptions.NameTakenError(username)
    
    cursor.execute("UPDATE USERS SET username = ?, password = ? WHERE username = ?", (details.username, details.password, username))
    conn.commit()

def remove_user(username: str):
    if not user_exists(username):
        raise Exceptions.UnknownUserError(username)

    cursor.execute("DELETE FROM USERS WHERE username = ?", (username,))
    conn.commit()

def get_users(log=False) -> list:
    """Inadvisable to use outside of testing."""
    cursor.execute("SELECT id, username FROM users")
    result = cursor.fetchall()
    if not log:
        return result
    
    with open("user_data.txt", "w") as userdata:
        userdata.write("-- USER DATA --\n")
        userdata.write("| ID | USERNAME |\n")
        for row in result:
            for value in row:
                userdata.write(f"| {value} ")
            
            userdata.write("\n")

    return "user_data.txt"


def dev_ishell():
    try:
        while True:
            user = input(">>> ")
            try:
                print(eval(user))

            except:
                try:
                    print(cursor.execute(user))
                    try:
                        conn.commit()
                    except:
                        pass
                    print(cursor.fetchall())

                except:
                    print("Unknown command.")

    except KeyboardInterrupt:
        return

def db_exit():
    """Clean-up function. Must be called every time program finishes execution."""
    conn.close()

del sqlite3