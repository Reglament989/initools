
class Switch():
    def __init__(self, obj=None, type_obj=None, attempts=None, on_success=None, on_fail=None):
        if obj is None:
            raise Exception('LoL, do you wont to compare nothing?')
        else:
            pass # NOthhhhing
        if type_obj:
            self._type = type_obj
        else:
            self._type = type(obj)
        if attempts:
            if type(attempts) is int:
                self.max_attempts = attempts
            else:
                raise ValueError("Please pull int item for attempts")
        else:
            self.max_attempts = 10E20 # max 1000000000000000000000
        if on_success:
            if hasattr(on_success, '__call__'):
                self.on_success = on_success
            else:
                raise TypeError("Method on_success worked only with func.")
        else:
            self.on_success = None
        if on_fail:
            if hasattr(on_fail, '__call__'):
                self.on_fail = on_fail
            else:
                raise TypeError("Method on_fail worked only with func.")
        else:
            self.on_fail = None
        self.obj = obj
        self.attempts = 0
        self.success = False

    def __repr__(self):
        return f"""
Case function for {self.obj}
Attempts to check: {self.attempts}
Success: {self.success}
"""

    def case(self, comparable=None):
        if comparable is not None:
            if self.max_attempts > self.attempts:
                self.attempts += 1
                if self.obj == comparable:
                    self.success = True
                    if self.on_success is not None:
                        self.on_success()
                    return True
                else:
                    if self.on_fail is not None:
                        self.on_fail()
                    return False
            else:
                raise StopIteration(f"Your case has reached max attempts - {self.max_attempts}") 
        else:
            raise ValueError('Mabe you want give to case comparable?')

