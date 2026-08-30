class StudentAccount:
    def __init__(self,name:str,marks:int)->None:
        self.name=name
        if 0<=marks<=100:
         self._marks=marks
        else:
            raise ValueError("Marks must be between 0 and 100")
        
    def update_marks(self,new_marks):
        if 0<=new_marks<=100:
            self._marks=new_marks
        else:
            raise ValueError("Marks must be between 0 and 100")
    def get_marks(self):
        return self._marks
    def display(self):
         print(f"Student name:{self.name},marks:{self._marks}")
