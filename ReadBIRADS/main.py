import pandas as pd
from pathlib import Path
import birads

'''
    Calc case description test set
'''
df_cal_test = pd.read_csv(r"C:\Users\ma-nu\Downloads\calc_case_description_test_set.csv")
df_cal_train = pd.read_csv(r'C:\Users\ma-nu\Downloads\calc_case_description_train_set.csv')
df_mass_test = pd.read_csv(r"C:\Users\ma-nu\Downloads\mass_case_description_test_set.csv")
df_mass_train = pd.read_csv(r'C:\Users\ma-nu\Downloads\mass_case_description_train_set.csv')
#df.info()

# Listas birads malignidad y benignidad-- LEFT AND RIGHT
birads_3_M = []
birads_3_M_L = []
birads_3_M_R = []
birads_3_B = []
birads_3_B_L = []
birads_3_B_R = []
birads_4_M = []
birads_4_M_L =[]
birads_4_M_R = []
birads_4_B = []
birads_4_B_L = []
birads_4_B_R = []

print('Cal-test:\n')
total_birads_3 = df_cal_test['assessment'].value_counts()[3] \
                + df_cal_train['assessment'].value_counts()[3] \
                + df_mass_test['assessment'].value_counts()[3] \
                + df_mass_train['assessment'].value_counts()[3]
total_birads_4 = df_cal_test['assessment'].value_counts()[4] \
                + df_cal_train['assessment'].value_counts()[4] \
                + df_mass_test['assessment'].value_counts()[4] \
                + df_mass_train['assessment'].value_counts()[4]

print(f'Total BIRADS 3: {total_birads_3}')
print(f'Total BIRADS 4: {total_birads_4}')

print('\n--------------------------Resumen cal-test --------------------------\n')
cal_test_3M = birads.consultBirads(df=df_cal_test)
birads_3_M.append(cal_test_3M)
print(f'BIRADS 3 pathology maligna cal-test: {cal_test_3M}')
cal_test_3ML = birads.consultSideBreast(df=df_cal_test)
birads_3_M_L.append(cal_test_3ML)
print(f'BIRADS 3 pathology maligna left cal-test: {cal_test_3ML}')
cal_test_3MR =  birads.consultSideBreast(df=df_cal_test, side='RIGHT')
birads_3_M_R.append(cal_test_3MR)
print(f'BIRADS 3 pathology maligna right cal-test: {cal_test_3MR}\n')

cal_test_3B = birads.consultBirads(df=df_cal_test, pathology='BENIGN')
birads_3_B.append(cal_test_3B)
print(f'BIRADS 3 pathology benigna cal-test: {cal_test_3B}')
cal_test_3BL = birads.consultSideBreast(df=df_cal_test, pathology='BENIGN')
birads_3_B_L.append(cal_test_3BL)
print(f'BIRADS 3 pathology benigna left cal-test: {cal_test_3BL}')
cal_test_3BR = birads.consultSideBreast(df=df_cal_test, side='RIGHT', pathology='BENIGN')
birads_3_B_R.append(cal_test_3BR)
print(f'BIRADS 3 pathology benigna right cal-test: {cal_test_3BR}\n')

cal_test_4M = birads.consultBirads(df=df_cal_test,birads=4)
birads_4_M.append(cal_test_4M)
print(f'BIRADS 4 pathology maligna cal-test: {cal_test_4M}')
cal_test_4ML = birads.consultSideBreast(df=df_cal_test, birads=4)
birads_4_M_L.append(cal_test_4ML)
print(f'BIRADS 4 pathology maligna left cal-test: {cal_test_4ML}')
cal_test_4MR = birads.consultSideBreast(df=df_cal_test, birads=4, side='RIGHT')
birads_4_M_R.append(cal_test_4MR)
print(f'BIRADS 4 pathology maligna right cal-test: {cal_test_4MR}\n')

