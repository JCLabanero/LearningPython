class Athlete:
    # Constructor/Init
    event = 'Men\'s Volleyball'  # attry

    def __init__(self, jerseyNo, name, position) -> None:
        self.jerseyNo = jerseyNo
        self.name = name
        self.position = position


a = Athlete(12, "john", "forward")
print(a.jerseyNo)
