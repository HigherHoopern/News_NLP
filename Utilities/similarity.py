import en_core_web_lg
nlp = en_core_web_lg.load()

target_text = str('Armed, Arms, Weapon, Weapons Army, Brigades, Forces, Militaries, Military, Paratroopers, Police, \Soldier, Soldiers, Troop, Troops Casualty, Casualties, Dead, Deadliest, Deadly, Death, Deaths, Died, Dies, Fatalities,\ Kill, Killed, Killing, Killings, Lethal, Violence Authority, Authorities, Civil, Government, Governments, Regime, State\ Citizens, Civilian, Civilians, Country, People, Peoples, Population, Nation, Nationals, Residents Clashes, Coup, \Demonstrations, Demonstration, Protest, Protests, Rebellion, Revolution, Riot, Rioting, Riots, Uprising Activist, \Activists, Demonstrator, Protester, Provocateurs, Revolutionaries, Rioters Combatant, Combatants, Fighters, Insurgent,\ Insurgents, Guerillas, Militants, Partisan, Rebel, Rebels, Revolutionaries, Separatist, Separatists Attack, Attacks, \Battle, Combat, Conflict, Conflicts, Fighting, Hostilities, Insurgency, Invasion, War, Wars, Unrest , political risk')

def Pre_Processing(text):    
    
    tokens = word_tokenize(text)
    
    # convert to lower case
    tokens = [w.lower() for w in tokens]
    
    # prepare regex for char filtering
    re_punc = re.compile('[%s]' % re.escape(string.punctuation))
    
    # remove punctuation from each word
    stripped = [re_punc.sub('', w) for w in tokens]
    
    # remove remaining tokens that are not alphabetic
    words = [word for word in stripped if word.isalpha()]
    
    # filter out stop words
    stop_words = set(stopwords.words('english'))
    
    words = [w for w in words if not w in stop_words]
    
    return words


def Spacy_Similarity(dataset,col_name:str,target_text:str):
    
    sim = []
    text_1 = " ".join(Pre_Processing(target_text))
    text_1 = text_1
    text_1 = nlp(text_1)
    for index, row in dataset.iterrows():
        text_2 = " ".join(Pre_Processing(row[col_name]))
        text_2 = nlp(text_2)
        sim.append(text_1.similarity(text_2))
    
    df_sim = pd.DataFrame(sim,columns=['spacy_sim'+'_{col_name}'.format(col_name=col_name)],index=dataset.index)
        
    return pd.concat([df_sim,dataset],axis=1)