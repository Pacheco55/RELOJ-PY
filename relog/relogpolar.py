import tkinter as tk
from tkinter import ttk
import time
import math
import datetime
from pygame import mixer
from tkinter import messagebox

class Clock(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Reloj Digital/Análogo")
        self.geometry("400x600")
        
        # Inicializar mixer para los sonidos
        mixer.init()
        
        # Variables
        self.clock_type = tk.StringVar(value="digital")
        self.alarm_time = None
        self.alarm_active = False
        
        self.create_widgets()
        self.update_clock()
        
    def create_widgets(self):
        # Selector de tipo de reloj
        ttk.Label(self, text="Tipo de Reloj:").pack(pady=5)
        ttk.Radiobutton(self, text="Digital", variable=self.clock_type, 
                       value="digital", command=self.switch_clock).pack()
        ttk.Radiobutton(self, text="Análogo", variable=self.clock_type, 
                       value="analog", command=self.switch_clock).pack()
        
        # Canvas para el reloj
        self.clock_canvas = tk.Canvas(self, width=300, height=300, bg='white')
        self.clock_canvas.pack(pady=20)
        
        # Frame para la alarma
        alarm_frame = ttk.LabelFrame(self, text="Configurar Alarma")
        alarm_frame.pack(pady=10, padx=10, fill="x")
        
        # Entrada de hora para alarma
        self.hour_var = tk.StringVar(value="00")
        self.minute_var = tk.StringVar(value="00")
        
        ttk.Label(alarm_frame, text="Hora:").pack(side=tk.LEFT, padx=5)
        ttk.Entry(alarm_frame, textvariable=self.hour_var, width=3).pack(side=tk.LEFT)
        ttk.Label(alarm_frame, text="Minuto:").pack(side=tk.LEFT, padx=5)
        ttk.Entry(alarm_frame, textvariable=self.minute_var, width=3).pack(side=tk.LEFT)
        
        # Botones de alarma
        ttk.Button(alarm_frame, text="Activar Alarma", 
                  command=self.set_alarm).pack(side=tk.LEFT, padx=5)
        ttk.Button(alarm_frame, text="Desactivar Alarma", 
                  command=self.disable_alarm).pack(side=tk.LEFT, padx=5)
        
        ttk.Label(text="Creado en PIXELBITS Studios").pack(side=tk.LEFT, padx=5)
        ttk.Label(text="    por PACHECO JULIO").pack(side=tk.LEFT, padx=5)

        
    def switch_clock(self):
        self.clock_canvas.delete("all")
        self.update_clock()
        
    def draw_analog_clock(self, hours, minutes, seconds):
        # Dibujar círculo del reloj
        self.clock_canvas.create_oval(10, 10, 290, 290)
        
        # Dibujar números
        for i in range(12):
            angle = i * math.pi/6 - math.pi/2
            x = 150 + 140 * math.cos(angle)
            y = 150 + 140 * math.sin(angle)
            self.clock_canvas.create_text(x, y, text=str(i+1))
        
        # Manecillas
        # Segundos
        second_angle = seconds * math.pi/30 - math.pi/2
        second_x = 150 + 120 * math.cos(second_angle)
        second_y = 150 + 120 * math.sin(second_angle)
        self.clock_canvas.create_line(150, 150, second_x, second_y, fill='red')
        
        # Minutos
        minute_angle = (minutes + seconds/60) * math.pi/30 - math.pi/2
        minute_x = 150 + 100 * math.cos(minute_angle)
        minute_y = 150 + 100 * math.sin(minute_angle)
        self.clock_canvas.create_line(150, 150, minute_x, minute_y, width=3)
        
        # Horas
        hour_angle = (hours + minutes/60) * math.pi/6 - math.pi/2
        hour_x = 150 + 80 * math.cos(hour_angle)
        hour_y = 150 + 80 * math.sin(hour_angle)
        self.clock_canvas.create_line(150, 150, hour_x, hour_y, width=5)
        
    def draw_digital_clock(self, hours, minutes, seconds):
        time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        self.clock_canvas.create_text(150, 150, text=time_str, 
                                    font=('Arial', 36, 'bold'))
        
    def update_clock(self):
        current_time = datetime.datetime.now()
        hours, minutes, seconds = current_time.hour, current_time.minute, current_time.second
        
        self.clock_canvas.delete("all")
        
        if self.clock_type.get() == "digital":
            self.draw_digital_clock(hours, minutes, seconds)
        else:
            self.draw_analog_clock(hours, minutes, seconds)
            
        # Verificar alarma
        if self.alarm_active and self.alarm_time:
            if (hours, minutes) == self.alarm_time:
                self.trigger_alarm()
                
        # Sonido cada hora
        if minutes == 0 and seconds == 0:
            self.play_hourly_sound()
            
        self.after(1000, self.update_clock)
        
    def set_alarm(self):
        try:
            hour = int(self.hour_var.get())
            minute = int(self.minute_var.get())
            if 0 <= hour < 24 and 0 <= minute < 60:
                self.alarm_time = (hour, minute)
                self.alarm_active = True
                messagebox.showinfo("Alarma", "Alarma configurada correctamente")
            else:
                messagebox.showerror("Error", "Hora no válida")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese números válidos")
            
    def disable_alarm(self):
        self.alarm_active = False
        self.alarm_time = None
        messagebox.showinfo("Alarma", "Alarma desactivada")
        
    def trigger_alarm(self):
        try:
            mixer.music.load("alarm.mp3")  # Asegúrate de tener este archivo
            mixer.music.play()
        except:
            messagebox.showinfo("Alarma", "¡Hora de la alarma!")
            
    def play_hourly_sound(self):
        try:
            mixer.music.load("hour.mp3")  # Asegúrate de tener este archivo
            mixer.music.play()
        except:
            print("Marca de hora")

if __name__ == "__main__":
    app = Clock()
    app.mainloop()