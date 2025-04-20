class Gorilla:
    def __init__(self):
        self.length_of_arms = 3.8
        self.length_of_legs = 2.3
        self.number_of_eyes = 2
        self.has_tail = False
        self.is_furry = True
    def print_characteristics(self):
        print(f"The gorilla's arms are {self.length_of_arms} feet long.")
        print(f"The gorilla's legs are {self.length_of_legs} feet long.")
        print(f"The gorilla has {self.number_of_eyes} eyes.")
        print(f"Does the gorilla have a tail: {self.has_tail}")
        print(f"Is the gorilla furry: {self.is_furry}")

def main():
    g = Gorilla()
    g.print_characteristics()

main()
