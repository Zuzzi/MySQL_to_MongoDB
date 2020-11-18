import tkinter as tk
import sqlparse
import delete as dl
import insert as ins
import update as upd
import select as slc
import join as jn





def clickMe(label2, name):
    mongo_query = ""
    query = name.get()
    formatted = sqlparse.format(query, keyword_case="upper")
    parsed = sqlparse.parse(formatted)  # fa il parsing della prima stringa
    token_list = parsed[0]  # estrae la prima query (se sono presenti più di una nella stringa)
    tokens = token_list.tokens  # estrae tutte le parole della query e le classifica in base alla loro tipologia
    query_type = tokens[0].value
    if query_type == "DELETE":
        print("it's a delete")
        mongo_query = dl.delete(tokens)
    elif query_type == "INSERT":
        print("it's an insert")
        mongo_query = ins.insert(tokens)
    elif query_type == "UPDATE":
        print("it's an update")
        mongo_query = upd.update(tokens)
    elif query_type == "SELECT":
        is_join = False
        for token in tokens:
            if token.value == "LEFT JOIN":
                is_join = True
        if is_join:
            mongo_query = jn.left_outer_join(tokens)
        else:
            mongo_query = slc.select(tokens)
    else:
        mongo_query = "QUERY NOT CORRECT"
    print("the relative mongo query is: ", mongo_query)
    label2.delete('1.0', tk.END) #clear the text box
    label2.insert(tk.END, mongo_query)

def showGUI():
    window = tk.Tk()
    window.title("MySQL -> MongoDB parser")
    window.minsize(300, 200)
    label = tk.Label(window, text="Enter the MySQL query")
    label.grid(column=0, row=0)
    label2 = tk.Text(window)
    label2.grid(column=0, row=3)
    label2.insert(tk.END,"")
    name = tk.StringVar()
    nameEntered = tk.Entry(window, width=100, textvariable=name)
    nameEntered.grid(column=0, row=1)
    button = tk.Button(window, text="Click Me", command=lambda: clickMe(label2, name))
    button.grid(column=0, row=2)
    window.mainloop()

def main():
    showGUI()



if __name__ == "__main__":
    main()