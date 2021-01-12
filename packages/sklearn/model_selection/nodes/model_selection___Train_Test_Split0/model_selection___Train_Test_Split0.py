from NIENV import *


# API METHODS --------------

# self.main_widget
# self.update_shape()

# Ports
# self.input(index)
# self.set_output_val(index, val)
# self.exec_output(index)

# self.create_new_input(type_, label, widget_name=None, widget_pos='under', pos=-1)
# self.delete_input(index)
# self.create_new_output(type_, label, pos=-1)
# self.delete_output(index)

# Logging
# mylog = self.new_log('Example Log')
# mylog.log('I\'m alive!!')
# self.log_message('hello global!', target='global')
# self.log_message('that\'s not good', target='error')

# --------------------------
from sklearn.model_selection import train_test_split


class Train_Test_Split_NodeInstance(NodeInstance):
    def __init__(self, params):
        super(Train_Test_Split_NodeInstance, self).__init__(params)

        # self.special_actions['action name'] = {'method': M(self.action_method)}
        # ...

    def update_event(self, input_called=-1):
        X = self.input(0)
        y = self.input(1)
        
        # defaults:
        test_size = None if self.input(2) == "" else self.input(2)
        train_size = None if self.input(3) == "" else self.input(3)
        random_state = None if self.input(4) == "" else self.input(4)
        shuffle = True if self.input(5) == "" else self.input(5)
        stratify = None if self.input(6) == "" else self.input(6)
        y_train = None
        y_test = None

        try:
            try:
                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, train_size=train_size, random_state=random_state, shuffle=shuffle, stratify=stratify)
            except:
                X_train, X_test = train_test_split(X, test_size=test_size, train_size=train_size, random_state=random_state, shuffle=shuffle, stratify=stratify)

            self.set_output_val(0, X_train)
            self.set_output_val(1, y_train)
            self.set_output_val(2, X_test)
            self.set_output_val(3, y_test)
        except:
            pass

    def get_data(self):
        data = {}
        return data

    def set_data(self, data):
        pass

    def removing(self):
        pass
