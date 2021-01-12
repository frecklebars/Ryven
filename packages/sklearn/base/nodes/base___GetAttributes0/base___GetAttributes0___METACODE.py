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
        self.special_actions['generate attribute outputs'] = {'method': M(self.init_attribute_ports)}
        self.ready = False
        # self.special_actions['action name'] = {'method': M(self.action_method)}
        # ...

    def update_event(self, input_called=-1):
        if self.ready:
            est = self.input(0)
            attributes = [i for i in dir(est) if (i[-1] == "_" and i[0] != "_")]
            attri = 0
            for attr in attributes:
                try:
                    self.set_output_val(attri, getattr(est, attr))
                except:
                    self.set_output_val(attri, None)
                attri += 1

    def init_attribute_ports(self):
        if self.input(0) == None:
            return
        est = self.input(0)
        for i in range(len(self.outputs)):
            self.delete_output(0)
        attributes = [i for i in dir(est) if (i[-1] == "_" and i[0] != "_")]
        attri = 0
        for attr in attributes:
            self.create_new_output(type_="data", label=attr, pos=-1)
            try:
                self.set_output_val(attri, getattr(est, attr))
            except:
                self.set_output_val(attri, None)
            attri += 1
        self.ready = True    

    def get_data(self):
        data = {}
        return data

    def set_data(self, data):
        pass

    def removing(self):
        pass
