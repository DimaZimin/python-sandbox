class SshClient:

    def __init__(self):
        self.running = False

    def create_connection(self):
        self.running = True
        print('Created SSH connection')

    def execute_command(self, command):
        print('Executing "{}"'.format(command))
        return '"{}" execution output'.format(command)

    def disconnect(self):
        self.running = False
        print('Stopped SSH connection')
