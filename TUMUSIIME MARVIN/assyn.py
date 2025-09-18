class Visitor:
    def __init__(self, name, visitor_id):
        self.name = name
        self.visitor_id = visitor_id

    def __str__(self):
        return f"Visitor(Name: {self.name}, ID: {self.visitor_id})"


class Resident:
    def __init__(self, name, room):
        self.name = name
        self.room = room

    def __str__(self):
        return f"Resident(Name: {self.name}, Room: {self.room})"


class Hostel:
    def __init__(self, name):
        self.name = name
        self.visits = []

    def record_visit(self, visitor, resident):
        self.visits.append((visitor, resident))
        print(f"✅ Visit recorded: {visitor.name} visited {resident.name} in room {resident.room}")

    def show_visits(self):
        print(f"\n📌 Visits recorded at {self.name}:")
        if not self.visits:
            print("No visits recorded yet.")
            return
        for i, (visitor, resident) in enumerate(self.visits, 1):
            print(f"{i}. {visitor.name} (ID: {visitor.visitor_id}) visited {resident.name} (Room: {resident.room})")

visitor1 = Visitor("Alice", "V123")
resident1 = Resident("Bob", "12B")
hostel = Hostel("UCU Hostel")

hostel.record_visit(visitor1, resident1)
hostel.show_visits()