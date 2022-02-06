import streamlit as st
from random import randint
from time import sleep

st.header("Inbetween Singapore")
st.markdown("<p style='color:Green; font-size:12px;'>By Lance Ng</p>", unsafe_allow_html=True)

st.write('\n')

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

st.write(f"Assuming the use of a standard 52 card deck, and we are not counting cards...")

if max_card != min_card:
    inside_probability = round(((max_card - min_card - 1)*4)/50*100,1)
    outside_probability = round(((50-6)/50*100)-inside_probability,1)
    tiang_probability = round(6/50*100,1)

    st.write(f'### Win probability: {inside_probability}%')
    st.write(f'### Outside probability: {outside_probability}%')
    st.write(f'### Tiang probability: {tiang_probability}%')

else:
    st.write(f'### Win probability: 0.0%')
    st.write(f'### Outside probability: {round((12*4)/50*100,1)}%')
    st.write(f'### Tiang probability: {round(2/50*100,1)}%')

# st.write("\n")

# st.markdown("## Let\'s practice")


# test_dict = {
# 1:'A',
# 2:'2',
# 3:'3',
# 4:'4',
# 5:'5',
# 6:'6',
# 7:'7',
# 8:'8',
# 9:'9',
# 10:'10',
# 11:'J',
# 12:'Q',
# 13:'K'
# }

# left_post, next_card, right_post = st.columns(3)
# bet, skip = st.columns(2)
# left_post.markdown(f'### Left')
# right_post.markdown(f'### Right')
# next_card.markdown(f'### Next')



# left_test = randint(1,13)
# right_test = randint(1,13)

# min_test = min(left_test, right_test)
# max_test = max(left_test, right_test)

# # displaying left and right card
# sleep(1)
# left_post.write(f'## {test_dict[min_test]}')
# sleep(1)
# right_post.write(f'## {test_dict[max_test]}')

# # predicting the third card
# deck = [1,2,3,4,5,6,7,8,9,10,11,12,13,
#         1,2,3,4,5,6,7,8,9,10,11,12,13,
#         1,2,3,4,5,6,7,8,9,10,11,12,13,
#         1,2,3,4,5,6,7,8,9,10,11,12,13]

# deck.remove(min_test)
# deck.remove(max_test)

# third_int = randint(0,49)
# third_card = test_dict[deck[third_int]]

# def display_third_bet():
#     next_card.markdown(f'## {third_card}')
#     if deck[third_int] < max_test and deck[third_int] > min_test:
#         next_card.markdown("<p style='color:Green;'>WIN</p>", unsafe_allow_html=True)
#     elif deck[third_int] == max_test or deck[third_int] == min_test:
#         next_card.markdown("<p style='color:Green;'>TIANG</p>", unsafe_allow_html=True)
#     else:
#         next_card.markdown("<p style='color:Green;'>LOSE</p>", unsafe_allow_html=True)
    

#     sleep(1)

# def display_third_pass():
#     next_card.markdown(f'## {third_card}')
#     next_card.markdown("<p style='color=Green;'>---</p>", unsafe_allow_html=True)


# left_blank, left_button, right_button, right_blank = st.columns(4)

# bet_button = left_button.button('bet', key='bet', on_click=display_third_bet)
# pass_button = right_button.button('pass', key='pass', on_click=display_third_pass)
# sleep(1)

# st.session_state['value'] = 

# if bet_button:
#     if third_int < max_test and third_int > min_test:
#         next_card.markdown(f'## {third_card}')
#         st.write('win')
#     elif third_int == max_test or third_int == min_test:
#         next_card.markdown(f'## {third_card}')
#         st.write('tiang')
#     else:
#         next_card.markdown(f'## {third_card}')
#         st.write('lose')



# if bet_button:
#     next_card.markdown(f'## {third_card}')
#     if third_int < max_test and third_int > min_test:
#         win_count +=1
#     if third_int == max_test or third_int == min_test:
#         tiang_count +=1
#     games +=1 

# elif pass_button:
#     next_card.markdown(f'## {third_card}')   
#     games +=1

# if games > 0:
#     st.write(win_rate = win_count / games)
#     st.write(tiang_rate = tiang_count / games)

# elif skip_button:
#     next_card.markdown(f'## {third_card}')
# else:
    # pass

# next_card.markdown(f'## {test_dict[deck[randint(0,49)]]}')

# for i in range(5):
#     st.write(test_dict[min_test])
#     st.write(test_dict[max_test])
#     sleep(1)