cal_test_4B = birads.consultBirads(df=df_cal_test, birads=4, pathology='BENIGN')
birads_4_B.append(cal_test_4B)
print(f'BIRADS 4 pathology benigna cal-test: {cal_test_4B}')
cal_test_4BL = birads.consultSideBreast(df=df_cal_test, birads=4, pathology='BENIGN')
birads_4_B_L.append(cal_test_4BL)
print(f'BIRADS 4 pathology benigna left cal-test: {cal_test_4BL}')
cal_test_4BR = birads.consultSideBreast(df=df_cal_test, birads=4, side='RIGHT', pathology='BENIGN')
birads_4_B_R.append(cal_test_4BR)
print(f'BIRADS 4 pathology benigna right cal-test: {cal_test_4BR}\n')

print('\n--------------------------Resumen cal-train --------------------------\n')
cal_train_3M = birads.consultBirads(df=df_cal_train)
birads_3_M.append(cal_train_3M)
print(f'BIRADS 3 pathology maligna cal-train: {cal_train_3M}')
cal_train_3ML = birads.consultSideBreast(df=df_cal_train)
birads_3_M_L.append(cal_train_3ML)
print(f'BIRADS 3 pathology maligna left cal-train: {cal_train_3ML}')
cal_train_3MR =  birads.consultSideBreast(df=df_cal_train, side='RIGHT')
birads_3_M_R.append(cal_train_3MR)
print(f'BIRADS 3 pathology maligna right cal-train: {cal_train_3MR}\n')

cal_train_3B = birads.consultBirads(df=df_cal_train, pathology='BENIGN')
birads_3_B.append(cal_train_3B)
print(f'BIRADS 3 pathology benigna cal-train: {cal_train_3B}')
cal_train_3BL = birads.consultSideBreast(df=df_cal_train, pathology='BENIGN')
birads_3_B_L.append(cal_train_3BL)
print(f'BIRADS 3 pathology benigna left cal-train: {cal_train_3BL}')
cal_train_3BR = birads.consultSideBreast(df=df_cal_train, side='RIGHT', pathology='BENIGN')
birads_3_B_R.append(cal_train_3BR)
print(f'BIRADS 3 pathology benigna right cal-train: {cal_train_3BR}\n')

cal_train_4M = birads.consultBirads(df=df_cal_train,birads=4)
birads_4_M.append(cal_train_4M)
print(f'BIRADS 4 pathology maligna cal-train: {cal_train_4M}')
cal_train_4ML = birads.consultSideBreast(df=df_cal_train, birads=4)
birads_4_M_L.append(cal_train_4ML)
print(f'BIRADS 4 pathology maligna left cal-train: {cal_train_4ML}')
cal_train_4MR = birads.consultSideBreast(df=df_cal_train, birads=4, side='RIGHT')
birads_4_M_R.append(cal_train_4MR)
print(f'BIRADS 4 pathology maligna right cal-train: {cal_train_4MR}\n')

cal_train_4B = birads.consultBirads(df=df_cal_train, birads=4, pathology='BENIGN')
birads_4_B.append(cal_train_4B)
print(f'BIRADS 4 pathology benigna cal-train: {cal_train_4B}')
cal_train_4BL = birads.consultSideBreast(df=df_cal_train, birads=4, pathology='BENIGN')
birads_4_B_L.append(cal_train_4BL)
print(f'BIRADS 4 pathology benigna left cal-train: {cal_train_4BL}')
cal_train_4BR = birads.consultSideBreast(df=df_cal_train, birads=4, side='RIGHT', pathology='BENIGN')
birads_4_B_R.append(cal_train_4BR)
print(f'BIRADS 4 pathology benigna right cal-train: {cal_train_4BR}\n')


print('\n--------------------------Resumen Mass-test --------------------------\n')
mass_test_3M = birads.consultBirads(df=df_mass_test)
birads_3_M.append(mass_test_3M)
print(f'BIRADS 3 pathology maligna mass-test: {mass_test_3M}')
mass_test_3ML = birads.consultSideBreast(df=df_mass_test)
birads_3_M_L.append(mass_test_3ML)
print(f'BIRADS 3 pathology maligna left mass-test: {mass_test_3ML}')
mass_test_3MR =  birads.consultSideBreast(df=df_mass_test, side='RIGHT')
birads_3_M_R.append(mass_test_3MR)
print(f'BIRADS 3 pathology maligna right mass-test: {mass_test_3MR}\n')

