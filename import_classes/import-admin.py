from  user import  Admin
yanan=Admin('liu','yanan',age=24,role='student')
print(yanan.des_user())
print(yanan.greet_user())
yanan.privileges.show_privileges()