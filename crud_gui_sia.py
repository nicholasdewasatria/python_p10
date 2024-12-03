import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Fungsi untuk membuat koneksi ke database
def create_connection():
    return mysql.connector.connect(
        host="localhost",  # Ganti dengan host MySQL jika diperlukan
        user="root",       # Ganti dengan user MySQL Anda
        password="",       # Ganti dengan password MySQL Anda
        database="crud_sia"  # Ganti dengan nama database yang Anda gunakan
    )

# Fungsi untuk menambah data mahasiswa
def add_student():
    npm = entry_npm.get()
    name = entry_name.get()
    program = entry_program.get()
    faculty = entry_faculty.get()

    if npm and name and program and faculty:
        connection = create_connection()
        cursor = connection.cursor()
        
        # Cek apakah NPM sudah ada di database
        cursor.execute("SELECT * FROM students WHERE npm = %s", (npm,))
        if cursor.fetchone():
            messagebox.showwarning("Input Error", "NPM already exists. Please use a different NPM.")
        else:
            query = "INSERT INTO students (npm, name, program, faculty) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (npm, name, program, faculty))
            connection.commit()
            messagebox.showinfo("Success", f"Student {name} added successfully!")
        
        cursor.close()
        connection.close()
        clear_fields()
        listbox_students.delete(0, tk.END)
        show_students()
    else:
        messagebox.showwarning("Input Error", "Please fill all fields.")

# Fungsi untuk menampilkan semua data mahasiswa
def show_students():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    listbox_students.delete(0, tk.END)  # Clear listbox before showing new data
    for row in students:
        listbox_students.insert(tk.END, f"NPM: {row[0]}, Name: {row[1]}, Program: {row[2]}, Faculty: {row[3]}")

    cursor.close()
    connection.close()

# Fungsi untuk mengupdate data mahasiswa berdasarkan NPM
def update_student(event):
    selected_student = listbox_students.curselection()
    if selected_student:
        student_info = listbox_students.get(selected_student).split(", ")
        npm = student_info[0].split(": ")[1].strip()
        name = student_info[1].split(": ")[1].strip()
        program = student_info[2].split(": ")[1].strip()
        faculty = student_info[3].split(": ")[1].strip()

        entry_npm.delete(0, tk.END)
        entry_npm.insert(0, npm)
        entry_name.delete(0, tk.END)
        entry_name.insert(0, name)
        entry_program.delete(0, tk.END)
        entry_program.insert(0, program)
        entry_faculty.delete(0, tk.END)
        entry_faculty.insert(0, faculty)

# Fungsi untuk mengupdate data mahasiswa di database
def update_student_data():
    npm = entry_npm.get()
    name = entry_name.get()
    program = entry_program.get()
    faculty = entry_faculty.get()

    if npm and name and program and faculty:
        connection = create_connection()
        cursor = connection.cursor()

        # Mengambil NPM yang lama dari data yang dipilih
        selected_student = listbox_students.curselection()
        if selected_student:
            old_student_info = listbox_students.get(selected_student).split(", ")
            old_npm = old_student_info[0].split(": ")[1].strip()

            # Cek jika NPM yang baru sudah ada di database dan bukan NPM yang sama
            if npm != old_npm:
                cursor.execute("SELECT * FROM students WHERE npm = %s", (npm,))
                if cursor.fetchone():
                    messagebox.showwarning("Input Error", "NPM already exists. Please use a different NPM.")
                    cursor.close()
                    connection.close()
                    return

        # Query untuk mengupdate data mahasiswa
        query = "UPDATE students SET name = %s, program = %s, faculty = %s WHERE npm = %s"
        cursor.execute(query, (name, program, faculty, npm))  # Menggunakan NPM yang lama untuk update
        connection.commit()
        cursor.close()
        connection.close()
       
        messagebox.showinfo("Success", f"Student {name} updated successfully!")
        clear_fields()
        listbox_students.delete(0, tk.END)
        show_students()
    else:
        messagebox.showwarning("Input Error", "Please fill all fields.")

# Fungsi untuk menghapus data mahasiswa berdasarkan NPM
def delete_student():
    selected_student = listbox_students.curselection()
    if selected_student:
        student_info = listbox_students.get(selected_student).split(", ")
        npm = student_info[0].split(": ")[1].strip()

        connection = create_connection()
        cursor = connection.cursor()
        query = "DELETE FROM students WHERE npm = %s"
        cursor.execute(query, (npm,))
        connection.commit()
        cursor.close()
        connection.close()
        messagebox.showinfo("Success", f"Student with NPM {npm} deleted successfully!")
        listbox_students.delete(0, tk.END)
        show_students()
    else:
        messagebox.showwarning("Selection Error", "Please select a student to delete.")

# Fungsi untuk menghapus isi kolom input
def clear_fields():
    entry_npm.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_program.delete(0, tk.END)
    entry_faculty.delete(0, tk.END)

# Fungsi utama untuk membuat tampilan GUI
def create_gui():
    global entry_npm, entry_name, entry_program, entry_faculty, listbox_students

    root = tk.Tk()
    root.title("CRUD Application with MySQL")
    root.geometry("600x500")
    root.config(bg="#f5f5f5")

    font_style = ("Arial", 12)

    frame_input = tk.Frame(root, bg="#f5f5f5")
    frame_input.pack(pady=10)

    tk.Label(frame_input, text="NPM:", font=font_style, bg="#f5f5f5").grid(row=0, column=0, padx=10, pady=5)
    entry_npm = tk.Entry(frame_input, font=font_style, width=30)
    entry_npm.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(frame_input, text="Name:", font=font_style, bg="#f5f5f5").grid(row=1, column=0, padx=10, pady=5)
    entry_name = tk.Entry(frame_input, font=font_style, width=30)
    entry_name.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(frame_input, text="Program:", font=font_style, bg="#f5f5f5").grid(row=2, column=0, padx=10, pady=5)
    entry_program = tk.Entry(frame_input, font=font_style, width=30)
    entry_program.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(frame_input, text="Faculty:", font=font_style, bg="#f5f5f5").grid(row=3, column=0, padx=10, pady=5)
    entry_faculty = tk.Entry(frame_input, font=font_style, width=30)
    entry_faculty.grid(row=3, column=1, padx=10, pady=5)

    frame_buttons = tk.Frame(root, bg="#f5f5f5")
    frame_buttons.pack(pady=10)

    tk.Button(frame_buttons, text="Add Student", font=font_style, bg="#4CAF50", fg="white", command=add_student, width=15).grid(row=0, column=0, padx=10, pady=5)
    tk.Button(frame_buttons, text="Update Student", font=font_style, bg="#FF9800", fg="white", command=update_student_data, width=15).grid(row=0, column=1, padx=10, pady=5)
    tk.Button(frame_buttons, text="Delete Student", font=font_style, bg="#F44336", fg="white", command=delete_student, width=15).grid(row=0, column=2, padx=10, pady=5)

    listbox_students = tk.Listbox(root, font=font_style, width=50, height=10)
    listbox_students.pack(pady=10)

    # Menambahkan binding untuk mengupdate data ketika item di listbox diklik
    listbox_students.bind('<<ListboxSelect>>', update_student)

    show_students()

    root.mainloop()

# Menjalankan aplikasi
if __name__ == "__main__":
    create_gui()