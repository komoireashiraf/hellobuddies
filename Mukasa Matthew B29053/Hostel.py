##MUKASA MATTHEW 
##M24B13/054



#Visitor class(added time in and out)
class Visitor:
   def __init__(self, Name, Number, Reason, Time_In, Time_Out):
      self.name=Name
      self.number=Number
      self.reason=Reason
      self.Time_In=Time_In
      self.Time_Out=Time_Out
   def info (self):
      print(f"The vistor is {self.name} with an ID number {self.number}. The time they have enetered the hostel is {self.Time_In} and they left at {self.Time_Out}. The reason for their visit: {self.reason}")   

#Resident Class(Name of the resident, their id number and room)      
class Resident:
    def __init__(self, Res_Name, Res_Num, Res_Room):
       self.ResidentName=Res_Name
       self.ResidentNumber=Res_Num
       self.ResidentRoom=Res_Room
    def Res_info (self):
      print(f"The resident is {self.ResidentName} with an ID number {self.ResidentNumber} in room {self.ResidentRoom}")   
#Hostel Class(Includes hostel Name and location)
class Hostel:
    def __init__ (self, Hos_Name, Hos_Loc):
       self.HostelName=Hos_Name
       
       self.HostelLocation=Hos_Loc
       self.visits=[]
    def record_visit(self, visitor, resident):
       self.visits.append({
          "visitor": visitor,
          "resident": resident
       })
       print(f"Recorded visit: {visitor.name} visited {resident.ResidentName}.")

    def show_visits(self):
       print(f"\n--- Visits at {self.HostelName} ---")
       if not self.visits:
          print("No recorded visits")
       else:
          for visit in self.visits:
             visitor_name=visit['visitor'].name
             resident_name=visit['resident'].ResidentName   
             resident_room=visit['resident'].ResidentRoom
             print(f"- {visitor_name} visted {resident_name} in room {resident_room}.")
# 
#Objects for all the classes
visitor1=Visitor("Samantha","F123", "Just checking", "12:05 pm", "2:00pm")  
visitor2=Visitor("Merinah","A53", "Finalizing group work", "3:05 pm", "4:45pm") 
visitor3=Visitor("Nothing","B34", "Proffessional Visit", "11:03 am", "2:50pm") 

#Resident
res1=Resident("Samuel","B3", "-5")  
res2=Resident("Mary","V4", "-12") 
res3=Resident("Sammy","M2", "-3") 

#hostel
hos1=Hostel("Sarameck Hostel","Wandegeya")  
hos2=Hostel("David's Ark","Bugujju") 
hos3=Hostel("PDR Hostel","Bugujju")

#Recording visit
hos3.record_visit(visitor1, res1)

#Example outputs 
visitor1.info()
res2.Res_info()
#Showing the visits
hos3.show_visits()