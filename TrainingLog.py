class TrainingLog:
    def __init__(self):
        self._h1 = ["Training", "Validation"]
        self._h2 = ["Progress", "Loss", "Accuracy"]
        
        self.current_epoch = 0
        self.initialize_row()

        self.at_empty_row = True

    def initialize_row(self):
        self.tpt = ''
        self.tl = self.ta = ''

        self.vpt = ''
        self.vl = self.va = ''

    def print_header(self):
        print("\n|{:^7}|{:^42}|{:^42}|".format("", "Training", "Validation"))
        print("|{:^7}|{:-^42}|{:-^42}|".format('Epoch', '', ''))
        print("|{:^7}|{:^20}|{:^10}|{:^10}|{:^20}|{:^10}|{:^10}|".format('', 'Progress', 'Loss', 'Accuracy', 'Progress', 'Loss', 'Accuracy'))
        print("|" + "|".join(['-'*7] + ['-'*20, '-'*10, '-'*10]*2) + "|")
        self.at_empty_row = True

    def clear_row(self):
        print("\r", end='')
        self.at_empty_row = True

    def new_row(self):
        if self.at_empty_row:
            return
        print('')
        self.at_empty_row = True
        self.initialize_row()

    def print_row(self):
        if not self.at_empty_row:
            self.new_row()
        f = "|{:^7}|{:^20}|{:^10}|{:^10}|{:^20}|{:^10}|{:^10}|"
        print(f.format(self.current_epoch,
                       self.tpt, self.tl, self.ta,
                       self.vpt, self.vl, self.va), end='')
        self.at_empty_row = False

    def update_row(self, epoch_num=None,
                   tp=None, tt=None, tl=None, ta=None,
                   vp=None, vt=None, vl=None, va=None):
        """
        Updates the current row with provided values

        args:
            epoch_num: Current epoch number
            tp: Training Progress
            tt: Current training duration
            tl: Training Loss
            ta: Training Accuracy
            vp: Validation Progress
            vt: Current validation duration
            vl: Validation Loss
            va: Validation Accuracy

        prints:
            Log of current row.
        """
        if epoch_num:
            self.current_epoch = epoch_num

        if tp and tt:
            self.tpt = "{:.2%} ({:.2F}s)".format(tp, tt)
        
        if tl:
            self.tl = "{:.4F}".format(tl)

        if ta:
            self.ta = "{:.2%}".format(ta)

        if vp and vt:
            self.vpt = "{:.2%} ({:.2F}s)".format(vp, vt)
        
        if vl:
            self.vl = "{:.4F}".format(vl)

        if va:
            self.va = "{:.2%}".format(va)

        self.clear_row()
        self.print_row()

    def finish(self):
        if not self.at_empty_row:
            self.new_row()
        print("|" + "-".join(['-'*7] + ['-'*20, '-'*10, '-'*10]*2) + "|", end='\n\n')
        
        
