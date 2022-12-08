# Ejercicio 1 
def buscar_palindromo(palindromo):
    palindromos = []
    letra = ""
    for i in range(len(palindromo)):
        letra = palindromo[i] #a
        for j in range(i+1, len(palindromo)):
            letra += palindromo[j] #acumulador 
            if letra == letra[: :-1] and len(letra) > 2: #condicion que comprueba el palindromo
                palindromos.append(letra) 
    return palindromos
print(buscar_palindromo("afoolishconsistencyisthehobgoblinoflittlemindsadoredbylittlestatesmenandphilosophersanddivineswithconsistencyagreatsoulhassimplynothingtodohemayaswellconcernhimselfwithhisshadowonthewallspeakwhatyouthinknowinhardwordsandtomorrowspeakwhattomorrowthinksinhardwordsagainthoughitcontradicteverythingyousaidtodayahsoyoushallbesuretobemisunderstoodisitsobadthentobemisunderstoodpythagoraswasmisunderstoodandsocratesandjesusandlutherandcopernicusandgalileoandnewtonandeverypureandwisespiritthatevertookfleshtobegreatistobemisunderstood"))