class SuperMario:
    def __init__(self):
        self.position = 0

    def forward(self):
        self.position = self.position + 20

mario1 = SuperMario()
mario2 = SuperMario()

mario1.forward()

print(mario1.position)
print(mario2.position)