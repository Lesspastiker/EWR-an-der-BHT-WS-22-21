# EWR1

### Von Alfred W. und Lennard C.

## Benutzung 

  - ### Generell:
    ```python 
    # das Modul importieren
    from Stripmethod import Stripmethod

    # Ein Object der Klasse erstellen 
    S = Stripmethod(funktion, linke_grenze, rechte_grenze, iterationen)
    ```
    >Dabei bestimmen die linke und rechte grenze das Intervall und "iterationen" die Anzahl an Rechtecken oder Streifen die errechnet werden sollen

    um dann zu ploten muss nur noch:
    ```python
    # zum Plotten der Untersumme
    S.plotUntersumme()

    # zum Plotten der Obersumme
    S.plotObersumme()

    # zum Plotten der Ober - und Untersumme
    S.plotOberUnter()

    ```
  - ### Mit vordefinierter Funktion
    > Eine einfache Beisspiel-Funktion:
    ```python
    def f(x:int) -> float:
      return x**2
    ```
    Diese Funktion kann man nun einfach als erstes Argument übergeben:

    ```python 
    from Stripmethod import Stripmethod
    A = Stripmethod(f, -5, 50, 1000)
    
    A.plotOberUnter()
    ```
  - ### Mit einfacher Lambda Funktion
    > Wenn man eine lambda funktion benutzen will, übergibt man diese einfach als erstes Argument:
    ```python
    from Stripmethod import Stripmethod
    A = Stripmethod(lambda x: x**2 , -5, 50, 1000) 

    ``` 
        
    Die kann auch mit jeglicher Numerischen Funktion in Python verwenden:
    ```python
    from Stripmethod import Stripmethod
    import math as m 
    A = Stripmethod(lambda x: m.sin(x), -5, 50, 1000)
    
    A.plotOberUnter()
    ```

  - ### Mit Python Syntax
    > #### Um Funktionen in einfacher Python Syntax zu verwenden, kann man den lambda_parser() benutzen der nur den Funktionsterm als string benötigt:

    ```python
    from Stripmethod import Stripmethod
    from Stripmethod import lambda_parser

    A = Stripmethod(lambda_parser("2*x**2") , -5, 50, 1000) 
    
    A.plotOberUnter()
    ``` 
  
  - ### Berrechnungen ohne Plot
  
    #### Die Ober - und Untersumme lässt sich auch berrechnen ohne das ein Plot errechnet werden muss:

    ```python
    from Stripmethod import Stripmethod
    
    A = Stripmethod(lambda x: x**2 , -5, 50, 1000) 

    # Liefert die Untersumme als float 
    A.Untersumme(lambda x: x**2 , -10, 5, 10) 

    # Liefert die Obersumme als float 
    A.Obersumme(lambda x: x**2 , -10, 5, 10) 
    ```
  
  



## Quellen:
- https://www.geogebra.org/m/wuUQ3JMF
- https://www.mathe-total.de/Buecher/mathe-total-pdfs/Integralrechnung-Ober-Untersummen.pdf
- https://www.statology.org/matplotlib-rectangle/
  - style: https://matplotlib.org/3.3.2/api/_as_gen/matplotlib.patches.Rectangle.html
- https://matplotlib.org/


  
 
