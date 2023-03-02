from json.decoder import JSONDecodeError
import operations
import json
from json import JSONDecodeError

print("Welcome to Meet app")
tp=open('organizers.json','r+')
try:
    cp=json.load(tp)
    if 'admin@edyoda.com' not in str(cp):
        operations.Register('organizer','members.json','organizers.json','admin','admin@edyoda.com','admin')
    tp.close()
except JSONDecodeError:
    operations.Register('organizer','members.json','organizers.json','admin','admin@edyoda.com','admin')
c=1
while True:
    print("Press:")
    print("1: Register")
    print("2: Login")
    print("0: Exit")
    try:
        c=int(input())
    except ValueError:
        print("Please enter valid choice")
        continue
    if c==1:
        print("Press :")
        print("1: Register as Organizer")
        print("2: Register as Member")
        try:
            in1=int(input())
        except ValueError:
            print("Please enter valid choice")
        if in1==1:
            print("Enter Full Name:")
            F=input()
            print("Enter Email:")
            E=input()
            print("Enter Password:")
            P=input()
            if (len(F)*len(E)*len(P))==0 or '@' not in E or '.com' not in E:
                print("Please enter valid data")
                continue
            else:
                operations.Register('organizer','members.json','organizers.json',F,E,P)
                print("Registered successfully as Organizer")
        elif in1==2:
            print("Enter Full Name:")
            F=input()
            print("Enter Email:")
            E=input()
            print("Enter Password:")
            P=input()
            if (len(F)*len(E)*len(P))==0 or '@' not in E or '.com' not in E:
                print("Please enter valid data")
                continue
            else:
                operations.Register('member','members.json','organizers.json',F,E,P)
                print("Registered successfully as Member")
        else:
            print("Please enter valid choice!")
    elif c==2:
        print("Press: ")
        print("1: Login as Organizer")
        print("2: Login as Member")
        try:
            in1=int(input())
        except ValueError:
            print("Please enter valid choice")
        if in1==1:
            print("Enter Email:")
            E=input()
            print("Enter Password:")
            P=input()
            s=operations.Login('organizer','members.json','organizers.json',E,P)
            if s==False:
                print("Invalid Credentials")
                continue
            else:
                t=open('organizers.json','r')
                cnt=json.load(t)
                t.close()
                n=""
                for i in range(len(cnt)):
                    if cnt[i]["Email"]==E and cnt[i]["Password"]==P:
                        n=cnt[i]["Full Name"]
                        break
                print("Welcome "+str(n))
                while True:
                    print("Press :")
                    print("1: Create Event")
                    print("2: View all Events created")
                    print("3: View Event Details by ID")
                    print("4: Update Event")
                    print("5: Delete Event")
                    print("0: Logout")
                    try:
                        i1=int(input())
                    except ValueError:
                        print("Please enter valid choice")
                    if i1==1:
                        Ev_ID=operations.AutoGenerate_EventID()
                        print("Event ID Generated - "+str(Ev_ID))
                        print("Enter Event Name:")
                        Ev_Name=input()
                        print("Enter Start Date (YYYY-MM-DD):")
                        St_dt=input()
                        print("Enter Start Time (HH:MM:SS):")
                        St_t=input()
                        print("Enter End Date (YYYY-MM-DD):")
                        En_dt=input()
                        print("Enter End Time (HH:MM:SS):")
                        En_t=input()
                        print("Enter Total Seats:")
                        try:
                            Cap=int(input())
                        except ValueError:
                            print("Please enter valid data")
                            continue
                        if (len(Ev_Name)*len(Ev_ID)*len(St_dt)*len(En_dt)*len(str(Cap)))==0 or len(St_dt)!=10 or len(En_dt)!=10 or len(St_t)!=8 or len(En_t)!=8 or St_dt>En_dt or (St_dt==En_dt and St_t>En_t):
                            print("Please enter valid data")
                            continue
                        else:
                            operations.Create_Event(n,'events.json',Ev_ID,Ev_Name,St_dt,St_t,En_dt,En_t,[],Cap,Cap)
                            print("Event created successfully")
                    elif i1==2:
                        ev_details=operations.View_Events(n,'events.json')
                        if len(ev_details)==0:
                            print("No Events created yet! \n")
                        else:
                            for i in range(len(ev_details)):
                                print("Event ID: "+str(ev_details[i]['ID']))
                                print("Event Name: " +str(ev_details[i]['Name']))
                                print("Organizer: " +str(ev_details[i]['Organizer']))
                                print("Start Date: " +str(ev_details[i]['Start Date']))
                                print("Start Time: " +str(ev_details[i]['Start Time']))
                                print("End Date: " +str(ev_details[i]['End Date']))
                                print("End Time: " +str(ev_details[i]['End Time']))
                                print("Total Users Registered: "+str(len(ev_details[i]["Users Registered"])))
                                print("Seats Available: "+str(ev_details[i]['Seats Available']))
                                print('\n')
                    elif i1==3:
                        print("Enter Event ID")
                        ev_id=input()
                        f14=open('events.json','r')
                        try:
                            c14=str(json.load(f14))
                            if ev_id not in c14:
                                print("Invalid event ID")
                                continue
                        except JSONDecodeError:
                            print("Events not available")
                            continue
                        d=operations.View_Event_ByID('events.json',ev_id)
                        print("Event Name: " +str(d[0]['Name']))
                        print("Organizer: " +str(d[0]['Organizer']))
                        print("Start Date: " +str(d[0]['Start Date']))
                        print("Start Time: " +str(d[0]['Start Time']))
                        print("End Date: " +str(d[0]['End Date']))
                        print("End Time: " +str(d[0]['End Time']))
                        print("Total Seats: "+str(d[0]["Capacity"]))
                        print("Seats Available: "+str(d[0]['Seats Available']))
                        print('\n')
                    elif i1==4:
                        print("Enter Event ID:")
                        ev_id=input()
                        print("Enter detail to be Updated ( Name || Start Date || Start Time || End Time || End Date ): ")
                        dtl=input()
                        print("Enter new value:")
                        updtl=input()
                        f11=open('events.json','r')
                        try:
                            c11=str(json.load(f11))
                            f11.close()
                        except JSONDecodeError:
                            print("No events created")
                            f11.close()
                            continue
                        if ev_id not in c11:
                            print("Invalid event ID")
                            continue
                        if (len(ev_id)*len(dtl)*len(updtl))==0:
                            print("Please enter valid data")
                            continue
                        else:
                            ch=operations.Update_Event(n,'events.json',ev_id,dtl,updtl)
                        if ch==False:
                            print("Cannot update event")
                        else:
                            print("Event updated successfully")
                    elif i1==5:
                        print("Enter Event ID")
                        event_id=input()
                        f1=open('events.json','r')
                        try:
                            c1=str(json.load(f1))
                            f1.close()
                        except JSONDecodeError:
                            print("No events created")
                            f1.close()
                            continue
                        if event_id not in c1:
                            print("Invalid event ID")
                            continue
                        if len(event_id)==0:
                            print("Please enter valid data")
                            continue
                        else:
                            o1=operations.Delete_Event(n,'events.json',event_id)
                        if o1==True:
                            print("Event deleted successfully")
                        else:
                            print("Cannot delete event")
                    elif i1==0:
                        break
                    else:
                        print("Ivalid Option")
        elif in1==2:
            print("Enter Email:")
            E=input()
            print("Enter Password:")
            P=input()
            s=operations.Login('member','members.json','organizers.json',E,P)
            if s==False:
                print("Invalid Credentials")
                continue
            else:
                t=open('members.json','r')
                cnt=json.load(t)
                t.close()
                n=""
                for i in range(len(cnt)):
                    if cnt[i]["Email"]==E and cnt[i]["Password"]==P:
                        n=cnt[i]["Full Name"]
                        break
                print("Welcome "+str(n))
                while True:
                    print("Press:")
                    print("1: View Registered Events")
                    print("2: Register for an Event")
                    print("3: Update Password")
                    print("4: View Event Details by ID")
                    print("0: Logout")
                    try:
                        i3=int(input())
                    except ValueError:
                        print("Please enter valid choice")
                    if i3==1:
                        all_events=[]
                        upcoming_ongoing=[]
                        operations.fetch_all_events('events.json',n,all_events,upcoming_ongoing)
                        print("All Upcoming/Ongoing Events: ")
                        for i in range(len(upcoming_ongoing)):
                            print("Event Name: " +str(upcoming_ongoing[i]['Name']))
                            print("Start Date: " +str(upcoming_ongoing[i]['Start Date']))
                            print("Start Time: " +str(upcoming_ongoing[i]['Start Time']))
                            print("End Date: " +str(upcoming_ongoing[i]['End Date']))
                            print("End Time: " +str(upcoming_ongoing[i]['End Time']))
                            print("Organizer: " +str(upcoming_ongoing[i]['Organizer']))
                            print('\n')
                    elif i3==2:
                        l=operations.View_all_events('events.json')
                        if len(l)==0:
                            print("No events available")
                        else:
                            print("All Events: ")
                            for i in range(len(l)):
                                t=l[i]
                                print("Event ID: "+str(t['ID']))
                                print("Event Name: " +str(t['Name']))
                                print("Organizer: "+str(t['Organizer']))
                                print("Start Date: " +str(t['Start Date']))
                                print("Start Time: " +str(t['Start Time']))
                                print("End Date: " +str(t['End Date']))
                                print("End Time: " +str(t['End Time']))
                                print("Seats Available: "+str(t['Seats Available']))
                                print("Total Seats: "+str(t['Capacity']))
                                print('\n')
                        print("Enter Event ID: ")
                        event_ID=input()
                        ch=operations.Register_for_Event('events.json',event_ID,n)
                        f44=open('events.json','r')
                        c44=str(json.load(f44))
                        if event_ID not in c44:
                            print("Invalid Event ID")
                        if ch==True:
                            print("Successfully Registered")
                        else:
                            print("Event seats are full! \n")
                    elif i3==3:
                        print("Enter new password")
                        pswd=input()
                        if(len(pswd))<4:
                            print("Please enter valid data")
                            continue
                        op=operations.Update_Password('members.json',n,pswd)
                        if op==True:
                            print("Password updated successfully")
                        else:
                            print("Cannot update password")
                    elif i3==4:
                        print("Enter Event ID")
                        ev_id=input()
                        f14=open('events.json','r')
                        try:
                            c14=str(json.load(f14))
                            if ev_id not in c14:
                                print("Invalid event ID")
                                continue
                        except JSONDecodeError:
                            print("Events not available")
                            continue
                        d=operations.View_Event_ByID('events.json',ev_id)
                        print("Event Name: " +str(d[0]['Name']))
                        print("Start Date: " +str(d[0]['Start Date']))
                        print("Start Time: " +str(d[0]['Start Time']))
                        print("End Date: " +str(d[0]['End Date']))
                        print("End Time: " +str(d[0]['End Time']))
                        print("End Time: " +str(d[0]['End Time']))
                        print("Organizer: "+str(d[0]["Organizer"]))
                        print("Seats Available: "+str(d[0]['Seats Available']))
                        print('\n')
                    elif i3==0:
                        break
                    else:
                        print("Invalid Choice, Please enter again")
                        continue
    elif c==0:
        break
    else:
        print("Invalid Choice, Please enter again")
        continue

