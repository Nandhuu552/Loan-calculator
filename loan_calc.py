import tkinter as tk
import customtkinter as ck
from tkinter import ttk
import matplotlib.pyplot as Plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

app = ck.CTk()
style = ttk.Style()
style.theme_use('clam')
style.configure("Treeview",font = ("Arial,10"), background = "black",
                 foreground= "white")
style.configure("Treeview.Headings", font = ("Arial,10"), background = "#573CFA",
                foreground= "black" )
ck.set_appearance_mode('dark')
ck.set_default_color_theme('blue')
app.geometry('1200*600')
app.title('Loan Calculator')

#left frame
left_frame = ck.CTkFrame(master = app,
                         width = 350,
                         height=580,
                         fg_color='#573CFA')
                              
left_frame.place(x =10,y= 10)

title = ck.CTkLabel(master= left_frame, text = "Loan Calculator",
                   font= ("Arial",20))
title.pack(padx = 100, pady = 50, fill="both", expand="True")

loan_amt_label = ck.CTkLabel(master= left_frame, text = "Enter loan Amount",
                   font= ("Arial",20), text_color="black", corner_radius=20)
loan_amt_label.pack(padx = 30, pady= 10, fill="both", expand="True")

loan_amt_entry = ck.CTkEntry(master= left_frame, font= ("Arial",20),
                             fg_color='white',text_color="black", corner_radius=20)
loan_amt_entry.pack(padx = 30, pady= 10, fill="both", expand="True")


loan_int_label = ck.CTkLabel(master= left_frame, text = "Enter loan Interest Rate",
                   font= ("Arial",20))
loan_int_label.pack(padx = 30, pady= 10, fill="both", expand="True")

loan_int_entry = ck.CTkEntry(master= left_frame, font= ("Arial",20),
                             fg_color='white',text_color="black", corner_radius=20)
loan_int_entry.pack(padx = 30, pady= 10, fill="both", expand="True")


loan_tenure_label = ck.CTkLabel(master= left_frame, text = "Enter loan Tenure",
                   font= ("Arial",20))
loan_tenure_label.pack(padx = 30, pady= 10, fill="both", expand="True")

loan_tenure_entry = ck.CTkEntry(master= left_frame, font= ("Arial",20),
                             fg_color='white',text_color="black", corner_radius=20)
loan_tenure_entry.pack(padx = 30, pady= 10, fill="both", expand="True")

submit_btn = ck.CTkButton(master=left_frame, text = "submit",
                          font= ("Arial",20), corner_radius=20,
                          fg_color="black", hover_color="black", 
                          command=lambda: submit())
submit_btn.pack(padx = 30,pady = 50,fill ="both")



#Right frame
right_frame = ck.CTkFrame(master = app,
                         width = 800,
                         height=580,
                         fg_color='#b63cfa')
                        
right_frame.place(x =370,y= 10)


#submit Button
def submit():
    principal = float(loan_amt_entry.get())
    interest = float(loan_int_entry.get())
    tenure = int(loan_tenure_entry.get())
    data = calculations(principal, interest, tenure)
    interest_payable = table_display(data)
    chart_display(principal, interest_payable)
    summary_display(principal, interest, data[0]['EMI'], tenure, interest_payable)
 

