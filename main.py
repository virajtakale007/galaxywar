from kivy.app import App
from kivy.uix.button import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.widget import Widget
import time
from kivy.properties import NumericProperty,ObjectProperty,ReferenceListProperty
from kivy.clock import Clock
from kivy.vector import Vector
from kivy.core.window import Window
from random import randint,choice
from kivy.core.audio import SoundLoader
class aliens4(Widget):
	target1_1_1_1:ObjectProperty(None)
	velocity_x=NumericProperty(0)
	velocity_y=NumericProperty(0)
	velocity=ReferenceListProperty(velocity_x,velocity_y)
	life=NumericProperty(10)
	def move(self):
		self.pos=Vector(*self.velocity)+self.pos
	
class aliens2(Widget):
	target1_1=ObjectProperty(None)
	target2_2=ObjectProperty(None)
	target3_3=ObjectProperty(None)
	target4_4=ObjectProperty(None)
	target5_5=ObjectProperty(None)
	target6_6=ObjectProperty(None)
	target7_7=ObjectProperty(None)
	target8_8=ObjectProperty(None)
	
	velocity_x=NumericProperty(0)
	velocity_y=NumericProperty(0)
	velocity=ReferenceListProperty(velocity_x,velocity_y)
	def move(self):
		self.pos=Vector(*self.velocity)+self.pos
class aliens3(Widget):
	target1_1_1=ObjectProperty(None)
	velocity_x=NumericProperty(0)
	velocity_y=NumericProperty(0)
	velocity=ReferenceListProperty(velocity_x,velocity_y)
	def move(self):
		self.pos=Vector(*self.velocity)+self.pos
class aliens(Widget):
	target1=ObjectProperty(None)
	target2=ObjectProperty(None)
	target3=ObjectProperty(None)
	target4=ObjectProperty(None)
	target5=ObjectProperty(None)
	target6=ObjectProperty(None)
	target7=ObjectProperty(None)
	target8=ObjectProperty(None)
	
	
	
	velocity_x=NumericProperty(0)
	velocity_y=NumericProperty(0)
	velocity=ReferenceListProperty(velocity_x,velocity_y)
	def move(self):
		self.pos=Vector(*self.velocity)+self.pos
class bullet(Widget):
	aim1=ObjectProperty(None)
	aim2=ObjectProperty(None)
	aim3=ObjectProperty(None)

	velocity_x=NumericProperty(0)
	velocity_y=NumericProperty(0)
	velocity=ReferenceListProperty(velocity_x,velocity_y)

	def move(self):
		self.pos=Vector(*self.velocity)+self.pos

class spaceship(Widget):
	ship=ObjectProperty(None)
	score=NumericProperty(0)
	life=NumericProperty(10)
	
