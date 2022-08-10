import pymysql
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk

# connection 
def connection():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='1234',
        db='book_system',
    )
    return conn

def refreshTable():
    for data in my_tree.get_children():
        my_tree.delete(data)

    for array in read():
        my_tree.insert(parent='', index='end', iid=array,
                       text="", values=(array), tag="orow")

    my_tree.tag_configure('orow', background='#99aab5',
                          foreground="#2f3136", font=('Gudea', 12))
    my_tree.place(x=10, y=680)

#main root   
if __name__ == '__main__':
    # gui
    root = Tk()
    root.title("Book")
    root.geometry("1080x1080")
    root.configure(bg='#2f3136')
    root.resizable(False, False)
    my_tree = ttk.Treeview(root)


    # placeholders for entry
    ph1 = tk.StringVar()
    ph2 = tk.StringVar()
    ph3 = tk.StringVar()
    ph4 = tk.StringVar()
    ph5 = tk.StringVar()

    # placeholders for Optiondrop

    option_category = [
        "---เลือก----",
        "ไม่สังกัดหมวด",
        "กีฬา ท่องเที่ยว สุขภาพและอาหาร",
        "กฏหมาย",
        "การศึกษา",
        "การเมืองและการปกครอง",
        "คอมพิวเตอร์",
        "การเกษตรและชีววิทยา",
        "เทคโนโลยี วิศวกรรม อุตสาหกรรม",
        "ประวัติศาสตร์และอัตชีวประวัติ",
        "จิตวิทยา",
        "วิทยาศาสตร์",
        "ศาสนาและปรัชญา",
        "ธุรกิจ เศรษฐศาสตร์และการจัดการ",
        "ศิลปะและวัฒนธรรม",
        "ทั่วไป",
        "นวนิยาย อ่านเล่นและนิทาน",
        "สังคมศาสตร์",
        "การเรียนรู้สำหรับเด็ก",
        "Help Me Learn Series",
        "ไฟฟ้าและอิเล็กทรอนิกส์",
        "ภาษาศาสตร์",
        "วรรณคดี",
        "ไม่สังกัดหมวด"
    ]

    option_publisher = [
        "---เลือก----",
        "ไม่ปรากฏสำนักพิมพ์ ",
        "สำนักพิมพ์ เอ็ดดูเวิลด์เน็ต",
        "สำนักพิมพ์ น้ำฝน",
        "สำนักพิมพ์ ทูบีเลิฟ",
        "สำนักพิมพ์ สกายบุ๊คส์",
        "สำนักพิมพ์มหาวิทยาลัยเกษตรศาสตร์",
        "สำนักพิมพ์ เอ็ม-เอ็ดดูเคชั่น",
        "สำนักพิมพ์ ไอ เอ็ม บุ๊คส์",
        "สำนักพิมพ์ มาร์เก็ตติ้ง แคเรีย",
        "มหาวิทยาลัยแห่งชาติลาว",
        "สำนักพิมพ์แม่โพสพ",
        "สำนักพิมพ์ ฟาร์โกล๊บ พับลิชชิ่ง",
        "สำนักพิมพ์ Freemind Publishing",
        "ชุติมา ไตรรัตน์วรกุล",
        "ศูนย์ส่งเสริมวิชาการ",
        "สำนักพิมพ์ วังอักษร",
        "เรสเตอร์ บุ๊ค",
        "สำนักพิมพ์ทีบุ๊คส์",
        "สำนักพิมพ์ปราณ",
        "สำนักพิมพ์ ยิปซี",
        "สำนักพิมพ์ กรีน ปัญญาญาณ",
        "สำนักพิมพ์ ธรรมสภา",
        "สำนักพิมพ์ IDC Premier"
    ]


    option_type = [
        "---เลือก----",
        "หนังสือเผยแพร่ ",
        "หนังสือลิขสิทธิ์สำนักพิมพ์",
        "หนังสือหายาก",
        "หนังสือต่างประเทศ"
    ]

    clicked_category = StringVar()
    clicked_category.set(option_category[0])
    clicked_publisher = StringVar()
    clicked_publisher.set(option_category[0])
    clicked_type = StringVar()
    clicked_type.set(option_category[0])

    # placeholder set value function


    def setph(word, num):
        if num == 1:
            ph1.set(word)
        if num == 2:
            ph2.set(word)
        if num == 3:
            ph3.set(word)
        if num == 4:
            ph4.set(word)
        if num == 5:
            ph5.set(word)


def read():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM book_table")
    results = cursor.fetchall()
    conn.commit()
    conn.close()
    return results


