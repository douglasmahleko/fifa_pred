# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 10:48:42 2021

@author: EliteBook
"""

import numpy as np
import pandas as pd
import streamlit as st
import pickle
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error, accuracy_score

loaded_model = pickle.load(open('C:/Users/EliteBook/Desktop/stack/AIAssignment/trained_model.sav', 'rb'))
Xtest = pd.read_pickle('C:/Users/EliteBook/Desktop/stack/AIAssignment/d.file')
predict_from_load = loaded_model.predict(Xtest)
Ytest = pd.read_pickle('C:/Users/EliteBook/Desktop/stack/AIAssignment/dy.file')
r2 = r2_score(Ytest, predict_from_load)
mean_ab = mean_absolute_error(Ytest, predict_from_load)
mean_sq= mean_squared_error(Ytest, predict_from_load)
r_mean = np.sqrt(mean_sq)

def player_prediction(arr):
    encode = LabelEncoder()
    for i in range (len(arr)):
        if type(arr[i]) == int:
            pass
        elif type(arr[i]) == float:
            pass
        arr[i] = encode.fit_transform(arr[i])
    to_array = np.asarray(arr)
    arr_reshape = to_array.reshape(1, -1)
    predic = loaded_model.predict(arr_reshape)
    print(predic)
    
def main():
    st.title("fifa player rating prediction")
    st.write("if a position not applicable you can leave blank")
    age = st.slider("age of players", 17, 50)
    player_positions = st.text_input("player_positions of players")
    preferred_foot = st.text_input("preferred_foot of players")
    international_reputation = st.text_input("international_reputation of players")
    weak_foot = st.text_input("weak_foot of players")
    skill_moves = st.text_input("skill_moves of players")
    work_rate = st.text_input("work_rate of players")
    player_tags = st.text_input("player_tags of players")
    team_position = st.text_input("team_position of players")
    nation_position = st.text_input("nation_position of players")
    pace = st.slider("pace of players", 0, 100)
    defending = st.slider("defending of players", 0, 100)
    gk_diving = st.slider("gk_diving of players", 0, 100)
    player_traits = st.slider("player_traits of players", 0, 100)
    attacking_crossing = st.text_input("attacking_crossing of players")
    attacking_finishing = st.text_input("attacking_finishing of players")
    attacking_heading_accuracy = st.text_input("attacking_heading_accuracy of players")
    attacking_short_passing = st.text_input("attacking_short_passing of players")
    attacking_volleys = st.text_input("attacking_volleys of players")
    skill_dribbling = st.text_input("skill_dribbling of players")
    skill_curve = st.text_input("skill_curve of players")
    skill_fk_accuracy = st.text_input("skill_fk_accuracy of players")
    skill_long_passing = st.text_input("skill_long_passing of players")
    skill_ball_control = st.text_input("skill_ball_control of players")
    movement_acceleration = st.text_input("movement_acceleration of players")
    movement_sprint_speed = st.text_input("movement_sprint_speed of players")
    movement_agility = st.text_input("movement_agility of players")
    movement_reactions = st.text_input("movement_reactions of players")
    movement_balance = st.text_input("movement_balance of players")
    power_shot_power = st.text_input("power_shot_power of players")
    power_jumping = st.text_input("power_jumping of players")
    power_stamina = st.text_input("power_stamina of players")
    power_strength = st.text_input("power_strength of players")
    power_long_shots = st.text_input("power_long_shots of players")
    mentality_aggression = st.text_input("mentality_aggression of players")
    mentality_interceptions = st.text_input("mentality_interceptions of players")
    mentality_positioning = st.text_input("mentality_positioning of players")
    mentality_vision = st.text_input("mentality_vision of players")
    mentality_penalties = st.text_input("mentality_penalties of players")
    defending_marking = st.text_input("defending_marking of players")
    defending_standing_tackle = st.text_input("defending_standing_tackle of players")
    defending_sliding_tackle = st.text_input("defending_sliding_tackle of players")
    ls = st.text_input("ls of players")
    lw = st.text_input("lw of players")
    lam = st.text_input("lam of players")
    lcb = st.text_input("lcb of players")

    results = ''
    var = [age, height_cm, weight_kg, club, player_positions, preferred_foot, international_reputation, weak_foot, skill_moves, work_rate, player_tags, team_position, nation_position, pace, defending, gk_diving, player_traits, attacking_crossing, attacking_finishing, attacking_heading_accuracy, attacking_short_passing, attacking_volleys, skill_dribbling, skill_curve, skill_fk_accuracy, skill_long_passing, skill_ball_control, movement_acceleration, movement_sprint_speed, movement_agility, movement_reactions, movement_balance, power_shot_power, power_jumping, power_stamina, power_strength, power_long_shots, mentality_aggression, mentality_interceptions, mentality_positioning, mentality_vision, mentality_penalties, defending_marking, defending_standing_tackle, defending_sliding_tackle, ls, lw, lam, lcb]
    for i in var:
        if i == "":
            i = 'nothing'
    if st.button("predictionResults"):
        results = player_prediction(var)
        
    st.success(results)
    st.write("the score is \t", r2, "\nthe mean absolute error is \t", mean_ab)
    st.write('the mean squared error is\t', mean_sq,'\nthe roo mean error \t', r_mean)
if __name__ == '__main__':
    main()
    