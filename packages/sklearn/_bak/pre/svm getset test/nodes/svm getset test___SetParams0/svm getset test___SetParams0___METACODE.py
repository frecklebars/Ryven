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


class %CLASS%(NodeInstance):
    def __init__(self, params):
        super(%CLASS%, self).__init__(params)
        self.special_actions['generate param outputs'] = {'method': M(self.init_param_ports)}
        self.ready = False
        # self.special_actions['action name'] = {'method': M(self.action_method)}
        # ...

    def update_event(self, input_called=-1):
        params = {}
        if self.ready:
            for i in range(len(self.inputs)):
                if self.input(i) != "":
                    params[self.inputs[i].label_str] = self.input(i)

            self.set_output_val(0, params)
        

    def init_param_ports(self):
        if self.input(0) == None:
            return
        model = self.input(0)
        self.delete_input(0)
        params = model.get_params()
        for key in params:
            self.create_new_input(type_="data", label=key, widget_name="std line edit l", widget_pos="besides", pos=-1)
        self.ready = True
        del self.special_actions['generate param outputs']

    def get_data(self):
        data = {}
        return data

    def set_data(self, data):
        pass

    def removing(self):
        pass
