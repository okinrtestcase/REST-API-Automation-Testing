import time

def print_test_info(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        
        print("\nAuthor : Everythink")
        print("Test Name :", func.__name__)
        print("Date :", time.strftime("%A %Y-%m-%d\n"))
        return result
    return wrapper

# test auth
@print_test_info
def check_register_success(response):
    if response.status_code == 200:
        print("Register Success...")
        print("Status Code:", response.status_code)
        return True
    return False

@print_test_info
def check_register_failure(response):
    if response.status_code == 400:
        print("Register Failure!")
        print("Status Code:", response.status_code)
        return True
    return False

@print_test_info
def check_login_success(response):
    if response.status_code == 200:
        print("Login Success...")
        print("Status Code:", response.status_code)
        return True
    return False

@print_test_info
def check_login_failure(response):
    if response.status_code == 400 :
        print("Login Failure!")
        print("Status Code:", response.status_code)
        return True
    return False

@print_test_info
def check_login_failure_3_attempts(response):
    if response.status_code == 200 :
        print("Login Failure After 3 Attempts...")
        print("Status Code:", response.status_code)
        return True
    return False

# test crud
@print_test_info
def check_get_all_users(response):
    if response.status_code == 200 :
        print("User Appeared...")
        print("Status Code:", response.status_code)
        return True
    return False
@print_test_info
def check_get_specifics_users(response):
    if response.status_code == 200 :
        print("User Appeared...")
        print("Status Code:", response.status_code)
        return True
    return False
@print_test_info
def check_create_users(response):
    if response.status_code == 201 :
        print("User Created...")
        print("Status Code:", response.status_code)
        return True
    return False
@print_test_info
def check_update_users(response):
    if response.status_code == 200 :
        print("User Updated...")
        print("Status Code:", response.status_code)
        return True
    return False
@print_test_info
def check_delete_users(response):
    if response.status_code == 204 :
        print("User Deleted...")
        print("Status Code:", response.status_code)
        return True
    return False

