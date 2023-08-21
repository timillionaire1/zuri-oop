class Module:
    def __init__(self, a, b, s):
        self.initial_step = a
        self.final_step = b
        self.speed = s
    def any_obstruction(self):
        return True
    def any_obstruction(self):
        return False
    def any_time(self):
        return (self.initial_step-self.final_step)/self.speed
    
module_1=Module(53.5872, 53.474, 0.000145)
module_2=Module(-2.4138, -2.2388, 0.000145)
print(module_1.any_time())
print(module_2.any_time())