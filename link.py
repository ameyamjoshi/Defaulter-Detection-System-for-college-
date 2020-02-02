import tkinter
from matplotlib import pyplot as plt
from matplotlib import style
import pandas as pd
import numpy as np
import tkinter
from tkinter import *
from tkinter.messagebox import *

def page1():
 master = Tk()
 def callback():
  import pandas as pd
  file=pd.read_csv('Fortnight_Attendance_I_new.csv')
  file.head()
  new_file = file.dropna(axis = 0, how ='any') 
  pd.set_option('mode.chained_assignment', None)
  new_file.to_csv('file1.csv') 
  new_file.rename(columns={'Unnamed: 0':'Roll No','Unnamed: 1':'Student Name','Unnamed: 2':'SE&PM(PP)','Unnamed: 3' : 'IS & EE(PP)',"Pimpri Chinchwad Education Trust's" : 'SDL(PP)','Unnamed: 5':'TOC(PP)','Unnamed: 6':'DBMS(PP)','Unnamed: 7' : 'CN(PP)','Unnamed: 8' : 'AOA(PP)','Unnamed: 9':'CN(PR)','Unnamed: 10':'DBMS Lab(PR)','Unnamed: 11':'SDL(PR)','Record No.: ACAD/R/037':'TH%','Unnamed: 13':'PR%','Unnamed: 14': 'Total%'},inplace=True)
  new_file.to_csv('file99.csv') 
  df1=new_file.drop(new_file.index[0])
  df1=df1[['Roll No','Student Name','SE&PM(PP)','IS & EE(PP)','SDL(PP)','TOC(PP)','DBMS(PP)','CN(PP)','AOA(PP)','CN(PR)','DBMS Lab(PR)','SDL(PR)','TH%','PR%','Total%']]
  df1.to_csv('file10.csv') 
  df1=df1.describe()
  df1.to_csv('desc.csv')
  df2=pd.read_csv('file10.csv')
  df3=df2.mean()
  df4=df3.drop(df3.index[0])
  df4.to_csv('subjectwise_mean.csv')
  df5=df2[df2['PR%']<75.0000]
  df5=df5.drop('Unnamed: 0', axis=1)
  df6=df5[['Roll No','Student Name','PR%']]
  df6.to_csv('Practical_defaulters.csv')
  df7=df2[df2['SE&PM(PP)']<75.0000]
  df7=df7.drop('Unnamed: 0', axis=1)
  df8=df7[['Roll No','Student Name','SE&PM(PP)']]
  df8.to_csv('SE&PM_Defaulters.csv')
  df9=df2[df2['IS & EE(PP)']<75.0000]
  df9=df9.drop('Unnamed: 0', axis=1)
  df10=df9[['Roll No','Student Name','IS & EE(PP)']]
  df10.to_csv('IS & EE(PP)_Defaulters.csv')
  df11=df2[df2['SDL(PP)']<75.0000]
  df11=df11.drop('Unnamed: 0', axis=1)
  df12=df11[['Roll No','Student Name','SDL(PP)']]
  df12.to_csv('SDL(PP)_Defaulters.csv')
  df13=df2[df2['TOC(PP)']<75.0000]
  df13=df13.drop('Unnamed: 0', axis=1)
  df14=df13[['Roll No','Student Name','TOC(PP)']]
  df14.to_csv('TOC(PP)_Defaulters.csv')
  df15=df2[df2['DBMS(PP)']<75.0000]
  df15=df15.drop('Unnamed: 0', axis=1)
  df16=df15[['Roll No','Student Name','DBMS(PP)']]
  df16.to_csv('DBMS(PP)_Defaulters.csv')
  df17=df2[df2['CN(PP)']<75.0000]
  df17=df17.drop('Unnamed: 0', axis=1)
  df18=df17[['Roll No','Student Name','CN(PP)']]
  df18.to_csv('CN(PP)_Defaulters.csv')
  df19=df2[df2['AOA(PP)']<75.0000]
  df19=df19.drop('Unnamed: 0', axis=1)
  df20=df19[['Roll No','Student Name','AOA(PP)']]
  df20.to_csv('AOA(PP)_Defaulters.csv')
  df21=df2[df2['CN(PR)']<75.0000]
  df21=df21.drop('Unnamed: 0', axis=1)
  df22=df21[['Roll No','Student Name','CN(PR)']]
  df22.to_csv('CN(PR)_Defaulters.csv')
  df23=df2[df2['DBMS Lab(PR)']<75.0000]
  df23=df23.drop('Unnamed: 0', axis=1)
  df24=df23[['Roll No','Student Name','DBMS Lab(PR)']]
  df24.to_csv('DBMS Lab(PR)_Defaulters.csv')
  df25=df2[df2['SDL(PR)']<75.0000]
  df25=df25.drop('Unnamed: 0', axis=1)
  df26=df25[['Roll No','Student Name','SDL(PR)']]
  df26.to_csv('SDL(PR)_Defaulters.csv')
  df27=df2[df2['TH%']<75.0000]
  df27=df27.drop('Unnamed: 0', axis=1)
  df28=df27[['Roll No','Student Name','TH%']]
  df28.to_csv('THEORY_Defaulters.csv')
  df29=df2[df2['Total%']<75.0000]
  df29=df29.drop('Unnamed: 0', axis=1)
  df30=df29[['Roll No','Student Name','Total%']]
  df30.to_csv('OVERALL_Defaulters.csv')
 b = Button(master, text="Generate Report",font=('courier',10,'bold'),width=30,height=6, fg='gold',bg='gray35',command=callback)
 b.pack(padx=15, pady=10)

 mainloop()


