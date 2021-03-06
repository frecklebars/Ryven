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
from sklearn.feature_selection import RFE


class RFE_NodeInstance(NodeInstance):
    def __init__(self, params):
        super(RFE_NodeInstance, self).__init__(params)

        # self.special_actions['action name'] = {'method': M(self.action_method)}
        # ...

    def update_event(self, input_called=-1):
        if input_called == 0:
            estimator = self.input(2)
            selector = RFE(estimator)
            if self.input(1) != None:
                selector.set_params(**self.input(1))
            try:
                X = self.input(3)
                y = self.input(4)

                selector.fit(X, y)
            except:
                pass
            
            self.set_output_val(1, selector)
            self.exec_output(0)
            

    def get_data(self):
        data = {}
        return data

    def set_data(self, data):
        pass

    def removing(self):
        pass
