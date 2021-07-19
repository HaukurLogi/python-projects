import random


all_genders = ["female", "male"]
gender = random.choice(all_genders)

boy_first_names = ["Árni", "Haukur", "Kristófer", "Birnir", "Jón" ,"Eiríkur", "Egill", "Dagur", "Guðmundur", "Gunnar", "Gauti", "Smári", "Guðjón", "Guðfinnur", "Guðni", "Benidikt", "Hilmar", "Hilmir", "Axelander", "Jónatan"]
boy_last_names = ["Eyðar", "Vikingur", "Dofri", "Ágúst", "Hauksson", "Þór", "Már", "Snær", "Hólmsteinn", "Blómhvist", "Steinn", "Kári", "Breki", "Freyr", "Vilberg", "Snorri", "Trausti", "Ær", "Helgi", "Axelson"]
girl_first_names = ["Máney", "Erla"]
girl_last_names = ["Þula", "Sólbjört"]


if gender == "female":
    print(random.choice(girl_first_names), random.choice(girl_last_names))
if gender == "male":
    print(random.choice(boy_first_names), random.choice(boy_last_names))