def add():
    bookid = str(bookidEntry.get())
    title = str(titleEntry.get())
    author = str(authorEntry.get())
    headings = str(headingEntry.get())
    details = str(detailsEntry.get())
    drop_cat = str(clicked_category.get())
    drop_pub = str(clicked_publisher.get())
    drop_t = str(clicked_type.get())
    if (bookid == "" or bookid == " ") or (title == "" or title == " ") or (author == "" or author == " ") or (headings == "" or headings == " ") or (details == "" or details == " ") or (drop_cat == "" or drop_cat == "---เลือก----") or (drop_pub == "" or drop_pub == "---เลือก----") or (drop_t == "" or drop_t == "---เลือก----"):
        messagebox.showinfo("Error", "Please fill up the blank entry")
        return
    else:
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO book_table VALUES ('"+bookid + "','"+title+"','"+author +
                           "','"+headings+"','"+details+"','"+drop_cat+"','"+drop_pub+"','"+drop_t+"') ")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", "Book ID already exist")
            return

    refreshTable()


def reset():
    desicion = messagebox.askquestion("Warning!!", "Delete all data ?")
    if desicion != "yes":
        return
    else:
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM book_table")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", "Sorry an error occured")
            return

    refreshTable()


def deletedata():
    desicion = messagebox.askquestion(
        "Warning!!", "Delete all selected data ?")
    if desicion != "yes":
        return
    else:
        selected_item = my_tree.selection()[0]
        deleteData = str(my_tree.item(selected_item)['values'][0])
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM book_table WHERE BOOKID='"+str(deleteData)+"'")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", "Sorry an error occured")
            return

    refreshTable()


def select():
    try:
        selected_item = my_tree.selection()[0]
        bookid = str(my_tree.item(selected_item)['values'][0])
        title = str(my_tree.item(selected_item)['values'][1])
        author = str(my_tree.item(selected_item)['values'][2])
        headings = str(my_tree.item(selected_item)['values'][3])
        details = str(my_tree.item(selected_item)['values'][4])
        drop_cat = str(my_tree.item(selected_item)['values'][5])
        drop_pub = str(my_tree.item(selected_item)['values'][6])
        drop_t = str(my_tree.item(selected_item)['values'][7])

        setph(bookid, 1)
        setph(title, 2)
        setph(author, 3)
        setph(headings, 4)
        setph(details, 5)
        clicked_category.set(drop_cat)
        clicked_publisher.set(drop_pub)
        clicked_type.set(drop_t)

    except:
        messagebox.showinfo("Error", "Please select a data row")


def search():
    bookid = str(bookidEntry.get())
    title = str(titleEntry.get())
    author = str(authorEntry.get())
    headings = str(headingEntry.get())
    details = str(detailsEntry.get())
    drop_cat = str(clicked_category.get())
    drop_pub = str(clicked_publisher.get())
    drop_t = str(clicked_type.get())

    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM book_table WHERE BOOKID='" +
                   bookid+"' or TITLE='" +
                   title+"' or AUTHOR='" +
                   author+"' or HEADING='" +
                   headings+"' or DETAILS='" +
                   details+"' or CATEGORY='" +
                   drop_cat+"' or PUBLISHER='" +
                   drop_pub+"' or BOOK_TYPE='" +
                   drop_t+"' ")

    try:
        result = cursor.fetchall()

        for num in range(0, 5):
            setph(result[0][num], (num+1))

        conn.commit()
        conn.close()
    except:
        messagebox.showinfo("Error", "No data found")


def update():
    selectedbookid = ""

    try:
        selected_item = my_tree.selection()[0]
        selectedbookid = str(my_tree.item(selected_item)['values'][0])
    except:
        messagebox.showinfo("Error", "Please select a data row")

    bookid = str(bookidEntry.get())
    title = str(titleEntry.get())
    author = str(authorEntry.get())
    headings = str(headingEntry.get())
    details = str(detailsEntry.get())
    drop_cat = str(clicked_category.get())
    drop_pub = str(clicked_publisher.get())
    drop_t = str(clicked_type.get())
    if (bookid == "" or bookid == " ") or (title == "" or title == " ") or (author == "" or author == " ") or (headings == "" or headings == " ") or (details == "" or details == " ") or (drop_cat == "" or drop_cat == "---เลือก----") or (drop_pub == "" or drop_pub == "---เลือก----") or (drop_t == "" or drop_t == "---เลือก----"):
        messagebox.showinfo("Error", "Please fill up the blank entry")
        return
    else:
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE book_table SET BOOKID='" +
                           bookid+"', TITLE='" +
                           title+"', AUTHOR='" +
                           author+"', HEADING='" +
                           headings+"', DETAILS='" +
                           details+"', CATEGORY='" +
                           drop_cat+"', PUBLISHER='" +
                           drop_pub+"', BOOK_TYPE='" +
                           drop_t+"' WHERE BOOKID='" +
                           selectedbookid+"' ")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", "Stud ID already exist")
            return

    refreshTable()


# gui
lblTitle = Label(root, text="Registration Book", font=(
    "Gudea", 42, "bold"), fg="#ffffff", bg="#2f3136")
