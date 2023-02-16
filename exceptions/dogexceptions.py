from food import Food   # DO NOT CHANGE THE IMPORTS. OTHERWISE THE GRADING IN A+ WONT WORK

'''
Todo: Implement the Exception classes ObjectIsNotDogObjectError and FeedingDogError.

ObjectIsNotDogObjectError should get the incorrect 'member'
tried to add. It needs to check which type it is, and tell the type in the message.

FeedingDogError is a superclass for its inheritors FeedingDogErrorMissingList, FeedingDogErrorNotFoodObject
and FeedingDogErrorObjectInListNotFoodObject.
'''

'''
Check the definitons of the classes from the exercise on A+
'''


class ObjectIsNotDogObjectError(Exception):

    #hint: use str(type())
    def __init__(self, member):
        self.member = member
        self.mytype = str(type(member))

    def __str__(self):
        return f"****** Exception: The object ({self.member}) you tried adding in the herd is not a dog object, but an object of {self.mytype}"



class FeedingDogError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class FeedingDogErrorMissingList(FeedingDogError):
    def __init__(self, msg=""):
        super().__init__("****** Exception: Dog object does not have a list of foods")


class FeedingDogErrorNotFoodObject(FeedingDogError):
    def __init__(self, msg=""):
        super().__init__("****** Exception: The object with which the dog is tried to be fed is not a food object")


class FeedingDogErrorObjectInListNotFoodObject(FeedingDogError):
    def __init__(self, msg=""):
        super().__init__("****** Exception: An object in dog's foodlist is not a food object")

