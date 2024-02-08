class SuperMario:
    def __init__(self):
        self.position = 0

    def forward(self):
        self.position = self.position + 20

mario = SuperMario()
mario.forward()
print(mario.position)