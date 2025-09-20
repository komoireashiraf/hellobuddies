class Hostel:
    def __init__(self, name):
        self.name = name 
        self.visits = []
    
    def record_visit(self, visitor, resident):
        visit_record ={
            'visitor': visitor,
            'resident': resident
        }
        self.visits.append(visit_record)
        print (f"Visit recorded: {visitor.name} visited {resident.name} in room {resident.room}")

    def show_visits(self):
        print(f"\n-- Visit Records for {self.name} ---")
        if not self.visits:
            print("No visits recorded yet.")
            return
        
        for i, visit in enumerate(self.visits, 1):
            print(f"{i}. {visit['visitor'].name} (ID: {visit['visitor'].visitor_id})"
                  f"visited {visit['resident'].name}(Room: {visit['resident'].room})")
            
class Visitor:
    def __init__(self, name, visitor_id):
       self.name = name 
       self.visitor_id = visitor_id
    
class Resident:
    def __init__(self, name, room):
       self.name = name 
       self.room = room


visitor1 = Visitor('Janice', 'U0054683F')
resident1 = Resident('Gabby', 'A10')
hostel = Hostel('Ankrah')

hostel.record_visit(visitor1, resident1)

hostel.show_visits()
    