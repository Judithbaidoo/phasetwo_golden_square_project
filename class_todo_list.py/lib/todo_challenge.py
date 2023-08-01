class TodoList:
    def __init__(self):
        self.checklist = []

    def add(self, todo):
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos
        self.checklist.append(todo)
    
    def incomplete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        undone = [todo.task for todo in self.checklist if todo.completed == False]
        return undone

    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        done = [todo.task for todo in self.checklist if todo.completed == True]
        return done

    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete

        for x in self.checklist:
            if x.completed == False:
                x.completed = True
            
