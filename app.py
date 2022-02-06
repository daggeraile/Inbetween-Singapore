import streamlit as st

st.header("Inbetween Probabillities")
st.write(f"""This is a calculator for Singapore style game **Inbetween**. Two cards are revealed to represent the 'goal post',
the objective is to bet that the next card to be in between the 'goal post'. If the next card happens to be outside the 'goal post',
the player loses the bet. If it hits the 'goal post', also affectionately known as 'tiang' in Singapore, the player pays double the bet.""")

st.write('\n')

st.write("### Please Select Card Range")
card_range = st.select_slider(label="", options=['A','2','3','4','5','6','7','8','9','10','J','Q','K'], value=('A', 'K'))

card_dict = {
'A':1,
'2':2,
'3':3,
'4':4,
'5':5,
'6':6,
'7':7,
'8':8,
'9':9,
'10':10,
'J':11,
'Q':12,
'K':13
}

max_card = card_dict[card_range[1]]
min_card = card_dict[card_range[0]]

if max_card != min_card:
    inside_probability = round(((max_card - min_card - 1)*4)/50*100,1)
    outside_probability = round(((50-6)/50*100)-inside_probability,1)
    tiang_probability = round(6/50*100,1)

    st.write(f'### Win probability: {inside_probability}%')
    st.write(f'### Outside probability: {outside_probability}%')
    st.write(f'### Tiang probability: {tiang_probability}%')

else:
    st.write(0)
    st.write(round((12*4)/50*100,1))
    st.write(round(2/50*100,1))