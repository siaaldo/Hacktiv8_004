import pandas as pd
import sqlite3

df1 = pd.read_csv('assessments.csv')
df2 = pd.read_csv('courses.csv')
df3 = pd.read_csv('studentInfo.csv')
df4 = pd.read_csv('studentRegistration.csv')
df5 = pd.read_csv('vle.csv')
df6 = pd.read_csv('studentAssessment.csv')

conn = sqlite3.connect('ungradedtest.db', timeout=30)

curr = conn.cursor()

def dropTable(table):
    curr.execute(f'''
        DROP TABLE {table}
    ''')
    conn.commit()

df1['id_assessment'] = df1['id_assessment'].astype(float)

dropTable('assessment')

curr.execute('''
    CREATE TABLE assessment(
        code_module varchar(50),
        code_presentation varchar(50),
        id_assessment INT PRIMARY KEY,
        assessment_type varchar(50),
        date date,
        weight FLOAT
    );'''
)

for i in range(len(df1)):
    curr.execute('''
    INSERT INTO assessment (code_module, code_presentation, id_assessment, assessment_type, date, weight)
    VALUES (?,?,?,?,?,?)''', (df1['code_module'][i],
    df1['code_presentation'][i],
    df1['id_assessment'][i],
    df1['assessment_type'][i],
    df1['date'][i],
    df1['weight'][i]))
    conn.commit()

df2['module_presentation_length'] = df2['module_presentation_length'].astype(float)

dropTable('courses')

curr.execute('''
    CREATE TABLE courses(
        code_module varchar(50),
        code_presentation varchar(50),
        module_presentation_lenght INT
    );'''
)

for i in range(len(df2)):
    curr.execute('''
    INSERT INTO courses (code_module, code_presentation, module_presentation_lenght)
    VALUES (?,?,?)''', 
    (df2['code_module'][i],
    df2['code_presentation'][i],
    df2['module_presentation_length'][i]))
    conn.commit()

df3['id_student'] = df3['id_student'].astype(float)
df3['num_of_prev_attempts'] = df3['num_of_prev_attempts'].astype(float)
df3['studied_credits'] = df3['studied_credits'].astype(float)

dropTable('studentInfo')

curr.execute('''
    CREATE TABLE studentInfo(
        code_module varchar(50),
        code_presentation varchar(50),
        id_student INT,
        gender varchar(50),
        region varchar(50),
        highest_education varchar(50),
        imd_band varchar(50),
        age_band varchar(50),
        num_of_prev_attempts INT,
        studied_credits INT,
        disability varchat(50),
        final_result varchar(50)
    )
''')


for i in range(len(df3)):
    curr.execute('''
        INSERT INTO studentInfo (code_module, 
        code_presentation, 
        id_student, 
        gender, 
        region, 
        highest_education, 
        imd_band, 
        age_band, 
        num_of_prev_attempts, 
        studied_credits, 
        disability, 
        final_result)
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?)''',(
            df3['code_module'][i],
            df3['code_presentation'][i],
            df3['id_student'][i],
            df3['gender'][i],
            df3['region'][i],
            df3['highest_education'][i],
            df3['imd_band'][i],
            df3['age_band'][i],
            df3['num_of_prev_attempts'][i],
            df3['studied_credits'][i],
            df3['disability'][i],
            df3['final_result'][i]
        ))
    conn.commit()

df4['id_student'] = df4['id_student'].astype(float)

dropTable('student_registration')

curr.execute('''
    CREATE TABLE student_registration(
        code_module varchar(50),
        code_presentation varchar(50),
        id_student INT,
        date_registration FLOAT,
        date_unregistration FLOAT
    );
''')

for i in range(len(df4)):
    curr.execute('''
        INSERT INTO student_registration (code_module, code_presentation, id_student, date_registration, date_unregistration)
        VALUES (?,?,?,?,?)''', (
            df4['code_module'][i],
            df4['code_presentation'][i],
            df4['id_student'][i],
            df4['date_registration'][i],
            df4['date_unregistration'][i]
        )
    )
    conn.commit()

df5['id_site'] = df5['id_site'].astype(float)
dropTable('vle')

curr.execute('''
    CREATE TABLE vle(
        id_site INT,
        code_module varchar(50),
        code_presentation varchar(50),
        activity_type varchar(50),
        week_from INT,
        week_to INT
    )
''')

for i in range(len(df5)):
    curr.execute('''
        INSERT INTO vle (id_site, code_module, code_presentation, activity_type, week_from, week_to)
        VALUES (?,?,?,?,?,?)''',
        (df5['id_site'][i],
        df5['code_module'][i],
        df5['code_presentation'][i],
        df5['activity_type'][i],
        df5['week_from'][i],
        df5['week_to'][i]
        ))
    conn.commit()

df6['id_assessment'] = df6['id_assessment'].astype(float)
df6['id_student'] = df6['id_student'].astype(float)
df6['date_submitted'] = df6['date_submitted'].astype(float)
df6['is_banked'] = df6['is_banked'].astype(float)

dropTable('studentAssessment')

curr.execute('''
    CREATE TABLE studentAssessment(
        id_assessment INT,
        id_student INT,
        date_submitted INT(50),
        is_banked INT(50),
        score INT
    )
''')

for i in range(len(df6)):   
    curr.execute('''
        INSERT INTO studentAssessment(id_assessment,  id_student, date_submitted, is_banked,score)
        VALUES (?,?,?,?,?)''',(
            df6['id_assessment'][i],
            df6['id_student'][i],
            df6['date_submitted'][i],
            df6['is_banked'][i],
            df6['score'][i]
        )
    )
    conn.commit()

final_query = curr.execute('''
    SELECT studentInfo.id_student, studentInfo.region, studentInfo.code_module,  a.assessment_type , studentAssessment.score
    FROM studentInfo
    JOIN studentAssessment
    ON studentInfo.Id_student = studentAssessment.id_student
    JOIN assessment a 
    ON studentAssessment.id_assessment = a.id_assessment
    WHERE studentInfo.code_presentation = '2014B'
''')

df_final = pd.DataFrame(final_query, columns=[
    'id_student',
    'region',
    'code_module',
    'assessment_type',
    'score'])

print(df_final)
curr.close()