lblTitle.pack(pady=50)

Label(root, text="Book ID", font=(
    "Gudea", 12, "bold"), fg="#ffffff", bg="#2f3136").place(x=50, y=150)
Label(root, text="Title", font=(
    "Gudea", 12, "bold"), fg="#ffffff", bg="#2f3136").place(x=50, y=190)
Label(root, text="Author", font=(
    "Gudea", 12, "bold"), fg="#ffffff", bg="#2f3136").place(x=50, y=230)
Label(root, text="Heading", font=(
    "Gudea", 12, "bold"), fg="#ffffff", bg="#2f3136").place(x=50, y=270)
Label(root, text="Details", font=(
    "Gudea", 12, "bold"), fg="#ffffff", bg="#2f3136").place(x=50, y=310)
Label(root, text="Category", font=(
    "Gudea", 12, "bold"), fg="#ffffff", bg="#2f3136").place(x=50, y=350)
Label(root, text="Publisher", font=(
    "Gudea", 12, "bold"), fg="#ffffff", bg="#2f3136").place(x=50, y=390)
Label(root, text="Book type", font=(
    "Gudea", 12, "bold"), fg="#ffffff", bg="#2f3136").place(x=50, y=430)

# textvariable later
bookidEntry = Entry(root, width=30, bd=2, font=("Gudea", 12), textvariable=ph1)
titleEntry = Entry(root, width=30, bd=2, font=("Gudea", 12), textvariable=ph2)
authorEntry = Entry(root, width=30, bd=2, font=("Gudea", 12), textvariable=ph3)
headingEntry = Entry(root, width=30, bd=2, font=(
    "Gudea", 12), textvariable=ph4)
detailsEntry = Entry(root, width=30, bd=2, font=(
    "Gudea", 12), textvariable=ph5)

# OptionDrop
drop_category = OptionMenu(root, clicked_category, *option_category)
drop_publisher = OptionMenu(root, clicked_publisher, *option_publisher)
drop_type = OptionMenu(root, clicked_type, *option_type)

# place OptionMenu
drop_category.place(x=250, y=350)
drop_publisher.place(x=250, y=390)
drop_type.place(x=250, y=430)

# place entry
bookidEntry.place(x=250, y=150)
titleEntry.place(x=250, y=190)
authorEntry.place(x=250, y=230)
headingEntry.place(x=250, y=270)
detailsEntry.place(x=250, y=310)

# button
Button(root, text="Save New Book", font=("Gudea", 14, "bold"), height=2,
       width=43, bg="#7289DA", fg="#ffffff", command=add).place(x=600, y=150)
Button(root, text="Update Book", font=("Gudea", 14, "bold"), height=2,
       width=43, bg="#7289DA", fg="#ffffff", command=update).place(x=600, y=220)
Button(root, text="Delete", font=("Gudea", 14, "bold"), height=2,
       width=43, bg="#7289DA", fg="#ffffff", command=deletedata).place(x=600, y=290)
Button(root, text="Search Book", font=("Gudea", 14, "bold"), height=2,
       width=43, bg="#7289DA", fg="#ffffff", command=search).place(x=600, y=360)
Button(root, text="Reset All", font=("Gudea", 14, "bold"), height=2,
       width=43, bg="#7289DA", fg="#ffffff", command=reset).place(x=600, y=430)
Button(root, text="Select", font=("Gudea", 14, "bold"), height=2,
       width=43, bg="#7289DA", fg="#ffffff", command=select).place(x=600, y=500)

style = ttk.Style()
style.configure("Treeview.Heading", font=('Arial Bold', 15))

my_tree['columns'] = ("Book ID", "Title", "Author", "Heading",
                      "Details", "Category", "Publisher", "Type")

my_tree.column("#0", width=0, stretch=NO)
my_tree.column("Book ID", anchor=CENTER, width=100)
my_tree.column("Title", anchor=CENTER, width=120)
my_tree.column("Author", anchor=CENTER, width=150)
my_tree.column("Heading", anchor=CENTER, width=120)
my_tree.column("Details", anchor=CENTER, width=150)
my_tree.column("Category", anchor=CENTER, width=120)
my_tree.column("Publisher", anchor=CENTER, width=120)
my_tree.column("Type", anchor=CENTER, width=120)

my_tree.heading("Book ID", text="BooK ID", anchor=CENTER)
my_tree.heading("Title", text="Title", anchor=CENTER)
my_tree.heading("Author", text="Author", anchor=CENTER)
my_tree.heading("Heading", text="Heading", anchor=CENTER)
my_tree.heading("Details", text="Details", anchor=CENTER)
my_tree.heading("Category", text="Category", anchor=CENTER)
my_tree.heading("Publisher", text="Publisher", anchor=CENTER)
my_tree.heading("Type", text="Type", anchor=CENTER)

refreshTable()
root.mainloop()
