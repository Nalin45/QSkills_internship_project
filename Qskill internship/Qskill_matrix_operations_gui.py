import numpy as np
import tkinter as tk
from tkinter import messagebox

# -------------------------------
# Convert text input to matrix
# -------------------------------
def read_matrix(text_widget):
    try:
        text = text_widget.get("1.0", tk.END).strip()
        rows = text.split("\n")
        matrix = []
        for row in rows:
            matrix.append(list(map(float, row.split())))
        return np.array(matrix)
    except:
        raise ValueError("Invalid matrix format.\nUse spaces for columns and new lines for rows.")

# -------------------------------
# Display result
# -------------------------------
def display_result(result):
    result_box.delete("1.0", tk.END)
    result_box.insert(tk.END, str(result))

# -------------------------------
# Matrix Operations
# -------------------------------
def add():
    try:
        A = read_matrix(matrixA)
        B = read_matrix(matrixB)
        if A.shape != B.shape:
            raise ValueError("Addition requires matrices of same size.")
        display_result(A + B)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def subtract():
    try:
        A = read_matrix(matrixA)
        B = read_matrix(matrixB)
        if A.shape != B.shape:
            raise ValueError("Subtraction requires matrices of same size.")
        display_result(A - B)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def multiply():
    try:
        A = read_matrix(matrixA)
        B = read_matrix(matrixB)
        if A.shape[1] != B.shape[0]:
            raise ValueError("Columns of A must equal rows of B.")
        display_result(np.dot(A, B))
    except Exception as e:
        messagebox.showerror("Error", str(e))

def transpose():
    try:
        A = read_matrix(matrixA)
        display_result(A.T)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def determinant():
    try:
        A = read_matrix(matrixA)
        if A.shape[0] != A.shape[1]:
            raise ValueError("Determinant requires a square matrix.")
        display_result(round(np.linalg.det(A), 2))
    except Exception as e:
        messagebox.showerror("Error", str(e))

# -------------------------------
# GUI Setup
# -------------------------------
root = tk.Tk()
root.title("Matrix Operations Tool")
root.geometry("600x550")

tk.Label(root, text="Matrix A (space-separated rows)").pack()
matrixA = tk.Text(root, height=6, width=50)
matrixA.pack()

tk.Label(root, text="Matrix B (space-separated rows)").pack()
matrixB = tk.Text(root, height=6, width=50)
matrixB.pack()

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Add", width=12, command=add).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Subtract", width=12, command=subtract).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Multiply", width=12, command=multiply).grid(row=0, column=2, padx=5)
tk.Button(btn_frame, text="Transpose (A)", width=12, command=transpose).grid(row=1, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="Determinant (A)", width=12, command=determinant).grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Result").pack()
result_box = tk.Text(root, height=6, width=50)
result_box.pack()

root.mainloop()
