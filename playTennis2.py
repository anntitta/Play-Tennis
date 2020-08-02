import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

outlook=ctrl.Antecedent(np.arange(0,15,1),'outlook')
temp=ctrl.Antecedent(np.arange(0,15,1),'temp')
play=ctrl.Antecedent(np.arange(0,15,1),'play')
wind=ctrl.Antecedent(np.arange(0,15,1),'wind')
humd=ctrl.Antecedent(np.arange(0,15,1),'humd')

outlook['sunny']=fuzz.trimf(outlook.universe,[0,0,4])
outlook['overcast']=fuzz.trimf(outlook.universe,[0,4,9])
outlook['rain']=fuzz.trimf(outlook.universe,[4,9,14])

temp['hot']=fuzz.trimf(temp.universe,[0,0,4])
temp['mild']=fuzz.trimf(temp.universe,[0,4,10])
temp['cool']=fuzz.trimf(temp.universe,[4,10,14])

play['yes']=fuzz.trimf(play.universe,[0,0,9])
play['no']=fuzz.trimf(play.universe,[0,9,14])

wind['strong']=fuzz.trimf(wind.universe,[0,0,6])
wind['weak']=fuzz.trimf(wind.universe,[0,6,14])

humd['high']=fuzz.trimf(humd.universe,[0,0,7])
humd['normal']=fuzz.trimf(humd.universe,[0,7,14])

outlook.view()
temp.view()
play.view()
wind.view()
humd.view()


rule1=ctrl.Rule(outlook['sunny'], temp['mild'], humd['normal'], wind['weak'], play['No'])
rule2=ctrl.Rule(outlook['overcast']& play['yes'])
rule3=ctrl.Rule(outlook['rain']& wind['weak'],play['yes'])
rule4=ctrl.Rule(outlook['rain']& humd['high'],play['yes'])
rule5=ctrl.Rule(outlook['overcast']& temp['cool'],humd['high'],wind['weak'],play['yes'])
rule6=ctrl.Rule(outlook['sunny']& humd['high'],play['no'])
rule7=ctrl.Rule(outlook['sunny']& temp['cool'],play['yes'])
rule8=ctrl.Rule(outlook['sunny']& temp['hot'],humd['normal'],wind['weak'],play['no'])
rule9=ctrl.Rule(outlook['rain']& wind['strong'],play['no'])
rule10=ctrl.Rule(humd['normal']& wind['weak'],play['yes'])
rule11=ctrl.Rule(outlook['sunny']& temp['hot']& wind['weak'],play['no'])
rule12=ctrl.Rule(outlook['sunny']& temp['mild']& wind['weak'],play['no'])
rule13=ctrl.Rule(outlook['rain']& temp['mild']& humd['high'],play['yes'])
rule14=ctrl.Rule(outlook['overcast']& temp['hot'],play['yes'])

print("........")

timing_ctrl=ctrl.ControlSystem([rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9,rule10,rule11,rule12,rule13,rule14])

timing=ctrl.ControlSystemSimulation(timing_ctrl)

timing.input['outlook']=9.8
timing.input['wind']=6.5
timing.input['humd']=7.8
timing.input['temp']=10.9

timing.compute()

print("crisp value",timing.output['play'])
timing.view(sim=timing)
