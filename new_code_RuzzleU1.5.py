Python 3.9.12 (tags/v3.9.12:b28265d, Mar 23 2022, 23:52:46) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> da  itertools  importa  permutazioni , combinazioni

classe  calcComb ():

    def  __init__ ( self , stringa ):

        sé . __N  =  len ( stringa )
        sé . __stringa  =  stringa
        sé . __listStringa  =  lista ( stringa )
        sé . __anagrammi  =  anagrammi ( auto . __stringa )

    def  get_stringa ( auto ):
        ritorno  di sé . __stringa

    def  get_listStringa ( auto ):
        ritorno  di sé . __listStringa

    def  setStringa ( auto ):
        '''
        modificare questo metodo in modo da verificare la coerenza delle variabili di
        istanza presente
        '''
        ritorno  0

    def  charRipetuti ( auto ):
        '''
        questo metodo deve creare un dizionario all'interno del quale la chiave deve essere
        il singolo carattere, il valore deve essere il numero di ripetizioni di quel carattere
        
        esempi di dizionario sono presenti nel file elementi_base/dictionary.py
        '''

    def  cerca ( stringa ):
        
        
        it  =  'words.italian.txt'
        f  =  aperto ( it , 'r' )
        riga  =  f . riga di lettura ()
        valore_stringa  =  Falso

        per la  riga  in  f :

            se  stringa  ==  riga [: - 1 ]:
                valore_stringa  =  True  #"vero" è una stringa, deve recuperare un valore booleano

        return  False   # restituisce falso se non la trova
        

    def  fattoriale ( n ):
        '''
        Implementa una qualunque versione della funzione fattoriale
        questo metodo può essere omessa se si utilizza un metodo built in delle
        librerie standard
        '''

    def  coeffBinom ( n , k ):
        '''
        implementare la formula del coefficiente binomiale a partire dalla fattoriale
        questo metodo può essere evitato se ri richiama una delle funzioni integrate
        delle librerie standard
        '''
        passaggio

    def  anagrammi ( self , stringa ):
    

        sé . __lettera  =  lista ( stringa )

        sé . __permutazioni  =  lista ( permutazioni ( self . __lettere ))

        temp  =  ''
        sé . __anagrammi  = []


        per  me  in me  stesso . __permutazioni :
            per  carattere  in  i :
        
                temp  +=  carattere 

    
            sé . __anagrammi . aggiungere ( temp )
    
            temp  =  ''

        ritorno  di sé . __anagrammi  # in realtà basta salvarlo nella variabile di istanza
    
        
    
    def  confUtil ( self ):
       
       it  =  'words.italian.txt'
       f  =  aperto ( it , 'r' )
       riga  =  f . riga di lettura ()
       


       per  me  in me  stesso . __anagrammi :
            stringa  =  sé . __anagrammi [ i ]
            io  = +  1
            per la  riga  in  f :
                se  stringa  ==  riga [: - 1 ]:
                    stampa ( stringa )
                    ritorno  "vero"


    # PERMUTAZIONI

    def  nPermutSenzaRip ( self ):
        '''
        restituire il numero di permutazioni SENZA ripetizione
        '''
        ritorno  0

    def  nPermutConRip ( auto ):
        '''
        restituire il numero di permutazioni CON ripetitivo
        '''
        ritorno  0

    def  permutSenzaRip ( self ):
        '''
        generare e ripristinare la lista di permutazioni SENZA ripetitiva
        '''
        ritorno  0

    def  permutConRip ( self , stringa ):
        permutazioneRipetizioni  =  lista ( permutazioni ( stringa ))

        ritorno  permutazioneRipetizioni

    # DISPOSIZIONI

    def  nDispSemplSenzaRip ( self ):
        '''
        ripristinare il numero di disposizioni semplici SENZA ripetitiva
        '''
        ritorno  0

    def  nDispSemplConRip ( self ):
        '''
        ripristinare il numero di disposizioni semplici CON ripetitivi
        '''
        ritorno  0

    def  dispSemplSenzaRip ( self ):
        '''
        generare e ripristinare la lista delle disposizioni semplici SENZA ripetitiva
        '''
        ritorno  0


    def  dispSemplConRip ( self ):
        '''
        generare e ripristinare la lista delle disposizioni semplici CON ripetizione
        '''
        ritorno  0

    # COMBINAZIONI

    def  nCombSemplSenzaRip ( self ):
        '''
        restituire il numero delle combinazioni SENZA ripetitiva
        '''
        ritorno  0

    def  nCombSemplConRip ( self ):
        '''
        restituire il numero delle combinazioni CON ripetitivo
        '''
        ritorno  0

    def  combSenzaRip ( self ):
        '''
        generare e restituire la lista delle combinazioni SENZA ripetitiva
        '''
        ritorno  0


    def  combConRip ( self ):
        '''
        generare e restituire la lista delle combinazioni CON ripetitiva
        '''
        ritorno  0

    #PROBABILITA'

    def  probConfUtil ( self ):
        passaggio