def page2():

 def show_answer1():
  df=pd.read_csv('file10.csv' , index_col='Roll No')
  Ans = int(num1.get())
  first=df.loc['TECOA'+str(Ans)]
  first.to_csv('stu.csv')
  x_axis_labels=[ 'SE&PM(PP)','IS & EE(PP)','SDL(PP)','TOC(PP)','DBMS(PP)','CN(PP)','AOA(PP)','CN(PR)','DBMS Lab(PR)','SDL(PR)','TH%','PR%','Total%']
  pos=np.arange(13)
  y_axis_values=[first['SE&PM(PP)'],first['IS & EE(PP)'],first['SDL(PP)'],first['TOC(PP)'],first['DBMS(PP)'],first['CN(PP)'],first['AOA(PP)'],first['CN(PR)'],first['DBMS Lab(PR)'],first['SDL(PR)'],first['TH%'],first['PR%'],first['Total%']]
  plt.bar(pos,y_axis_values)
  plt.xticks(pos,x_axis_labels)
  plt.show()
  df1=pd.read_csv('file10.csv' )

 main = tkinter.Tk()
 Label(main, text = "Enter rollno:",font=('courier',10,'bold'),width=20,height=6).grid(row=0)


 num1 = Entry(main,width=70)

 num1.grid(row=0, column=1)

 Button(main, text='Quit', font=('courier',10,'bold'),bg='azure',width=20,height=4,command=main.destroy).grid(row=4, column=0, sticky=W, pady=4)

 Button(main, text='Showgraph', font=('courier',10,'bold'),bg='SeaGreen',width=20,height=4,command=show_answer1).grid(row=4, column=1, sticky=W, pady=4)
 
 main.mainloop()

