from tkinter import *
import threading
import time

track_lock_1 = threading.Lock()
track_lock_2 = threading.Lock()
track_lock_3 = threading.Lock()
track_lock_4 = threading.Lock()
track_lock_5 = threading.Lock()
track_lock_6 = threading.Lock()

class TremController():

    def initialize_var(self):
        self.trem_1_distance = -1
        self.trem_2_distance = -1
        self.trem_3_distance = -1
        self.trem_4_distance = -1
        self.trem_1_speed = 1 / 15
        self.trem_2_speed = 1 / 15
        self.trem_3_speed = 1 / 15
        self.trem_4_speed = 1 / 15

    def setup_interface(self):
        self.root = Tk()
        self.root.title('Problema dos 4 Trens')
        self.root.geometry('600x900')
        self.root.config(bg='#fff')
        self.canvas = Canvas(self.root, height=850, width=900, bg="white")
        self.canvas.pack()
        return self.root, self.canvas

    def setup_trilhos(self):
        self.canvas.create_rectangle(20, 30, 195, 195, outline="gold", width=5)
        self.canvas.create_rectangle(205, 30, 370, 195, outline="violet", width=5)
        self.canvas.create_rectangle(380, 30, 542, 195, outline="turquoise", width=5)
        self.canvas.create_rectangle(20, 205, 542, 375, outline="springgreen", width=5)

    def setup_trens(self):
        self.trem_1 = self.canvas.create_rectangle(20, 20, 40, 40, fill="gold")
        self.trem_2 = self.canvas.create_rectangle(200, 20, 220, 40, fill="violet")
        self.trem_3 = self.canvas.create_rectangle(375, 20, 395, 40, fill="turquoise")
        self.trem_4 = self.canvas.create_rectangle(20, 190, 40, 210, fill="springgreen")

    def move_trem_1(self):
        while True:
            self.trem_1_distance += 1
            while -1 < self.trem_1_distance < 16:
                self.canvas.move(self.trem_1, 10, 0)
                self.trem_1_distance += 1
                time.sleep(self.trem_1_speed)
            track_lock_1.acquire()
            while 16 <= self.trem_1_distance < 33:
                self.canvas.move(self.trem_1, 0, 10)
                self.trem_1_distance += 1
                time.sleep(self.trem_1_speed)
            track_lock_1.release()
            track_lock_2.acquire()
            while 33 <= self.trem_1_distance < 50:
                self.canvas.move(self.trem_1, -10, 0)
                self.trem_1_distance += 1
                time.sleep(self.trem_1_speed)
            track_lock_2.release()
            while 50 <= self.trem_1_distance < 67:
                self.canvas.move(self.trem_1, 0, -10)
                self.trem_1_distance += 1
                time.sleep(self.trem_1_speed)
            if self.trem_1_distance == 67:
                self.trem_1_distance = -1
                self.canvas.move(self.trem_1, 10, 0)
                time.sleep(self.trem_1_speed)

    def move_trem_2(self):
        while True:
            self.trem_2_distance += 1
            while -1 < self.trem_2_distance < 16:
                self.canvas.move(self.trem_2, 10, 0)
                self.trem_2_distance += 1
                time.sleep(self.trem_2_speed)
            track_lock_3.acquire()
            while 16 <= self.trem_2_distance < 33:
                self.canvas.move(self.trem_2, 0, 10)
                self.trem_2_distance += 1
                time.sleep(self.trem_2_speed)
            track_lock_3.release()
            track_lock_4.acquire()
            while 33 <= self.trem_2_distance < 50:
                self.canvas.move(self.trem_2, -10, 0)
                self.trem_2_distance += 1
                time.sleep(self.trem_2_speed)
            track_lock_4.release()
            track_lock_1.acquire()
            while 50 <= self.trem_2_distance < 67:
                self.canvas.move(self.trem_2, 0, -10)
                self.trem_2_distance += 1
                time.sleep(self.trem_2_speed)
            track_lock_1.release()
            if self.trem_2_distance == 67:
                self.trem_2_distance = -1
                self.canvas.move(self.trem_2, 10, 0)
                time.sleep(self.trem_2_speed)

    def move_trem_3(self):
        while True:
            self.trem_3_distance += 1
            while -1 < self.trem_3_distance < 16:
                self.canvas.move(self.trem_3, 10, 0)
                self.trem_3_distance += 1
                time.sleep(self.trem_3_speed)
            while 16 <= self.trem_3_distance < 33:
                self.canvas.move(self.trem_3, 0, 10)
                self.trem_3_distance += 1
                time.sleep(self.trem_3_speed)
            track_lock_5.acquire()
            while 33 <= self.trem_3_distance < 50:
                self.canvas.move(self.trem_3, -10, 0)
                self.trem_3_distance += 1
                time.sleep(self.trem_3_speed)
            track_lock_5.release()
            track_lock_3.acquire()
            while 50 <= self.trem_3_distance < 67:
                self.canvas.move(self.trem_3, 0, -10)
                self.trem_3_distance += 1
                time.sleep(self.trem_3_speed)
            track_lock_3.release()
            if self.trem_3_distance == 67:
                self.trem_3_distance = -1
                self.canvas.move(self.trem_3, 10, 0)
                time.sleep(self.trem_3_speed)

    def move_trem_4(self):
        while True:
            self.trem_4_distance += 1
            track_lock_2.acquire()
            track_lock_4.acquire()
            track_lock_5.acquire()
            while -1 < self.trem_4_distance < 16:
                self.canvas.move(self.trem_4, 10, 0)
                self.trem_4_distance += 1
                time.sleep(self.trem_4_speed)
            track_lock_2.release()
            while 16 <= self.trem_4_distance < 33:
                self.canvas.move(self.trem_4, 10, 0)
                self.trem_4_distance += 1
                time.sleep(self.trem_4_speed)
            track_lock_4.release()
            while 33 <= self.trem_4_distance < 50:
                self.canvas.move(self.trem_4, 10, 0)
                self.trem_4_distance += 1
                time.sleep(self.trem_4_speed)
            track_lock_5.release()
            while 50 <= self.trem_4_distance < 67:
                self.canvas.move(self.trem_4, 0, 10)
                self.trem_4_distance += 1
                time.sleep(self.trem_4_speed)
            while 67 <= self.trem_4_distance < 118:
                self.canvas.move(self.trem_4, -10, 0)
                self.trem_4_distance += 1
                time.sleep(self.trem_4_speed)
            while 118 <= self.trem_4_distance < 135:
                self.canvas.move(self.trem_4, 0, -10)
                self.trem_4_distance += 1
                time.sleep(self.trem_4_speed)
            if self.trem_4_distance == 135:
                self.trem_4_distance = -1
                self.canvas.move(self.trem_4, 10, 0)
                time.sleep(self.trem_4_speed)

    def setup_control_panel(self):
        controls = [
            {"text": "Trem 1", "color": "gold", "command": self.update_trem_1_speed, "speed": self.trem_1_speed, "x": 180},
            {"text": "Trem 2", "color": "violet", "command": self.update_trem_2_speed, "speed": self.trem_2_speed, "x": 250},
            {"text": "Trem 3", "color": "turquoise", "command": self.update_trem_3_speed, "speed": self.trem_3_speed, "x": 320},
            {"text": "Trem 4", "color": "springgreen", "command": self.update_trem_4_speed, "speed": self.trem_4_speed, "x": 390},
        ]
        for control in controls:
            self.canvas.create_rectangle(control["x"]-20, 440, control["x"]+20, 630, outline="lightgray")
            self.canvas.create_text(control["x"], 415, text=control["text"], font="Helvetica 12 bold", fill=control["color"])
            scale = Scale(self.root, from_=20, to=1, orient=VERTICAL, length=180, command=control["command"])
            scale.set(10)
            self.canvas.create_window(control["x"], 535, window=scale)

    def update_trem_1_speed(self, val):
        if int(val) == 0:
            self.train_1_speed = 0
        self.trem_1_speed = 1 / int(val)

    def update_trem_2_speed(self, val):
        if int(val) == 0:
            self.train_2_speed = 0
        self.trem_2_speed = 1 / int(val)

    def update_trem_3_speed(self, val):
        if int(val) == 0:
            self.train_3_speed = 0
        self.trem_3_speed = 1 / int(val)

    def update_trem_4_speed(self, val):
        if int(val) == 0:
            self.train_4_speed = 0
        self.trem_4_speed = 1 / int(val)

    def start(self):
        t1 = threading.Thread(target=self.move_trem_1)
        t2 = threading.Thread(target=self.move_trem_2)
        t3 = threading.Thread(target=self.move_trem_3)
        t4 = threading.Thread(target=self.move_trem_4)
        t1.daemon = True
        t2.daemon = True
        t3.daemon = True
        t4.daemon = True
        t1.start()
        t2.start()
        t3.start()
        t4.start()
        self.root.mainloop()

if __name__ == "__main__":
    controller = TremController()
    controller.initialize_var()
    controller.setup_interface()
    controller.setup_trilhos()
    controller.setup_trens()
    controller.setup_control_panel()
    controller.start()


