from weather_subject import WeatherSubject
from phone_observer import PhoneObserver
from led_observer import LEDObserver
if __name__=="__main__":
    subj1=WeatherSubject()
    ph1=PhoneObserver()
    ph2=PhoneObserver()
    led1=LEDObserver()
    subj1.attach(ph1)
    subj1.attach(ph2)
    subj1.attach(led1)
    subj1.set_state("30 degrees")