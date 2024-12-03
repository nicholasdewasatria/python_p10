import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Fungsi untuk membuat koneksi ke database
def create_connection():
    # Membuat koneksi ke database MySQL
    return mysql.connector.connect(
        host="localhost",  # Ganti dengan host MySQL jika diperlukan
        user="root",       # Ganti dengan user MySQL Anda
        password="",       # Ganti dengan password MySQL Anda
        database="crud_python"  # Ganti dengan nama database yang Anda gunakan
    )

# Fungsi untuk menambah data pengguna
def add_user():
    # Mengambil input dari kolom yang ada di GUI
    name = entry_name.get()
    email = entry_email.get()
    age = entry_age.get()

    # Cek jika semua input sudah diisi
    if name and email and age:
        # Membuat koneksi ke database
        connection = create_connection()
        cursor = connection.cursor()
        # Query untuk menambah data pengguna
        query = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"
        cursor.execute(query, (name, email, age))  # Eksekusi query
        connection.commit()  # Menyimpan perubahan ke database
        cursor.close()
        connection.close()
        # Menampilkan pesan sukses
        messagebox.showinfo("Success", f"User {name} added successfully!")
        clear_fields()  # Menghapus kolom input setelah menambah data
        listbox_users.delete(0, tk.END)  # Menghapus listbox sebelum menampilkan ulang
        show_users()  # Menampilkan ulang data pengguna
    else:
        # Menampilkan pesan peringatan jika ada kolom yang belum diisi
        messagebox.showwarning("Input Error", "Please fill all fields.")

# Fungsi untuk menampilkan semua data pengguna
def show_users():
    # Membuat koneksi ke database
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")  # Mengambil semua data dari tabel users
    users = cursor.fetchall()  # Menyimpan hasil query dalam variabel users

    # Menampilkan data pengguna ke dalam listbox
    for row in users:
        listbox_users.insert(tk.END, f"ID: {row[0]}, Name: {row[1]}, Email: {row[2]}, Age: {row[3]}")

    cursor.close()
    connection.close()

# Fungsi untuk mengupdate data pengguna berdasarkan ID
def update_user():
    # Mengambil user yang dipilih dari listbox
    selected_user = listbox_users.curselection()
    if selected_user:
        # Mengambil ID pengguna yang dipilih
        user_id = listbox_users.get(selected_user).split(",")[0].split(":")[1].strip()
        name = entry_name.get()
        email = entry_email.get()
        age = entry_age.get()

        # Cek jika semua input sudah diisi
        if name and email and age:
            # Membuat koneksi ke database
            connection = create_connection()
            cursor = connection.cursor()
            # Query untuk mengupdate data pengguna
            query = "UPDATE users SET name = %s, email = %s, age = %s WHERE id = %s"
            cursor.execute(query, (name, email, age, user_id))  # Eksekusi query
            connection.commit()  # Menyimpan perubahan ke database
            cursor.close()
            connection.close()
            # Menampilkan pesan sukses
            messagebox.showinfo("Success", f"User {name} updated successfully!")
            clear_fields()  # Menghapus kolom input setelah mengupdate data
            listbox_users.delete(0, tk.END)  # Menghapus listbox sebelum menampilkan ulang
            show_users()  # Menampilkan ulang data pengguna
        else:
            # Menampilkan pesan peringatan jika ada kolom yang belum diisi
            messagebox.showwarning("Input Error", "Please fill all fields.")
    else:
        # Menampilkan pesan peringatan jika tidak ada pengguna yang dipilih
        messagebox.showwarning("Selection Error", "Please select a user to update.")

