import mysql.connector

# Fungsi untuk membuat koneksi
def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="crud_python"
    )

# CREATE: Menambah data pengguna baru
def create_user(name, email, age):
    connection = create_connection()
    cursor = connection.cursor()
    query = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, email, age))
    connection.commit()
    print(f"User {name} added successfully!")
    cursor.close()
    connection.close()

# READ: Menampilkan semua data pengguna
def read_users():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    for user in users:
        print(user)
    cursor.close()
    connection.close()

# UPDATE: Mengupdate data pengguna berdasarkan ID
def update_user(user_id, name, email, age):
    connection = create_connection()
    cursor = connection.cursor()
    query = "UPDATE users SET name = %s, email = %s, age = %s WHERE id = %s"
    cursor.execute(query, (name, email, age, user_id))
    connection.commit()
    print(f"User with ID {user_id} updated successfully!")
    cursor.close()
    connection.close()

# DELETE: Menghapus data pengguna berdasarkan ID
def delete_user(user_id):
    connection = create_connection()
    cursor = connection.cursor()
    query = "DELETE FROM users WHERE id = %s"
    cursor.execute(query, (user_id,))
    connection.commit()
    print(f"User with ID {user_id} deleted successfully!")
    cursor.close()
    connection.close()

# Menu utama untuk memilih operasi CRUD
def menu():
    while True:
        print("\nCRUD Application")
        print("1. Add User")
        print("2. View Users")
        print("3. Update User")
        print("4. Delete User")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            email = input("Enter email: ")
            age = int(input("Enter age: "))
            create_user(name, email, age)

        elif choice == "2":
            read_users()

        elif choice == "3":
            user_id = int(input("Enter user ID to update: "))
            name = input("Enter new name: ")
            email = input("Enter new email: ")
            age = int(input("Enter new age: "))
            update_user(user_id, name, email, age)

        elif choice == "4":
            user_id = int(input("Enter user ID to delete: "))
            delete_user(user_id)

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    menu()