mass_test_3B = birads.consultBirads(df=df_mass_test, pathology='BENIGN')
birads_3_B.append(mass_test_3B)
print(f'BIRADS 3 pathology benigna mass-test: {mass_test_3B}')
mass_test_3BL = birads.consultSideBreast(df=df_mass_test, pathology='BENIGN')
birads_3_B_L.append(mass_test_3BL)
print(f'BIRADS 3 pathology benigna left mass-test: {mass_test_3BL}')
mass_test_3BR = birads.consultSideBreast(df=df_mass_test, side='RIGHT', pathology='BENIGN')
birads_3_B_R.append(mass_test_3BR)
print(f'BIRADS 3 pathology benigna right mass-test: {mass_test_3BR}\n')

mass_test_4M = birads.consultBirads(df=df_mass_test,birads=4)
birads_4_M.append(mass_test_4M)
print(f'BIRADS 4 pathology maligna mass-test: {mass_test_4M}')
mass_test_4ML = birads.consultSideBreast(df=df_mass_test, birads=4)
birads_4_M_L.append(mass_test_4ML)
print(f'BIRADS 4 pathology maligna left mass-test: {mass_test_4ML}')
mass_test_4MR = birads.consultSideBreast(df=df_mass_test, birads=4, side='RIGHT')
birads_4_M_R.append(mass_test_4MR)
print(f'BIRADS 4 pathology maligna right mass-test: {mass_test_4MR}\n')

mass_test_4B = birads.consultBirads(df=df_mass_test, birads=4, pathology='BENIGN')
birads_4_B.append(mass_test_4B)
print(f'BIRADS 4 pathology benigna mass-test: {mass_test_4B}')
mass_test_4BL = birads.consultSideBreast(df=df_mass_test, birads=4, pathology='BENIGN')
birads_4_B_L.append(mass_test_4BL)
print(f'BIRADS 4 pathology benigna left mass-test: {mass_test_4BL}')
mass_test_4BR = birads.consultSideBreast(df=df_mass_test, birads=4, side='RIGHT', pathology='BENIGN')
birads_4_B_R.append(mass_test_4BR)
print(f'BIRADS 4 pathology benigna right mass-test: {mass_test_4BR}\n')

print('\n--------------------------Resumen Mass-train --------------------------\n')
mass_train_3M = birads.consultBirads(df=df_mass_train)
birads_3_M.append(mass_train_3M)
print(f'BIRADS 3 pathology maligna mass-train: {mass_train_3M}')
mass_train_3ML = birads.consultSideBreast(df=df_mass_train)
birads_3_M_L.append(mass_train_3ML)
print(f'BIRADS 3 pathology maligna left mass-train: {mass_train_3ML}')
mass_train_3MR =  birads.consultSideBreast(df=df_mass_train, side='RIGHT')
birads_3_M_R.append(mass_train_3MR)
print(f'BIRADS 3 pathology maligna right mass-train: {mass_train_3MR}\n')

mass_train_3B = birads.consultBirads(df=df_mass_train, pathology='BENIGN')
birads_3_B.append(mass_train_3B)
print(f'BIRADS 3 pathology benigna mass-train: {mass_train_3B}')
mass_train_3BL = birads.consultSideBreast(df=df_mass_train, pathology='BENIGN')
birads_3_B_L.append(mass_train_3BL)
print(f'BIRADS 3 pathology benigna left mass-train: {mass_train_3BL}')
mass_train_3BR = birads.consultSideBreast(df=df_mass_train, side='RIGHT', pathology='BENIGN')
birads_3_B_R.append(mass_train_3BR)
print(f'BIRADS 3 pathology benigna right mass-train: {mass_train_3BR}\n')

mass_train_4M = birads.consultBirads(df=df_mass_train,birads=4)
birads_4_M.append(mass_train_4M)
print(f'BIRADS 4 pathology maligna mass-train: {mass_train_4M}')
mass_train_4ML = birads.consultSideBreast(df=df_mass_train, birads=4)
birads_4_M_L.append(mass_train_4ML)
print(f'BIRADS 4 pathology maligna left mass-train: {mass_train_4ML}')
mass_train_4MR = birads.consultSideBreast(df=df_mass_train, birads=4, side='RIGHT')
birads_4_M_R.append(mass_train_4MR)
print(f'BIRADS 4 pathology maligna right mass-train: {mass_train_4MR}\n')

