import streamlit as st
import pandas as pd
st.set_page_config(page_title="Les dépenses communes !")


st.title('Répartition compte')

##Input

d = {'jour': [4,4,5,5,6,8,15,29,5,17,10,30,30], 'Nom': ['Tel port F', 'Charges copro', 'Elec', 'Entretien chaudière',
'Internet+TV', 'Assurance habitation', 'TF', 'Ecole+Perisco', 'Alloc familiale', 'Mutuelle F', 'Creche', 'CB F', 'CB R'],
 'Montant': [-9.99,-320.22,-1.00,-8.87,-1.98,-25.46,-144.00,-146.00,139.00,-60.85,-450.00, 0, 0]}
df = pd.DataFrame(data=d).sort_values('jour')

edited_df = st.data_editor(df, hide_index=True, height=490)

solde_compte = st.number_input('Solde du compte:')


depense_commune = solde_compte + edited_df['Montant'].sum()


st.text(f'Dépense commune : {round(depense_commune,2)}')

commun_paye_par_F_perso = st.number_input('Commun payé par F perso:')

commun_paye_par_R_perso = st.number_input('Commun payé par R perso:')

commun_pour_F_perso = st.number_input('Commun pour F perso:')

commun_pour_R_perso = st.number_input('Commun pour R perso:')

salaire_R = st.number_input('Salaire R',value = 1)

salaire_F = st.number_input('Salaire F', value = 1)

## Calcul

depense_commune_total = depense_commune - commun_pour_F_perso - commun_pour_R_perso


salaire_r_net = salaire_R+ commun_pour_R_perso
salaire_f_net = salaire_F + commun_pour_F_perso
ratio = salaire_f_net / (salaire_r_net + salaire_f_net)

commun_a_payer_f = depense_commune_total * ratio

commun_a_payer_r = depense_commune_total * (1 - ratio)

part_perso_r_pour_commun_f = commun_paye_par_R_perso * ratio
part_perso_r_pour_commun_r = -part_perso_r_pour_commun_f

part_perso_f_pour_commun_r = commun_paye_par_F_perso*(1-ratio)
part_perso_f_pour_commun_f = - part_perso_f_pour_commun_r

commun_a_payer_f_final = commun_a_payer_f + commun_pour_F_perso + part_perso_r_pour_commun_r + part_perso_f_pour_commun_r
commun_a_payer_r_final = commun_a_payer_r + commun_pour_R_perso + part_perso_r_pour_commun_f + part_perso_f_pour_commun_f

## Output


if st.button('calcul'):

  st.text(f'Ratio salaire : {round(ratio,2)}')

  st.text(f'Dépenses communes net {round(depense_commune_total,2)}')
  st.text(f'Commun à payer F {round(commun_a_payer_f,2)}')
  st.text(f'Commun à payer R {round(commun_a_payer_r,2)}')
  st.text(f'part perso R pour commun R {round(part_perso_r_pour_commun_r,2)}')
  st.text(f'part perso R pour commun F {round(part_perso_r_pour_commun_f,2)}')
  st.text(f'part perso F pour commun R {round(part_perso_f_pour_commun_r,2)}')
  st.text(f'part perso F pour commun F {round(part_perso_f_pour_commun_f,2)}')

  st.text(f'Commun à payer F final : {round(commun_a_payer_f_final,2)}')
  st.text(f'Commun à payer R final : {round(commun_a_payer_r_final,2)}')
