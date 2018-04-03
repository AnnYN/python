class User:#不继承不需要括号
    def __init__(self,first_name,last_name,**other_info):
        self.first_name=first_name
        self.last_name=last_name
        self.other_info=other_info
    def des_user(self):
        profile={}
        profile['first name']=self.first_name
        profile['last name']=self.last_name
        for key,value in self.other_info.items():
            profile[key]=value
        return profile
    def greet_user(self):
        print("Hello, "+self.first_name+' '+self.last_name)