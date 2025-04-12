import pandas as pd
    
def consultBirads(df, birads=3, pathology='MALIGNANT'):
    '''Calculate len of birads and pathology'''
    result = df.loc[(df.assessment==birads) & (df.pathology == pathology)]
    return len(result)
    
def consultSideBreast(df, side='LEFT', birads=3, pathology='MALIGNANT'):
    result = df.loc[(df['left or right breast'] == side) & 
                    (df.assessment == birads) & 
                    (df.pathology == pathology)]
    return len(result)

def Id_repetidos(df_column1, df_column2):
    repetidos = []
    for patient_id in set(df_column1):
        if patient_id in set(df_column2):
            repetidos.append(patient_id)
    return repetidos

# Pacientes totales en BIRADS 3 Y 4
def patients_birads(df, birads):
    copia_birads = df[['patient_id', 'assessment', 'pathology']]
    result = copia_birads.loc[(copia_birads.assessment==birads)]
    return len(set(result['patient_id']))