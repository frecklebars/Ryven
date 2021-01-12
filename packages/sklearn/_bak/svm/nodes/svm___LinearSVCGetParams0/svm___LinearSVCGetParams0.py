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
from sklearn.svm import LinearSVC


class LinearSVCGetParams_NodeInstance(NodeInstance):
    def __init__(self, params):
        super(LinearSVCGetParams_NodeInstance, self).__init__(params)
        tmp = LinearSVC()
        params = tmp.get_params()
        for key in params:
            self.create_new_output(type_="data", label=key, pos=-1)
        del tmp
        self.create_new_output(type_="data", label="param dict", pos=-1)
        # self.special_actions['action name'] = {'method': M(self.action_method)}
        # ...

    def update_event(self, input_called=-1):
        if input_called == 0:
            model = self.input(1)
            params = model.get_params()
            i = 0
            for param in params:
                self.set_output_val(i, params[param])
                i += 1
            self.set_output_val(i, params)

    def get_data(self):
        data = {}
        return data

    def set_data(self, data):
        pass

    def removing(self):
        pass
