class Giraffes:
    def left_foot_forward(self):
        print('левая нога впереди')
    def left_foot_back(self):
        print('левая нога сзади')
    def right_foot_forward(self):
        print('правая нога впереди')
    def right_foot_back(self):
        print('правая нога сзади')
    def dance(self):
        self.left_foot_forward()
        self.left_foot_back()
        self.right_foot_forward()
        self.right_foot_back()
        self.left_foot_back()
        self.right_foot_back()
        self.right_foot_forward()
        self.left_foot_forward()

reginald = Giraffes()
reginald.dance()
