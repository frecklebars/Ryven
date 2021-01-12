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
from sklearn.linear_model import LinearRegression


class %CLASS%(NodeInstance):
    def __init__(self, params):
        super(%CLASS%, self).__init__(params)

        # self.special_actions['action name'] = {'method': M(self.action_method)}
        # ...

    def update_event(self, input_called=-1):
        if input_called == 0:
            regr = LinearRegression()
            if self.input(1) != None:
                par = self.input(1)
                regr.set_params(**par)
            X = self.input(2)
            y = self.input(3)

            regr.fit(X, y)
    
            self.set_output_val(1, regr)
            self.set_output_val(2, regr.coef_)
            self.set_output_val(3, regr.rank_)
            self.set_output_val(4, regr.singular_)
            self.set_output_val(5, regr.intercept_)
            self.exec_output(0)

    def get_data(self):
        data = {}
        return data

    def set_data(self, data):
        pass

    def removing(self):
        pass
