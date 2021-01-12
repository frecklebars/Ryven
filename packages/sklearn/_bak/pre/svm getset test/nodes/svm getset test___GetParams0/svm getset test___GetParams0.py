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


class GetParams_NodeInstance(NodeInstance):
    def __init__(self, params):
        super(GetParams_NodeInstance, self).__init__(params)
        self.special_actions['generate param outputs'] = {'method': M(self.init_param_ports)}
        self.ready = False
        # self.special_actions['action name'] = {'method': M(self.action_method)}
        # ...

    def update_event(self, input_called=-1):
        if self.ready:
            params = self.input(0).get_params()
            i = 0
            for key in params:
                self.set_output_val(i, params[key])
                i += 1
            self.set_output_val(i, params)
                

    def init_param_ports(self):
        if self.input(0) == None:
            return
        model = self.input(0)
        for i in range(len(self.outputs)):
            self.delete_output(0)
        params = model.get_params()
        keyi = 0
        for key in params:
            self.create_new_output(type_="data", label=key, pos=-1)
            self.set_output_val(keyi, params[key])
            keyi += 1
        self.create_new_output(type_="data", label="params dict", pos=-1)
        self.set_output_val(keyi, params)
        self.ready = True

    def get_data(self):
        data = {}
        return data

    def set_data(self, data):
        pass

    def removing(self):
        pass
