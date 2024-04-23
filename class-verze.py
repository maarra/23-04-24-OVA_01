import pickle

class IntegerListManager:
    def __init__(self, filename = 'data.pkl'):
        self.filename = filename

    def save_data(self, data):
        '''Save list of integers to a file using pickle.'''
        with open(self.filename, 'wb') as file:
            pickle.dump(data, file)

    def load_data(self):
        with open(self.filename, 'rb') as file:
            return pickle.load(file)

    def run(self):
        user_input = input('Vloz list cislic separovanych mezerou ')
        int_list = [int(item) for item in user_input.split()]
        filename = 'data.pkl'
        self.save_data(int_list)
        loaded_list = self.load_data()
        print(f'nactenea data ze souboru {loaded_list}')

if __name__ == '__main__':
    manager = IntegerListManager()
    manager.run()
    print(manager.load_data())
# 64645
