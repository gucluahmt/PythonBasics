#define functions as steps to login

def enter_username(username):
    print('*********Login page*******')
    uname = input('enter your username')
    print(f'you entered {uname}')

def enter_password():
    pword = input('enter your password:')
    print(f'you entered *******{pword[-2:]}')

def click_login():
    print('login was clicked')
    print('you successfully logged in')

def logout():
    print('logging out')
    print('you successfully log out')

enter_username('jhon')
enter_password()
click_login()

