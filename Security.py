from tkinter import *
from Server import server
obj = server()

passwd = "test"

def check_login_passwd():
	ret = lcs(e.get(),passwd)
	if(ret == {'test'}):
		secwindow()
def lcs(S,T):
	m = len(S)
	n = len(T)
	counter = [[0]*(n+1) for x in range(m+1)]
	longest = 0
	lcs_set = set()
	for i in range(m):
		for j in range(n):
			if S[i] == T[j]:
				c = counter[i][j] + 1
				counter[i+1][j+1] = c
				if c > longest:
					lcs_set = set()
					longest = c
					lcs_set.add(S[i-c+1:i+1])
				elif c == longest:
					lcs_set.add(S[i-c+1:i+1])
	return lcs_set

def input_func(par,Master):
	
	obj.Access(par)
	#Message(Master,text=par,width=3000).pack()
	Master.destroy

def secwindow():
	master = Tk()
	master.title("Welcome")
	master.geometry("300x200+500+300")
	Label(master,text="Dept:Data,Finance,Market").pack()
	Label(master,text="Dept:").pack()
	ent = Entry(master)
	ent.pack()
	Label(master,text="Password:").pack()
	E = Entry(master,show="*")
	E.pack()
	b = Button(master, text="OK", width=10,command=lambda: input_func(E.get(),master))
	b.pack()
	mainloop()



master = Tk()
master.title("Login Page")
master.geometry("300x200+500+300")
Label(master,text="UserName:").pack()
ee = Entry(master)
ee.pack()
Label(master,text="Password:").pack()
e = Entry(master,show="*")
e.pack()
b = Button(master, text="OK", width=10, command=check_login_passwd)
b.pack()
mainloop()
