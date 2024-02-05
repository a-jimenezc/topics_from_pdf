EN_TOPICS_FROM_LISTS = '''Describe the topics of each of the double-quote delimited lists in a simple sentence and also write down three possible different subtopics. The lists are the result of an algorithm for topic discovery.
        Do not provide an introduction or a conclusion, only describe the topics. Avoid using the words "topic" and "subtopic".
        Use the following template for the response.

        topic 1: <<<(sentence describing the topic)>>>
        - <<<(Phrase describing the first subtopic)>>>
        - <<<(Phrase describing the second subtopic)>>>
        - <<<(Phrase describing the third subtopic)>>>

        topic 2: <<<(sentence describing the topic)>>>
        - <<<(Phrase describing the first subtopic)>>>
        - <<<(Phrase describing the second subtopic)>>>
        - <<<(Phrase describing the third subtopic)>>>

        ...

        topic n: <<<(sentence describing the topic)>>>
        - <<<(Phrase describing the first subtopic)>>>
        - <<<(Phrase describing the second subtopic)>>>
        - <<<(Phrase describing the third subtopic)>>>

        Lists: """{string_lda}""" '''

ES_TOPICS_FROM_LISTS = '''Responde en español. Describe el tema de cada una de las listas delimitadas por comillas en una oración sencilla y escribe además tres posibles subtemas diferentes. Las listas son el resultado de un algoritmo para descubrir temas.
        No des una introducción ni una conclusión, solo describe los temas.
        Utiliza el siguiente Template para la respuesta. Limita a devolver las descripciones de las secciones, evita usar las palabras temas y subtemas en la respuesta. 

        Tema  1: <<<(oración que describe el tema)>>>
        - <<<Frase que describe primer subtema)>>>
        - <<<(Frase que describe segundo subtema)>>>
        - <<<Frase que describe tercer subtema)>>>

        Tema  2: <<<(oración que describe el tema)>>>
        - <<<Frase que describe primer subtema)>>>
        - <<<(Frase que describe segundo subtema)>>>
        - <<<Frase que describe tercer subtema)>>>
        
        ...

        Tema  n: <<<(oración que describe el tema)>>>
        - <<<Frase que describe primer subtema)>>>
        - <<<(Frase que describe segundo subtema)>>>
        - <<<Frase que describe tercer subtema)>>>
        
        Listas: """{string_lda}""" '''
