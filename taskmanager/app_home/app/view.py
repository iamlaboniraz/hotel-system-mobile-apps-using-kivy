from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import StringProperty, NumericProperty
from kivy.properties import ObjectProperty
from kivy.metrics import sp, dp
from kivy.utils import rgba
from kivy.uix.modalview import ModalView
from kivy.garden.circulardatetimepicker import CircularTimePicker as CTP
from kivy.uix.button import Button
from app.storage.db import Database
from kivy.core.window import Window
from datetime import datetime


class NewTask(ModalView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get_time(self):
        mv = ModalView(size_hint=[.8, .6])
        box = BoxLayout(orientation='vertical', size_hint=[.5, .5])
        mv.add_widget(box)
        cl = CTP(color=[1, 1, 1, 1])
        cl.bind(time=self.set_time)
        submit = Button(text='OK', background_normal='',
                        color=rgba('#0e1574'), background_color=[1, 1, 1, 1],
                        size_hint_y=.2)
        submit.bind(on_release=lambda x: self.update_time(cl.time, mv))
        box.add_widget(cl)
        box.add_widget(submit)
        mv.open()

    def set_time(self, inst, value):
        print(value)

    def update_time(self, checkin, mv):
        mv.dismiss()
        self.ids.task_checkin.text = str(checkin)

    def get_time2(self):
        mv1 = ModalView(size_hint=[.8, .6])
        box1 = BoxLayout(orientation='vertical', size_hint=[.5, .5])
        mv1.add_widget(box1)
        cl1 = CTP(color=[1, 1, 1, 1])
        cl1.bind(time=self.set_time2)
        submit = Button(text='OK', background_normal='',
                        color=rgba('#0e1574'), background_color=[1, 1, 1, 1],
                        size_hint_y=.2)
        submit.bind(on_release=lambda x: self.update_time2(cl1.time, mv1))
        box1.add_widget(cl1)
        box1.add_widget(submit)
        mv1.open()

    def set_time2(self, inst, value):
        print(value)

    def update_time2(self, checkout, mv1):
        mv1.dismiss()
        self.ids.task_checkout.text = str(checkout)


class NewButton(ButtonBehavior, BoxLayout):
    pass


# class Task(ButtonBehavior, BoxLayout):
#     name = StringProperty('')
#     time = StringProperty('')
#
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
class Task(ButtonBehavior, BoxLayout):
    rooms = StringProperty('')
    checkin = StringProperty('')
    date1 = StringProperty('')
    checkout = StringProperty('')
    date2 = StringProperty('')
    room_type = StringProperty('')
    NumOfAdults = ObjectProperty('')
    NumOfChild = ObjectProperty('')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        btn3 = Button(text='view',background_color=rgba('#0088aafd'),size_hint =(.4, .4),
                pos_hint ={'x':.2, 'y':.2})
        btn3.bind(on_press=lambda x: self.view_tasks())
        # self.bind(on_release=lambda x: self.view_task())
        self.add_widget(btn3)

    def view_tasks(self):
        vt = ViewTask()
        vt.ids.rooms.text = "Guest Name ="+self.rooms
        vt.ids.checkin.text =  "CheckIn Date "+self.checkin
        vt.ids.date1.text = "(Time "+self.date1+")"
        vt.ids.checkout.text = "CheckOut Date "+self.checkout
        vt.ids.date2.text = "(Time "+self.date2+")"
        vt.ids.room_type.text = "Room Type = "+self.room_type
        vt.ids.NumOfAdults.text = "Number of Adult = "+self.NumOfAdults
        vt.ids.NumOfChild.text = "Number of Children = "+self.NumOfChild
        vt.open()


class roomss(ButtonBehavior, BoxLayout):
    rooms_number = StringProperty('')
    room_type = StringProperty('')
    facility = ObjectProperty('')
    price = ObjectProperty('')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class ViewTask(ModalView):
    pass


class Today(Task):
    pass


class Upcoming(Task):
    pass


class BestRoom(roomss):
    pass


class MainWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.db = Database()
        self.init_view()

    # def init_view(self):
    #     all_tasks = self.db.get_task()
    #     scroll_parent = Window
    #     tw = self.ids.today_wrapper
    #     uw = self.ids.upcoming_wrapper
    #     for t in all_tasks:
    #         checkin, date1 = t[2], t[2]
    #         if self.clear_date(date1):
    #             task = Today()
    #             task.rooms = t[1]
    #             task.date1 = date1
    #             task.checkin = checkin
    #             task.checkout, task.date2 = t[3], t[3]
    #             task.room_type = t[4]
    #             task.NumOfAdults = t[5]
    #             task.NumOfChild = t[6]
    #             task.size_hint = (None, 1)
    #             task.size = [scroll_parent.width / 2.4, 45]
    #             tw.add_widget(task)
    #         else:
    #             task = Upcoming()
    #             task.rooms = t[1]
    #             task.checkin = ''.join(date1)
    #             task.checkin = checkin
    #             task.checkout, task.date2 = t[3], t[3]
    #             task.room_type = t[4]
    #             task.NumOfAdults = t[5]
    #             task.NumOfChild = t[6]
    #             task.size_hint = (1, None)
    #             task.height = dp(100)
    #             uw.add_widget(task)

    def init_view(self):
        all_tasks = self.db.get_task()
        scroll_parent = Window
        tw = self.ids.today_wrapper
        for t in all_tasks:
            task = Today()
            task.rooms = t[1]
            task.checkin,task.date1 = t[2],t[3]
            print(task.checkin,task.date1)
            task.checkout, task.date2 = t[4], t[5]
            print(task.checkout, task.date2)
            # task.checkout = t[3]
            task.room_type = t[6]
            # task.checkin, task.date1 = t[2], t[3]
            # print(task.checkin, task.date1)
            task.NumOfAdults = t[7]
            task.NumOfChild = t[8]
            task.size_hint = (None, 1)
            # task.size = [100,200]
            task.size = [scroll_parent.width / 2.4, 45]

            itask = Today()
            itask.rooms = t[1]
            itask.room_type = t[6]
            itask.checkin, itask.date1 = t[2], t[3]
            itask.size_hint = (None, None)
            itask.size = [scroll_parent.width / 2.4,
                          round(scroll_parent.height / 3)]

            tw.add_widget(task)
            self.ids.all_today.add_widget(itask)

    def clear_date(self, date: str):
        today = datetime.today()
        _date = date.split('/')
        print("date = ", _date)
        if len(_date) < 3:
            _date = date.split('-')
        date_ = [int(x) for x in reversed(_date)]
        print(date_)
        task_date = datetime(date_[0], date_[1], date_[2])
        x = abs((today - task_date).days)
        print(x)
        if x == 0:
            return True
        else:
            return False
    def get_update(self,inst):
        nt = NewTask()
        nt.ids.task_rooms.text = inst.rooms
        nt.ids.task_checkin.text = inst.date1
        nt.ids.task_date1.text = inst.checkin
        nt.ids.task_checkout.text = inst.date2
        nt.ids.task_date2.text = inst.checkout
        nt.ids.task_room_type.text = inst.room_type
        nt.ids.task_adults.text = inst.NumOfAdults
        nt.ids.task_child.text = inst.NumOfChild
        nt.ids.submit_wrapper.clear_widgets()
        submit = Button(text='Update Reserve',background_normal='',
                        background_color=rgba('#0e5174'))
        submit.bind(on_release=lambda x:self.update_task(nt,inst))
        nt.ids.submit_wrapper.add_widget(submit)
        nt.open()

    def update_task(self,task_data,task):
        xtask = [
            task_data.ids.task_rooms.text,
            task_data.ids.task_date1.text,
            task_data.ids.task_checkin.text,
            task_data.ids.task_date2.text,
            task_data.ids.task_checkout.text,

            task_data.ids.task_room_type.text,
            task_data.ids.task_adults.text,
            task_data.ids.task_child.text,
            task_data.ids.submit_wrapper.clear_widgets()

        ]
        error = None
        for t in xtask:
            if t is not None:
                if len(t)<1:
                    t.hint_text = 'Field required'
                    t.hint_text_color = [1,0,0,1]
                    error = True
        if error:
            pass
        else:
            # xtask = [xtask[0],''.join(xtask[1:]),task.rooms]
            if self.db.update_task(xtask):
                task.rooms = task_data.ids.task_rooms.text
                task.date1 = task_data.ids.task_checkin.text
                task.checkin = task_data.ids.task_date1.text
                task.date2 = task_data.ids.task_checkout.text
                task.checkout = task_data.ids.task_date2.text
                task.room_type = task_data.ids.task_room_type.text
                task.NumOfAdults = task_data.ids.task_adults.text
                task.NumOfChild = task_data.ids.task_child.text
        task_data.dismiss()

    def delete_task(self, task: Today):
        rooms = task.rooms
        if self.db.delete_task(rooms):
            task.parent.remove_widget(task)

    def add_new(self):
        nt = NewTask()
        nt.open()

    def add_task(self, mv, xtask: tuple):
        error = False
        scroll_parent = self.ids.scroll_parent
        tw = self.ids.today_wrapper
        for t in xtask:
            if len(t.text) < 1:
                t.hint_text = 'Field required'
                t.hint_text_color = [1, 0, 0, 1]
                error = True
        if error:
            pass
        else:
            task = Today()
            task.rooms = xtask[0].text
            task.checkin = xtask[2].text
            task.date1 = xtask[1].text
            task.checkout = xtask[4].text
            task.date2 = xtask[3].text
            task.room_type = xtask[5].text
            task.NumOfAdults = xtask[6].text
            task.NumOfChild = xtask[7].text
            task.size_hint = (None, None)
            task.size = [scroll_parent.width / 2.4,
                         scroll_parent.height -
                         (.1 * scroll_parent.height)]
            # add tasks1 to db
            # checkin_date = ''.join([xtask[1].text, xtask[2].text])
            # checkout_date = ''.join([xtask[3].text, xtask[4].text])
            task_ = (
                xtask[0].text, xtask[1].text, xtask[2].text, xtask[3].text, xtask[4].text, xtask[5].text, xtask[6].text,
                xtask[7].text)
            if self.db.add_task(task_):
                tw.add_widget(task)
            mv.dismiss()
            # check if we have enough tasks to show
            # if len(tw.children)>1:
            #     for child in tw.children:
            #         if type(child) == NewButton:
            #             tw.remove_widget(child)
            #             break
    def add_user(self,username,password):
        if len(username.text)<3 or len(password.text)<6:
            pass
        else:
            user = (username.text,password.text)
            if self.db.add_user(user):
                self.ids.scrn_mngr.current = 'scrn_signin'

    def auth_user(self, username, password):
        uname = username.text
        upass = password.text
        if self.db.auth_user((uname,upass)):
            self.ids.scrn_mngr.current = 'scrn_main'
        username.text=''
        password.text=''
