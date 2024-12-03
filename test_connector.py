import mysql.connector

def test_connection():
    try:
        print("Memulai koneksi ke database...")
        connection = mysql.connector.connect(
            host="localhost",
            user="root",          # Username MySQL default
            password="",          # Password default (kosong)
            database="crud_python"  # Ganti dengan nama database Anda
        )
        if connection.is_connected():
            print("Koneksi berhasil!")
            print(f"Info Server: {connection.get_server_info()}")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            connection.close()
            print("Koneksi ditutup.")

if __name__ == "__main__":
    test_connection()