def page3():

 def p1():
  df=pd.read_csv('file10.csv')
  df1=pd.DataFrame(df,columns=['SE&PM(PP)']) 
  df1.hist()
  plt.show() 

 def p2():
  df=pd.read_csv('file10.csv')
  df2=pd.DataFrame(df,columns=['TOC(PP)'])
  df2.hist()
  plt.show()

 def p3():
  df=pd.read_csv('file10.csv')
  df3=pd.DataFrame(df,columns=['CN(PP)'])
  df3.hist()
  plt.show() 

 def p4():
  df=pd.read_csv('file10.csv')
  df4=pd.DataFrame(df,columns=['CN(PR)'])
  df4.hist()
  plt.show()

 def p5():
  df=pd.read_csv('file10.csv')
  df5=pd.DataFrame(df,columns=['DBMS Lab(PR)'])
  df5.hist()
  plt.show() 

 def p6():
  df=pd.read_csv('file10.csv')
  df6=pd.DataFrame(df,columns=['TH%','PR%'])
  df6.hist()
  plt.show()

 def p7():
  df=pd.read_csv('file10.csv')
  df1=pd.DataFrame(df,columns=['IS & EE(PP)']) 
  df1.hist()
  plt.show() 

 def p8():
  df=pd.read_csv('file10.csv')
  df2=pd.DataFrame(df,columns=['SDL(PP)'])
  df2.hist()
  plt.show()

 def p9():
  df=pd.read_csv('file10.csv')
  df3=pd.DataFrame(df,columns=['DBMS(PP)'])
  df3.hist()
  plt.show() 

 def p10():
  df=pd.read_csv('file10.csv')
  df4=pd.DataFrame(df,columns=['AOA(PP)'])
  df4.hist()
  plt.show()

 def p11():
  df=pd.read_csv('file10.csv')
  df5=pd.DataFrame(df,columns=['SDL(PR)'])
  df5.hist()
  plt.show() 

 top = tkinter.Tk()
 t=Frame(top,height=100,width=100)
 t.pack()
 B = tkinter.Button(t, text ='SE&PM(PP)',font=('courier',10,'bold'),bg='cornsilk',width=10,height=4,command = p1)
 B1 = tkinter.Button(t, text ='TOC(PP)',font=('courier',10,'bold'),bg='DeepSkyBlue',width=10,height=4, command = p2)
 B2 = tkinter.Button(t, text ='CN(PP)', font=('courier',10,'bold'),bg='cornsilk',width=10,height=4,command = p3)
 B3 = tkinter.Button(t, text ='CN(PR)', font=('courier',10,'bold'),bg='DeepSkyBlue',width=10,height=4,command = p4)
 B4 = tkinter.Button(t, text ='DBMSLab(PR)',font=('courier',10,'bold'),bg='cornsilk',width=10,height=4, command = p5)
 B5 = tkinter.Button(t, text ="Theory/Practical", font=('courier',10,'bold'),bg='DeepSkyBlue',width=20,height=4,command = p6)
 B6 = tkinter.Button(t, text ='IS & EE(PP)', font=('courier',10,'bold'),bg='cornsilk',width=10,height=4,command = p7)
 B7 = tkinter.Button(t, text ='SDL(PP)',font=('courier',10,'bold'),bg='DeepSkyBlue',width=10,height=4, command = p8)
 B8 = tkinter.Button(t, text ='DBMS(PP)', font=('courier',10,'bold'),bg='cornsilk',width=10,height=4,command = p9)
 B9 = tkinter.Button(t, text ='AOA(PP)', font=('courier',10,'bold'),bg='DeepSkyBlue',width=10,height=4,command = p10)
 B10 = tkinter.Button(t, text ='SDL(PR)',font=('courier',10,'bold'),bg='cornsilk',width=10,height=4, command = p11)

 B.pack(padx=15, pady=10, side=tkinter.LEFT)
 B1.pack(padx=15, pady=20, side=tkinter.LEFT)
 B2.pack(padx=15, pady=30, side=tkinter.LEFT)
 B3.pack(padx=15, pady=40, side=tkinter.LEFT)
 B4.pack(padx=15, pady=50, side=tkinter.LEFT)
 B5.pack(padx=15, pady=60, side=tkinter.LEFT)
 B6.pack(padx=15, pady=60, side=tkinter.LEFT)
 B7.pack(padx=15, pady=60, side=tkinter.LEFT)
 B8.pack(padx=15, pady=60, side=tkinter.LEFT)
 B9.pack(padx=15, pady=60, side=tkinter.LEFT)
 B10.pack(padx=15, pady=60, side=tkinter.LEFT)
 top.mainloop()

 top.mainloop()

window = tkinter.Tk()

page1text = tkinter.Label(window, text="PIMPRI CHINCHWAD COLLEGE OF ENGINEERING",font=('courier',16,'bold underline'))
page2text = tkinter.Label(window, text="Third Year Computer Department",font=('courier',12,'bold'),width=50,height=4,fg='chocolate')
page3text = tkinter.Label(window, text="Welcome to attendance monitoring system",font=('courier',14,'bold'),fg='VioletRed')

page1text.pack()
page2text.pack()
page3text.pack()

t=Frame(window,height=900,width=600)
t.pack()
page1btn = tkinter.Button(t, text="Report Generator(in csv)", font=('courier',10,'bold'),width=30,height=6,bg='plum',command=page1)
page2btn = tkinter.Button(t, text="          Individual report      ",font=('courier',10,'bold'), width=30,height=6,bg='khaki',command=page2)
page3btn = tkinter.Button(t, text="         Teacher's Report       ",font=('courier',10,'bold'),width=30,height=6, bg='GreenYellow',command=page3)



page1btn.pack(padx=15, pady=10, side=tkinter.LEFT)
page2btn.pack(padx=15, pady=20, side=tkinter.LEFT)
page3btn.pack(padx=15, pady=30, side=tkinter.LEFT)

window.mainloop()