# Fungsi untuk menghapus data pengguna berdasarkan ID
def delete_user():
    # Mengambil user yang dipilih dari listbox
    selected_user = listbox_users.curselection()
    if selected_user:
        # Mengambil ID pengguna yang dipilih
        user_id = listbox_users.get(selected_user).split(",")[0].split(":")[1].strip()

        # Membuat koneksi ke database
        connection = create_connection()
        cursor = connection.cursor()
        # Query untuk menghapus data pengguna
        query = "DELETE FROM users WHERE id = %s"
        cursor.execute(query, (user_id,))  # Eksekusi query
        connection.commit()  # Menyimpan perubahan ke database
        cursor.close()
        connection.close()
        # Menampilkan pesan sukses
        messagebox.showinfo("Success", f"User with ID {user_id} deleted successfully!")
        listbox_users.delete(0, tk.END)  # Menghapus listbox sebelum menampilkan ulang
        show_users()  # Menampilkan ulang data pengguna
    else:
        # Menampilkan pesan peringatan jika tidak ada pengguna yang dipilih
        messagebox.showwarning("Selection Error", "Please select a user to delete.")

# Fungsi untuk menghapus isi kolom input
def clear_fields():
    # Menghapus teks di kolom input
    entry_name.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_age.delete(0, tk.END)

# Fungsi utama untuk membuat tampilan GUI
def create_gui():
    global entry_name, entry_email, entry_age, listbox_users

    # Setup jendela aplikasi
    root = tk.Tk()
    root.title("CRUD Application with MySQL")
    root.geometry("600x500")
    root.config(bg="#f5f5f5")  # Warna latar belakang

    # Gaya font
    font_style = ("Arial", 12)

    # Frame untuk kolom input
    frame_input = tk.Frame(root, bg="#f5f5f5")
    frame_input.pack(pady=10)

    # Kolom untuk input Nama
    tk.Label(frame_input, text="Name:", font=font_style, bg="#f5f5f5").grid(row=0, column=0, padx=10, pady=5)
    entry_name = tk.Entry(frame_input, font=font_style, width=30)
    entry_name.grid(row=0, column=1, padx=10, pady=5)

    # Kolom untuk input Email
    tk.Label(frame_input, text="Email:", font=font_style, bg="#f5f5f5").grid(row=1, column=0, padx=10, pady=5)
    entry_email = tk.Entry(frame_input, font=font_style, width=30)
    entry_email.grid(row=1, column=1, padx=10, pady=5)

    # Kolom untuk input Umur
    tk.Label(frame_input, text="Age:", font=font_style, bg="#f5f5f5").grid(row=2, column=0, padx=10, pady=5)
    entry_age = tk.Entry(frame_input, font=font_style, width=30)
    entry_age.grid(row=2, column=1, padx=10, pady=5)

    # Frame untuk tombol CRUD
    frame_buttons = tk.Frame(root, bg="#f5f5f5")
    frame_buttons.pack(pady=10)

    # Tombol untuk operasi CRUD
    tk.Button(frame_buttons, text="Add User", font=font_style, bg="#4CAF50", fg="white", command=add_user, width=15).grid(row=0, column=0, padx=10, pady=5)
    tk.Button(frame_buttons, text="Update User", font=font_style, bg="#FF9800", fg="white", command=update_user, width=15).grid(row=0, column=1, padx=10, pady=5)
    tk.Button(frame_buttons, text="Delete User", font=font_style, bg="#F44336", fg="white", command=delete_user, width=15).grid(row=0, column=2, padx=10, pady=5)

    # Listbox untuk menampilkan data pengguna dengan scrollbar
    listbox_frame = tk.Frame(root, bg="#f5f5f5")
    listbox_frame.pack(pady=10)

    listbox_users = tk.Listbox(listbox_frame, width=50, height=10, font=font_style)
    listbox_users.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Scrollbar untuk listbox
    scrollbar = tk.Scrollbar(listbox_frame, orient="vertical", command=listbox_users.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    listbox_users.config(yscrollcommand=scrollbar.set)

    # Menampilkan semua pengguna ketika aplikasi pertama kali dijalankan
    show_users()

    # Memulai loop GUI
    root.mainloop()

# Menjalankan aplikasi GUI
if __name__ == "__main__":
    create_gui()