mass_train_4B = birads.consultBirads(df=df_mass_train, birads=4, pathology='BENIGN')
birads_4_B.append(mass_train_4B)
print(f'BIRADS 4 pathology benigna mass-train: {mass_train_4B}')
mass_train_4BL = birads.consultSideBreast(df=df_mass_train, birads=4, pathology='BENIGN')
birads_4_B_L.append(mass_train_4BL)
print(f'BIRADS 4 pathology benigna left mass-train: {mass_train_4BL}')
mass_train_4BR = birads.consultSideBreast(df=df_mass_train, birads=4, side='RIGHT', pathology='BENIGN')
birads_4_B_R.append(mass_train_4BR)
print(f'BIRADS 4 pathology benigna right mass-train: {mass_train_4BR}\n')

# Calcular la malignidad en todos los datos de birads 3
malignidad_birads_3 = sum(birads_3_M)
print(birads_3_M)
malignidad_birads_3_L = sum(birads_3_M_L)
malignidad_birads_3_R = sum(birads_3_M_R)

# Calcular la benignidad en todos los datos de birads 3
benignidad_birads_3 = sum(birads_3_B)
print(birads_3_B)
benignidad_birads_3_L = sum(birads_3_B_L)
benignidad_birads_3_R = sum(birads_3_B_R)

# Calcular la malignidad en todos los datos de birads 4
malignidad_birads_4 = sum(birads_4_M)
malignidad_birads_4_L = sum(birads_4_M_L)
malignidad_birads_4_R = sum(birads_4_M_R)
# Calcular la benignidad en todos los datos de birads 4
benignidad_birads_4 = sum(birads_4_B)
benignidad_birads_4_L = sum(birads_4_B_L)
benignidad_birads_4_R = sum(birads_4_B_R)


# Verificar los IDs repetidos en cada uno de los csv:
combinations = [
    df_cal_test['patient_id'],
    df_cal_train['patient_id'],
    df_mass_test['patient_id'],
    df_mass_train['patient_id']
]
# Se calculan los elementos repetidos
total_rep = 0
for i in combinations:
    for j in combinations:
        if i.equals(j):
             continue
        total_rep += len(birads.Id_repetidos(df_column1=i, df_column2=j))
        print(f'Pacientes repetidos: {birads.Id_repetidos(df_column1=i, df_column2=j)}')


# Calculamos los pacientes totales en las bases de datos eliminando las repeticiones
pacientes_totales = len(set(df_cal_test['patient_id']))+ len(set(df_cal_train['patient_id'])) \
                    + len(set(df_mass_test['patient_id']))+ len(set(df_mass_train['patient_id'])) \
                    - total_rep

print(f'Pacientes totales: {pacientes_totales}')



# Pacientes totales de birads 3 y 4
print('\n--------------Cal-Test-Train--------------\n')
print(f'Pacientes birads 3 cal-test: {birads.patients_birads(df=df_cal_test, birads=3)}')
print(f'Pacientes birads 4 cal-test: {birads.patients_birads(df=df_cal_test, birads=4)}')
print(f'Pacientes birads 3 cal-train: {birads.patients_birads(df=df_cal_train, birads=3)}')
print(f'Pacientes birads 4 cal-train: {birads.patients_birads(df=df_cal_train, birads=4)}')

print('\n--------------Mass-Test-Train--------------\n')
print(f'Pacientes birads 3 mass-test: {birads.patients_birads(df=df_mass_test, birads=3)}')
print(f'Pacientes birads 4 mass-test: {birads.patients_birads(df=df_mass_test, birads=4)}')
print(f'Pacientes birads 3 mass-train: {birads.patients_birads(df=df_mass_train, birads=3)}')
print(f'Pacientes birads 4 mass-train: {birads.patients_birads(df=df_mass_train, birads=4)}')

