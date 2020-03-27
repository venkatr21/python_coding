def decorate(func):
    def make():
        print('add beginning')
        func()
        print('add end')
    return make()
