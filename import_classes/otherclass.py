from useronly import User
class  Admin(User):
    def __init__(self,first_name,last_name,**other_info):
        super().__init__(first_name,last_name,**other_info)
        self.privileges=Pri()
class Pri():#将previliges设置成class
    def __init__(self,*user_privileges):
        self.user_privileges=('can_delete_users','can_add_post','can_ban_user')
    def show_privileges(self):
            print("用户权限: " , end='')
            for _ in self.user_privileges:
                print(_,end=' ')#加入空格让权限分开