class galaxianGame(Widget):
	
	invasion=ObjectProperty(None)
	pause_button=ObjectProperty(None)
	start_button=ObjectProperty(None)
	firing_button=ObjectProperty(None)
	exit_button=ObjectProperty(None)
	losing=ObjectProperty(None)
	saving=ObjectProperty(None)
	hard_button=ObjectProperty(None)
	medium_button=ObjectProperty(None)
	easy_button=ObjectProperty(None)
	resume=ObjectProperty(None)
	restart=ObjectProperty(None)
	back1=ObjectProperty(None)
	back2=ObjectProperty(None)
	initialize=ObjectProperty(None)
	
	start_time=NumericProperty(0)
	end_time=NumericProperty(0)
	sound_fire=SoundLoader.load("Fire.wav")
	sound_blast=SoundLoader.load("Blast.wav")
	sound=SoundLoader.load("vmusic.mp3")
	def closing(self):
		App.get_running_app().stop()
		Window.close()
	
	def boss(self,dt):
		list=[self.target1,self.target2,self.target3,self.target4,self.target5,self.target6,self.target7,self.target8,self.target1_1,self.target2_2,self.target3_3,self.target4_4,self.target5_5,self.target6_6,self.target7_7,self.target8_8,self.target1_1_1]
		for i in list :
			i.center_y=self.height+500
			
		j=self.target1_1_1_1
		if (j.center_y>self.height):
				j.velocity=Vector(randint(-5,5),-(randint(1,1)))

	
	def random(self):
		list=[self.target1,self.target2,self.target3,self.target4]
		for i in list:
			
			if (i.center_y>self.height) and self.target1_1_1_1.life!=1:
				i.velocity=Vector(randint(-5,5),-(randint(3,3)))
	
	def random2(self):
		list=[self.target5,self.target6,self.target7,self.target8]
		
		for i in list:
			if (i.center_y>self.height) and self.target1_1_1_1.life!=1:
				i.velocity=Vector(randint(-7,7),-(randint(3,3)))

				
				
	def random3(self,dt):
		i=self.target1_1_1
		
		if (i.center_y>self.height) and self.target1_1_1_1.life!=0:
			i.velocity=Vector(randint(-5,5),-(randint(2,2)))
			
	def random4(self,dt):
		list=[self.target1_1,self.target2_2,self.target3_3,self.target4_4,self.target5_5,self.target6_6,self.target7_7,self.target8_8]
		for i in list:
			
			if (i.center_y>self.height) and (self.target1_1_1_1.life!=0):
				i.velocity=Vector(randint(-8,8),-(randint(3,4)))
	
	def blast3(self):
		list=[self.target1,self.target2,self.target3,self.target4,self.target5,self.target6,self.target7,self.target8,self.target1_1,self.target2_2,self.target3_3,self.target4_4,self.target5_5,self.target6_6,self.target7_7,self.target8_8,self.target1_1_1]
		for i in list:
			if i.collide_widget(self.ship) and self.target1_1_1_1.life!=0:
				self.ship.life-=1
				i.center_y=self.height+100
				self.sound_blast.play()
				if self.ship.life==0:
					self.invasion.disabled=False
					self.invasion.opacity=1
					self.losing.disabled=False
					self.losing.opacity=1
					Clock.unschedule(self.update)
					self.firing_button.disabled=True
					self.firing_button.opacity=0
	
					self.restart.opacity=1
					self.restart.disabled=False
	tem=1
	def blast2(self):
		
		for i in (self.aim1,self.aim2,self.aim3):
			if i.collide_widget(self.target1_1_1_1):
				self.target1_1_1_1.life-=1
				self.sound_blast.play()
				i.center_y=self.ship.center_y+i.height/4
				i.center_x=self.ship.center_x
				i.velocity_y=0
				
				if self.target1_1_1_1.life ==0 and self.tem==1:
					self.restart.opacity=1
					self.restart.disabled=False
					self.target1_1_1_1.velocity=Vector(0,0)
					self.ship.score+=100
					self.saving.disabled=False
					self.saving.opacity=1
					tem=0
					self.target1_1_1_1.center_y=self.height+300
					self.firing_button.disabled=True
					self.sound.play()
					self.firing_button.opacity=0
					list=[self.target1,self.target2,self.target3,self.target4,self.target5,self.target6,self.target7,self.target8,self.target1_1,self.target2_2,self.target3_3,self.target4_4,self.target5_5,self.target6_6,self.target7_7,self.target8_8,self.target1_1_1]
					for i in list:
						i.velocity_y*=-1
				
	def blast1(self):
		list=[self.target1,self.target2,self.target3,self.target4,self.target5,self.target6,self.target7,self.target8,self.target1_1,self.target2_2,self.target3_3,self.target4_4,self.target5_5,self.target6_6,self.target7_7,self.target8_8,self.target1_1_1]
		for i in list:
			if self.aim1.collide_widget(i) and self.target1_1_1_1.life!=0:
				i.center_y=self.height+100
				self.aim1.center_y=self.ship.center_y+self.aim1.height/4
				self.aim1.center_x=self.ship.center_x
				self.aim1.velocity_y=0
				self.sound_blast.play()
				self.ship.score+=5
			elif self.aim2.collide_widget(i) and self.target1_1_1_1.life!=0:
				i.center_y=self.height+100
				self.aim2.center_y=self.ship.center_y+self.aim2.height/4
				self.aim2.center_x=self.ship.center_x
				self.aim2.velocity_y=0
				self.sound_blast.play()
				self.ship.score+=5
			elif self.aim3.collide_widget(i) and self.target1_1_1_1.life!=0:
				i.center_y=self.height+100
				self.aim3.center_y=self.ship.center_y+self.aim3.height/4
				self.aim3.center_x=self.ship.center_x
				self.aim3.velocity_y=0
				self.ship.score+=5
				self.sound_blast.play()
				

	def firing(self):
		
		self.sound_fire.play()
		if self.aim1.center_y<(self.ship.center_y+self.ship.height/2):
			self.aim1.velocity=Vector(0,25)
		elif self.aim2.center_y<(self.ship.center_y+self.ship.height/2):
			self.aim2.velocity=Vector(0,25)
		elif self.aim3.center_y<(self.ship.center_y+self.ship.height/2):
			self.aim3.velocity=Vector(0,25)
		
		
	
	def update(self,dt):
		self.aim1.move()
		self.aim2.move()
		self.aim3.move()
		self.blast1()
		self.blast2()
		self.blast3()
		list=[self.target1,self.target2,self.target3,self.target4,self.target5,self.target6,self.target7,self.target8,self.target1_1,self.target2_2,self.target3_3,self.target4_4,self.target5_5,self.target6_6,self.target7_7,self.target8_8,self.target1_1_1,self.target1_1_1_1]
		for i in list:
			i.move()
		
			if i.center_x<i.width/2 or i.center_x>self.width-i.width/2:
				if i.velocity_y>(-6):
					i.velocity_y*=self.value
				else:
					i.velocity_y=choice((-5,-6))
				if (-10)<i.velocity_x<(10):
					i.velocity_x*=-self.value
				else:
					i.velocity_x*=-1
				
				
		for i in list:
			if i.center_y<0 and self.target1_1_1_1.life!=0 :
				i.center_y=self.height+100
		for i in list:
			if (i.center_y<self.height*3/4) and i in (self.target1,self.target2,self.target3,self.target4):
				self.random2()
			
			
		
	
		if self.aim1.center_y>self.height:
			self.aim1.center_y=self.ship.center_y+self.ship.height*1/4
			self.aim1.center_x=self.ship.center_x
			self.aim1.velocity=Vector(0,0)
		if self.aim2.center_y>self.height:
			self.aim2.center_y=self.ship.center_y+self.ship.height*1/4
			self.aim2.center_x=self.ship.center_x
			self.aim2.velocity=Vector(0,0)
		if self.aim3.center_y>self.height:
			self.aim3.center_y=self.ship.center_y+self.ship.height*1/4
			self.aim3.center_x=self.ship.center_x
			self.aim3.velocity=Vector(0,0)
		
		
	value=1.05
	speed=100.0
	def hard(self):
		self.speed=200.0
		self.value=1.5
	def easy(self):
		self.speed=50.0
		self.value=1.05
	def medium(self):
		self.speed=180.0
		self.value=1.20
	def on_touch_move(self,touch):
		if self.ship.life<=0 or self.target1_1_1_1.life==0:
			pass
		else:
			if touch.y<(self.ship.center_y+self.ship.height/2):
				self.ship.center_x=touch.x
				if self.aim1.center_y<(self.ship.center_y+self.ship.height/2) :
					self.aim1.center_x=touch.x
				if self.aim2.center_y<(self.ship.center_y+self.ship.height/2) :
					self.aim2.center_x=touch.x
				if self.aim3.center_y<(self.ship.center_y+self.ship.height/2) :
					self.aim3.center_x=touch.x
	def resuming(self):
		self.end_time=time.time()
		timee=self.end_time-self.start_time
		Clock.unschedule(self.random3)
		Clock.unschedule(self.random4)
		Clock.unschedule(self.boss)
		Clock.schedule_interval(self.update,1.0/100)
		Clock.schedule_interval(self.random3,8.0/1.0+timee)
		Clock.schedule_interval(self.random4,20.0/1.0+timee)
		Clock.schedule_once(self.boss,self.speed/1.0+timee)
		self.resume.opacity=0
		self.resume.disabled=True
		self.restart.disabled=True
		self.restart.opacity=0
		self.exit_button.disabled=True
		self.exit_button.opacity=0
	def restarting(self):
		Clock.unschedule(self.update)
		Clock.unschedule(self.random3)
		Clock.unschedule(self.random4)
		Clock.unschedule(self.boss)
		self.exit_button.disabled=True
		self.exit_button.opacity=0
		self.sound.stop()
		self.resume.disabled=True
		self.resume.opacity=0
		self.restart.opacity=0
		self.restart.disabled=True
		self.ship.score=0
		self.firing_button.opacity=1
		self.firing_button.disabled=False
		self.ship.life=10
		
		self.target1_1_1_1.life=10
		list=[self.target1,self.target2,self.target3,self.target4,self.target5,self.target6,self.target7,self.target8,self.target1_1,self.target2_2,self.target3_3,self.target4_4,self.target5_5,self.target6_6,self.target7_7,self.target8_8,self.target1_1_1]
		for i in list:
			i.center_x=self.width/2
			i.center_y=self.height+100
			i.velocity=Vector(0,0)
		self.random()
		self.saving.disabled=True
		self.saving.opacity=0
		tem=1
		self.target1_1_1_1.center_y=self.height+500
		self.invasion.disabled=True
		self.invasion.opacity=0
		self.losing.disabled=True
		self.losing.opacity=0
		Clock.schedule_interval(self.update,1.0/100.0)
		Clock.schedule_interval(self.random3,8.0/1.0)
		Clock.schedule_interval(self.random4,20.0/1.0)
		Clock.schedule_once(self.boss,self.speed/1.0)
	def pause(self):
		self.start_time=time.time()
		self.exit_button.disabled=False
		self.exit_button.opacity=1
		Clock.unschedule(self.update)
		self.resume.disabled=False
		self.resume.opacity=1
		self.restart.opacity=1
		self.restart.disabled=False
	def change(self,dt):
		list=[self.back1,self.back2]
		i=choice(list)
		i.disabled=False
		i.opacity=1
		b=list.index(i)
		b=1-b
		list[b].disabled=True
		list[b].opacity=0
		
		
	def play(self):
		self.initialize.disabled=True
		self.initialize.opacity=0
		self.pause_button.disabled=False
		self.pause_button.opacity=1
		self.firing_button.opacity=1
		self.firing_button.disabled=False
		self.start_button.disabled=True
		self.start_button.opacity=0
		self.easy_button.disabled=True
		self.easy_button.opacity=0
		self.hard_button.disabled=True
		self.hard_button.opacity=0
		self.medium_button.disabled=True
		self.medium_button.opacity=0
		
		self.random()
		Clock.schedule_interval(self.update,1.0/100.0)
		Clock.schedule_interval(self.random3,8.0/1.0)
		Clock.schedule_interval(self.random4,20.0/1.0)
		Clock.schedule_once(self.boss,self.speed/1.0)
		Clock.schedule_interval(self.change,1.0/2)

g=galaxianGame()
	
class galaxianApp(App):
	def build(self):
		g=galaxianGame()	
		return g
galaxianApp().run()