def summary_display(principal, interest, emi, tenure, interest_payable):

    inner_frame = ck.CTkFrame(master=right_frame)
    inner_frame.grid(row=0, column=0)
    principal_text = ck.CTkLabel(master=inner_frame,
                                 font = ("Arial",20),
                                 text = "Loan amount",
                                 width = 45)
    principal_text.grid(row=0, column=0,padx=20,)

    principal_value = ck.CTkLabel(master=inner_frame,
                                 font = ("Arial",20),
                                 text = principal,
                                 width = 45)
    principal_value.grid(row=0, column=1,padx=20,)



    interest_text = ck.CTkLabel(master=inner_frame,
                                 font = ("Arial",20),
                                 text = "Rate of interest",
                                 width = 45)
    interest_text.grid(row=1, column=0,padx=20,)


    interest_value = ck.CTkLabel(master=inner_frame,
                                 font = ("Arial",20),
                                 text = interest,
                                 width = 45)
    interest_value.grid(row=1, column=1,padx=20,)


    tenure_text= ck.CTkLabel(master=inner_frame,
                                 font = ("Arial",20),
                                 text = "loan tenure",
                                 width = 45)
    tenure_text.grid(row=2, column=0,padx=20,)

    tenure_value = ck.CTkLabel(master=inner_frame,
                                 font = ("Arial",20),
                                 text = tenure,
                                 width = 45)
    tenure_value.grid(row=2, column=1,padx=20,)

    interest_payable_text = ck.CTkLabel(master=inner_frame,
                                 font = ("Arial",20),
                                 text = ("Interest Payable"),
                                 width = 45)
    interest_payable_text.grid(row=3, column=0,padx=20,)

    interest_payable_value = ck.CTkLabel(master=inner_frame,
                                 font = ("Arial",20),
                                 text = interest_payable,
                                 width = 45)
    interest_payable_value.grid(row=3, column=1,padx=20,)

    total_text = ck.CTkLabel(master=inner_frame,
                                 font = ("Arial",20),
                                 text = ("Loan amount"),
                                 width = 45)
    total_text.grid(row=4, column=0,padx=20,)
    
    total_value = ck.CTkLabel(master=inner_frame,
                                 font = ("Arial",20),
                                 text = (principal + interest_payable),
                                 width = 45)
    total_value.grid(row=4, column=1,padx=20,)
    



def chart_display(principal, interest_payable):
    fig = Plt.Figure(figsize=(4,3), dpi=100)
    plot = fig.add_subplot(111)
    canvas = FigureCanvasTkAgg(fig,master=right_frame)
    canvas.get_tk_widget().grid(row = 0, column=1, padx=10, pady=10)
    x = [principal, interest_payable]
    mylabels = ['Principal', 'Iterest']
    myexplode = [0.0,0.1]
    plot.pie(x, labels=mylabels, autopct='%1.1f%%', explode=myexplode)
    
    
 
def table_display(data):
     
    table = ttk.Treeview(master=right_frame, 
                         columns=('month','interest','principal','emi','balprinciple'),
                         show="headings", style="Treeview")
    
    table.heading('month', text="Month", anchor='nw')
    table.heading('interest', text="Interest Payable", anchor='nw')
    table.heading('principal', text="Principal Payable", anchor='nw')
    table.heading('emi', text="EMI", anchor='nw')
    table.heading('balprinciple', text="Balance Principle", anchor='nw')
    interest_payable = 0.00
    for k in range(len(data)):
        table.insert(parent="", index= k,
                     values= (data[k]['Month'],
                              data[k]['Interest_payable'],
                              data[k]['Principle payable'],
                              data[k]['EMI'],
                              data[k]['Balance principle']))
        interest_payable = interest_payable + data[k]['Interest_payable']
    table.grid(row = 1, column=0, rowspan=2, columnspan=2, padx=10, pady=80)
    return interest_payable

#calculations
def calculations(p,i,t):
    roi_per_mon = i/12/100
    tenure_in_mon = t*12

    emi = round(p*roi_per_mon*pow(1+roi_per_mon, tenure_in_mon))/(pow(1+roi_per_mon,tenure_in_mon)-1)
    
    balance = p
    shedule = []
    for mon in range(tenure_in_mon):
        interest_monthly_payable = round(balance * roi_per_mon)
        remain_emi_bal = round(emi - interest_monthly_payable)
        balance = round(balance - remain_emi_bal)
        shedule.append({
            'Month':mon+1,
            'Interest_payable':interest_monthly_payable,
            'Principle payable':remain_emi_bal,
            'EMI':emi,
            'Balance principle':balance
        })
    return shedule

app.mainloop()