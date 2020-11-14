mport datetime



def time(year,month,day,hour,minute,sec,savings,goal):
    time_1=30*(goal/savings)
    time_2=int(goal/savings)
    time_3=day
    y_1=year
    m_1=month+time_2
    create= datetime.datetime(year,month,day,hour,minute,sec)
    add=0
    if m_1>12:
        add=m_1%12
        m_1=int(m_1/12)
        
    if time_1>365:
        temp=int(time_1/365.25)
        y_1=temp+y_1
    # y_1=y_1+add
    time_rem=datetime.datetime(y_1,m_1,time_3,hour,minute,sec)-create
    print(time_rem)