print('-----------------Resultados pacientes totales birads 3 y 4--------------')
# Pacientes totales de birads 3
total_birads_3_patients = birads.patients_birads(df=df_cal_test, birads=3) \
                + birads.patients_birads(df=df_cal_train, birads=3) \
                + birads.patients_birads(df=df_mass_test, birads=3) \
                + birads.patients_birads(df=df_mass_train, birads=3)

print(f'Total de pacientes birads 3: {total_birads_3_patients}')

# Pacientes totales de birads 4
total_birads_4_patients = birads.patients_birads(df=df_cal_test, birads=4) \
                + birads.patients_birads(df=df_cal_train, birads=4) \
                + birads.patients_birads(df=df_mass_test, birads=4) \
                + birads.patients_birads(df=df_mass_train, birads=4)

print(f'Total de pacientes birads 4: {total_birads_4_patients}')

# Valores BENIGN WITHOUT CALLBACK
print('\n---------------BENIGN_WITHOUT_CALLBACK-----------------\n')
benign_without_cal_T_3 = birads.consultBirads(df = df_cal_test, pathology='BENIGN_WITHOUT_CALLBACK')
benign_without_cal_TR_3 = birads.consultBirads(df = df_cal_train, pathology='BENIGN_WITHOUT_CALLBACK')
benign_without_mass_T_3 = birads.consultBirads(df = df_mass_test, pathology='BENIGN_WITHOUT_CALLBACK')
benign_without_mass_TR_3 = birads.consultBirads(df = df_mass_train, pathology='BENIGN_WITHOUT_CALLBACK')
Total_benign_without_3 = benign_without_cal_T_3 + benign_without_cal_TR_3 \
                        + benign_without_mass_T_3 + benign_without_mass_TR_3

benign_without_cal_T_4 = birads.consultBirads(df = df_cal_test, birads=4, pathology='BENIGN_WITHOUT_CALLBACK')
benign_without_cal_TR_4 = birads.consultBirads(df = df_cal_train, birads=4, pathology='BENIGN_WITHOUT_CALLBACK')
benign_without_mass_T_4 = birads.consultBirads(df = df_mass_test, birads=4, pathology='BENIGN_WITHOUT_CALLBACK')
benign_without_mass_TR_4 = birads.consultBirads(df = df_mass_train, birads=4, pathology='BENIGN_WITHOUT_CALLBACK')
Total_benign_without_4 = benign_without_cal_T_4 + benign_without_cal_TR_4 \
                        + benign_without_mass_T_4 + benign_without_mass_TR_4

# Resumen final
df_final = pd.DataFrame({'Pacientes_totales': [pacientes_totales],
                         'Pacientes_birads_3': [total_birads_3_patients],
                         'Pacientes_birads_4': [total_birads_4_patients],
                         'Imagenes_birads_3': [total_birads_3],
                         'Imagenes_birads_4': [total_birads_4],
                         'Imagenes_birads_3_malignas': [malignidad_birads_3],
                         'Imagenes_birads_3_benignas': [benignidad_birads_3],
                         'Imagenes_birads_3_benigns_without':[Total_benign_without_3],
                         'Imagenes_birads_4_malignas': [malignidad_birads_4],
                         'Imagenes_birads_4_benignas': [benignidad_birads_4],
                         'Imagenes_birads_4_benigns_without': [Total_benign_without_4],
                         'Imagenes_birads_3_malignas_left':[malignidad_birads_3_L],
                         'Imagenes_birads_3_malignas_right':[malignidad_birads_3_R],
                         'Imagenes_birads_3_benignas_left':[benignidad_birads_3_L],
                         'Imagenes_birads_3_benignas_right':[benignidad_birads_3_R],
                         'Imagenes_birads_4_malignas_left':[malignidad_birads_4_L],
                         'Imagenes_birads_4_malignas_right':[malignidad_birads_4_R],
                         'Imagenes_birads_4_benignas_left':[benignidad_birads_4_L],
                         'Imagenes_birads_4_benignas_right':[benignidad_birads_4_R],
                        })

# Generar el informe final en un archivo csv
df_final.to_csv('resulmen_final.csv', index=False)