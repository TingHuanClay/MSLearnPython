def logger(func):
    def wrapper():
        print('========== Logging  [START]    ==========')
        func()
        print('========== Logging  [FINISHED] ==========')
    return wrapper


@logger
def sample():
    print('--- Inside a sample function ---')

sample()