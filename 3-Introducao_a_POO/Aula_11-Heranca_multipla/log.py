class LogMixin:
    @staticmethod
    def write(msg):
        with open('log.txt', 'a+') as f:
            f.write(f'{msg}\n')

    def log_info(self, msg):
        self.write(f'INFO: {msg}')

    def log_error(self, msg):
        self.write(f'ERROR: {msg}')


